from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class OfficeModel(models.Model):
    class Meta:
        db_table = 'office'

    name = models.CharField(max_length=20,
                            validators=[RegexValidator('^([a-zA-Z]{3,20})$', message='only a-z A-Z min 3 max 20')])
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class EmployeeModel(models.Model):
    class Meta:
        db_table = 'employee'

    name = models.CharField(max_length=20,
                            validators=[RegexValidator('^([a-zA-Z]{3,20})$', message='only a-z A-Z min 3 max 20')])
    age = models.IntegerField()
    city = models.CharField(max_length=20)
    office = models.ForeignKey(OfficeModel, related_name='employees', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
