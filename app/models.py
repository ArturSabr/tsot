from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class EventModel(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.CharField(max_length=255)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='events/images')

    def __str__(self):
        return f'{self.title} | {self.date}'


class EmployeeModel(models.Model):
    Firstname = models.CharField(max_length=255)
    MiddleName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    body = RichTextUploadingField(blank=True, null=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='employees/images')
    position = models.CharField(max_length=123, default='Сотрудник', blank=True)

    def __str__(self):
        return f'{self.Firstname} | {self.MiddleName}'

    def get_full_name(self):
        return f'{self.Firstname} {self.MiddleName}'

