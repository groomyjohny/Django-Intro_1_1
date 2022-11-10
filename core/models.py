from django.db import models
import datetime


class EmergencyServiceModel(models.Model):
    """Модель экстренной службы"""
    name = models.CharField('Название', max_length=255)
    service_code = models.CharField('Код службы', max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=255)

    def __str__(self):
        return f'{self.name}, код {self.service_code}, номер {self.phone_number}'

    class Meta:
        verbose_name = 'Экстренная служба'
        verbose_name_plural = 'Экстренные службы'
        ordering = ('service_code',)


class ServicePrintable:
    def services_string(self):
        """Возвращает названия служб, задействованных в этом обращении, в виде строки.
        Если их нет, то возращается строка '(нет служб)'"""
        s = ', '.join([i.name for i in self.services.all()])
        if not s:
            return '(нет служб)'
        return s

    services_string.short_description = 'Задействованные службы'


class AccidentModel(models.Model, ServicePrintable):
    """Модель происшествия"""
    number = models.PositiveIntegerField('Номер')
    injured_count = models.PositiveIntegerField('Количество пострадавших')
    dont_call = models.BooleanField('Не звонить', default=False)
    services = models.ManyToManyField(EmergencyServiceModel, blank=True)
    addition_datetime = models.DateTimeField('Дата добавления', null=True)  # consider auto_add_now

    def __str__(self):
        return f"Происшествие №{self.number}, пострадавших: {self.injured_count}, дата: {self.addition_datetime}"

    class Meta:
        verbose_name = 'Происшествие'
        verbose_name_plural = 'Происшествия'
        indexes = (
            models.Index(fields=['number']),
        )


class ApplicantModel(models.Model):
    """Модель заявителя"""
    class GenderChoices(models.TextChoices):  # можно через tuple сделать
        M = 'М'  # строка 'М' - русская, поле - латинское
        F = 'Ж'
    surname = models.CharField('Фамилия', default='', max_length=255)
    first_name = models.CharField('Имя', default='', max_length=255)
    patronymic_name = models.CharField('Отчество', default='', max_length=255)
    birth_date = models.DateField('Дата рождения', null=True)
    phone_number = models.CharField('Номер телефона', default='', blank=True, max_length=255)
    health_state = models.TextField('Состояние здоровья', blank=True, default='практически здоров',
                                    help_text='аллергоанамнез, хронические заболевания и т.п.')
    accidents = models.ManyToManyField(AccidentModel, blank=True, verbose_name='Происшествия')  # verbose_name можно здесь, переделать само отношение
    gender = models.CharField('Пол', max_length=1, choices=GenderChoices.choices, default=GenderChoices.M)
    image = models.ImageField('Изображение', blank=True)

    def __str__(self):
        try:
            return f'Заявитель {self.full_name()}, пол: {self.gender}, р. {self.birth_date}, телефон: {self.phone_number}'
        except TypeError:
            return f'(Ошибка при получении описания экземляра {self.__class__.__name__})'

    def full_name(self):
        try:
            return ' '.join([self.surname, self.first_name, self.patronymic_name])
        except TypeError:
            return '(не удалось получить полное имя)'
    full_name.short_description = 'ФИО'

    class Meta:
        verbose_name = 'Заявитель'
        verbose_name_plural = 'Заявители'
        ordering = ('surname', 'first_name', 'patronymic_name')


class AppealModel(models.Model, ServicePrintable):
    """Модель обращения"""
    class StatusChoice(models.TextChoices):
        IN_PROGRESS = 'В работе'
        DONE = 'Завершено'
    date = models.DateTimeField('Дата', default=datetime.datetime.now)
    number = models.PositiveIntegerField('Номер')
    card_number = models.PositiveIntegerField('Номер карточки', unique=True, editable=False, null=True)
    applicant = models.ForeignKey(ApplicantModel, on_delete=models.CASCADE, related_name='appeals', verbose_name='Заявитель')
    services = models.ManyToManyField(EmergencyServiceModel, blank=True, verbose_name='Задействованные службы')
    status = models.CharField("Статус", max_length=16, choices=StatusChoice.choices, default=StatusChoice.IN_PROGRESS)
    description = models.TextField("Описание", blank=True, default='')

    def applicant_name(self):
        """Возвращает ФИО заявителя этого обращения"""
        return self.applicant.full_name()
    applicant_name.short_description = 'ФИО заявителя'

    def __str__(self):
        return f'Обращение №{self.number} от {self.date}, заявитель: {self.applicant_name()}'

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ('date', 'number')
