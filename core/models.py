from django.db import models
import datetime


class EmergencyServiceModel(models.Model):
    """Модель экстренной службы"""
    name = models.CharField('Название', max_length=128)
    service_code = models.PositiveIntegerField('Код службы')
    phone_number = models.CharField('Номер телефона', max_length=16)

    def __str__(self):
        return f'{self.name}, код {self.service_code}, номер {self.phone_number}'

    class Meta:
        verbose_name = 'Экстренная служба'
        verbose_name_plural = 'Экстренные службы'
        ordering = ['service_code']


class ApplicantModel(models.Model):
    """Модель заявителя"""
    class GenderChoices(models.TextChoices):
        M = 'М'  # строка 'М' - русская, поле - латинское
        F = 'Ж'
    full_name = models.CharField('ФИО', max_length=128)
    birth_date = models.DateField('Дата рождения')
    phone_number = models.BigIntegerField('Номер телефона', blank=True)
    health_state = models.TextField('Состояние здоровья', blank=True, default='практически здоров',
                                    help_text='аллергоанамнез, хронические заболевания и т.п.')
    gender = models.CharField('Пол', max_length=1, choices=GenderChoices.choices, default=GenderChoices.M)
    image = models.ImageField("Изображение", blank=True)

    def __str__(self):
        return f'Заявитель {self.full_name}, пол: {self.gender}, р. {self.birth_date}, телефон: {self.phone_number}'

    class Meta:
        verbose_name = 'Заявитель'
        verbose_name_plural = 'Заявители'
        ordering = ['full_name']


class AppealModel(models.Model):
    """Модель обращения"""
    date = models.DateTimeField('Дата', default=datetime.datetime.now())
    number = models.PositiveIntegerField('Номер')
    applicant = models.ForeignKey(ApplicantModel, on_delete=models.CASCADE, related_name='appeals')
    services = models.ManyToManyField(EmergencyServiceModel, blank=True)

    def applicant_name(self):
        """Возвращает ФИО заявителя этого обращения"""
        return self.applicant.full_name
    applicant_name.short_description = 'ФИО заявителя'

    def services_string(self):
        """Возвращает названия служб, задействованных в этом обращении, в виде строки.
        Если их нет, то возращается строка '(нет служб)'"""
        s = ', '.join([i.name for i in self.services.all()])
        if s == '':
            return '(нет служб)'
        else:
            return s
    services_string.short_description = 'Задействованные службы'

    def __str__(self):
        return f'Обращение №{self.number} от {self.date}, заявитель: {self.applicant_name()}'

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ['date', 'number']


class AccidentModel(models.Model):
    """Модель происшествия"""
    card_number = models.PositiveIntegerField('Номер карточки')
    injured_count = models.PositiveIntegerField('Количество пострадавших')
    dont_call = models.BooleanField('Не звонить')

    class Meta:
        verbose_name = 'Происшествие'
        verbose_name_plural = 'Происшествия'
