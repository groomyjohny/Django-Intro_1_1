from django.db import models

# Create your models here.
class EmergencyServiceModel(models.Model):
    name = models.CharField('Название', max_length=128)
    serviceCode = models.IntegerField('Код службы')
    phoneNumber = models.BigIntegerField('Номер телефона') #TODO: maybe char field?

class ApplicantModel(models.Model):
    fullName = models.CharField('ФИО', max_length=128)
    phoneNumber = models.BigIntegerField('Номер телефона')
    healthState = models.TextField("Состояние здоровья")

class AppealModel(models.Model):
    date = models.DateTimeField("Дата")
    number = models.IntegerField("Номер")
    applicantId = models.ForeignKey(ApplicantModel, on_delete=models.CASCADE)