from django.db import models


class EmergencyServiceModel(models.Model):
    name = models.CharField('Название', max_length=128)
    service_code = models.IntegerField('Код службы')
    phone_number = models.CharField('Номер телефона', max_length=16)

    def __str__(self):
        return f"{self.name}, код {self.service_code}, номер {self.phone_number}"

    class Meta:
        verbose_name = "Экстренная служба"
        verbose_name_plural = "Экстренные службы"
        ordering = ['service_code']


class ApplicantModel(models.Model):
    full_name = models.CharField('ФИО', max_length=128)
    birth_date = models.DateField("Дата рождения")
    phone_number = models.BigIntegerField('Номер телефона')
    health_state = models.TextField("Состояние здоровья")

    def __str__(self):
        return f"Заявитель {self.full_name}, р. {self.birth_date}, телефон: {self.phone_number}"

    class Meta:
        verbose_name = "Заявитель"
        verbose_name_plural = "Заявители"
        ordering = ['full_name']


class AppealModel(models.Model):
    date = models.DateTimeField("Дата")
    number = models.IntegerField("Номер")
    applicant = models.ForeignKey(ApplicantModel, on_delete=models.CASCADE, related_name='appeals')
    services = models.ManyToManyField(EmergencyServiceModel, blank=True)

    def applicant_name(self):
        return self.applicant.full_name
    applicant_name.short_description = "ФИО заявителя"

    def services_string(self):
        s = ', '.join([i.name for i in self.services.all()])
        if s == '':
            return "(нет служб)"
        else:
            return s
    services_string.short_description = "Задействованные службы"

    def __str__(self):
        return f"Обращение №{self.number} от {self.date}, заявитель: {self.applicant_name()}"

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"
        ordering = ['date', 'number']
