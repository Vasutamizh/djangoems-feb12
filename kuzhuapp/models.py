from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,MaxLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def maxlen(value):
    count = 0
    for i in str(value):
        count+=1

    if count>12:
        raise ValidationError(
        _("Aadhaar Number must be 12 characters"),
            params={"value": value},
        )


class Member(models.Model):
    Name = models.CharField(max_length=25)
    Age = models.PositiveIntegerField()
    Gaurdian = models.CharField(max_length=25, blank=True, null=True)
    Aadhaarnumber = models.IntegerField(validators=[maxlen],default=00000000000)
    Pannumber = models.CharField(max_length=10, blank=True, null=True)
    Loanamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Image = models.ImageField(upload_to="images/",default="images/default.png")
    emis = models.ManyToManyField('Emi')


    def __str__(self):
        return self.Name

class Emi(models.Model):
    mem = models.ForeignKey(Member, on_delete=models.CASCADE)
    repay = models.PositiveIntegerField()
    Intrest = models.PositiveIntegerField()
    Savings = models.PositiveIntegerField()
    Sandha = models.PositiveIntegerField()
    mon  = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.mem}-{self.mon}"



class Loan(models.Model):
    mem = models.ForeignKey(Member,null=True, on_delete=models.SET_NULL)
    loan = models.PositiveIntegerField()
    intrest = models.CharField(max_length=10, blank=True, null=True)
    mon = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.mem}+{self.loan}"
