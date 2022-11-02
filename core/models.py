from django.db import models

# Create your models here.
class EmergencyServiceModel(models.Model):
    name = models.CharField('Название', max_length=128)
    serviceCode = models.IntegerField('Код службы')
    phoneNumber = models.CharField('Номер телефона', max_length=16)

    class Meta:
        verbose_name = "Экстренная служба"
        verbose_name_plural = "Экстренные службы"

class ApplicantModel(models.Model):
    fullName = models.CharField('ФИО', max_length=128)
    phoneNumber = models.BigIntegerField('Номер телефона')
    healthState = models.TextField("Состояние здоровья")

    class Meta:
        verbose_name = "Заявитель"
        verbose_name_plural = "Заявители"
class AppealModel(models.Model):
    date = models.DateTimeField("Дата")
    number = models.IntegerField("Номер")
    applicantId = models.ForeignKey(ApplicantModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"