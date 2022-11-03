from django.db import models
import datetime


class EmergencyServiceModel(models.Model):
    """Модель экстренной службы"""
    name = models.CharField('Название', max_length=128)
    service_code = models.CharField('Код службы', max_length=16)
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
    first_name = models.CharField("Имя", max_length=40, null=True)
    surname = models.CharField("Фамилия", max_length=40, null=True)
    patronymic_name = models.CharField("Отчество", max_length=40, null=True)
    birth_date = models.DateField('Дата рождения', null=True)
    phone_number = models.CharField('Номер телефона', blank=True, null=True, max_length=20)
    health_state = models.TextField('Состояние здоровья', blank=True, default='практически здоров',
                                    help_text='аллергоанамнез, хронические заболевания и т.п.')
    gender = models.CharField('Пол', max_length=1, choices=GenderChoices.choices, default=GenderChoices.M)
    image = models.ImageField("Изображение", blank=True)

    def __str__(self):
        try:
            return f'Заявитель {self.surname} {self.first_name} {self.patronymic_name}, пол: {self.gender}, р. {self.birth_date}, телефон: {self.phone_number}'
        except TypeError:
            return f'(Ошибка при получении описания экземляра {self.__class__.__name__})'

    #def __repr__(self):
        #return "<%s: %s>" % ('ApplicantModel', self.getStringRepresentation())
        # TODO: not defining this causes infinite recursion. __str__ tries to call __repr__, which calls __str__ again, etc
        # defining causes admin panel for Appeal to stop showing Applicant name
        #return "Stub"

    def full_name(self):
        try:
            return ' '.join([self.surname, self.first_name, self.patronymic_name])
        except TypeError:
            return '(не удалось получить полное имя)'
    full_name.short_description = 'ФИО'

    class Meta:
        verbose_name = 'Заявитель'
        verbose_name_plural = 'Заявители'
        # this is similar to full_name if Surname FirstName Patronymic format is used (i.e. Kuznetzov Anton Ivanovich)
        ordering = ['surname', 'first_name', 'patronymic_name']


class AppealModel(models.Model):
    """Модель обращения"""
    class StatusChoice(models.TextChoices):
        IN_PROGRESS = 'В работе'
        DONE = 'Завершено'
    date = models.DateTimeField('Дата', default=datetime.datetime.now)
    number = models.PositiveIntegerField('Номер')
    card_number = models.PositiveIntegerField('Номер карточки', unique=True, editable=False, null=True)
    applicant = models.ForeignKey(ApplicantModel, on_delete=models.CASCADE, related_name='appeals')
    applicant.verbose_name = "Заявитель"
    services = models.ManyToManyField(EmergencyServiceModel, blank=True)
    services.verbose_name = "Задействованные службы"
    status = models.CharField("Статус", max_length=16, choices=StatusChoice.choices, default=StatusChoice.IN_PROGRESS)

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
    number = models.PositiveIntegerField('Номер')
    injured_count = models.PositiveIntegerField('Количество пострадавших')
    dont_call = models.BooleanField('Не звонить')
    services = models.ManyToManyField(EmergencyServiceModel, blank=True)
    addition_datetime = models.DateTimeField("Дата добавления", null=True)

    def services_string(self): #TODO: exact repeat of code from AppealModel, needs rework to remove this copy
        """Возвращает названия служб, задействованных в этом обращении, в виде строки.
        Если их нет, то возращается строка '(нет служб)'"""
        s = ', '.join([i.name for i in self.services.all()])
        if s == '':
            return '(нет служб)'
        else:
            return s
    services_string.short_description = 'Задействованные службы'

    class Meta:
        verbose_name = 'Происшествие'
        verbose_name_plural = 'Происшествия'
        indexes = [
            models.Index(fields=['number'])
        ]
