from django.db import models

# Create your models here.
class EmergencyServiceModel(models.Model):
    name = models.CharField('Название', max_length=128)
    serviceCode = models.IntegerField('Код службы')
    phoneNumber = models.CharField('Номер телефона', max_length=16)

    def __str__(self):
        return f"{self.name}, код {self.serviceCode}, номер {self.phoneNumber}"

    class Meta:
        verbose_name = "Экстренная служба"
        verbose_name_plural = "Экстренные службы"
        ordering = ['serviceCode']

class ApplicantModel(models.Model):
    fullName = models.CharField('ФИО', max_length=128)
    phoneNumber = models.BigIntegerField('Номер телефона')
    healthState = models.TextField("Состояние здоровья")

    def __str__(self):
        return f"Заявитель {self.fullName}, телефон: {self.phoneNumber}"
    class Meta:
        verbose_name = "Заявитель"
        verbose_name_plural = "Заявители"
        ordering = ['fullName']
class AppealModel(models.Model):
    date = models.DateTimeField("Дата")
    number = models.IntegerField("Номер")
    applicantId = models.ForeignKey(ApplicantModel, on_delete=models.CASCADE, related_name='appeals')

    def applicantName(self):
        return self.applicantId.fullName
    applicantName.short_description = "ФИО заявителя"

    def __str__(self):
        #return f"Обращение №{self.number} от {self.date}, заявитель: {self.applicantName()}"
        return f"Обращение №{self.number} от {self.date}, заявитель: {self.applicantName()}"

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"
        ordering = ['date', 'number']