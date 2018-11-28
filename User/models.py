from django.db import models
from django.utils import timezone


class donationtype(models.Model):
    name = models.TextField(max_length=200)
    monthlyComitment = models.BooleanField



class UserType(models.Model):
    role = models.CharField(max_length=50)



class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    role = models.ForeignKey(UserType, on_delete=models.CASCADE)
    donation = models.ForeignKey(donationtype, on_delete=models.CASCADE)
    userNamed = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=200)



    def __str__(self):
        return self.firstname + "   " + self.lastname + "   " + str(self.donation) + "   " + str(self.created_date.date())




class donationMade(models.Model):
    Amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donation = models.ForeignKey(donationtype, on_delete=models.CASCADE)