from django.db import models
from django.contrib.auth.models import User
# Create your models here.


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

class HouseholdData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_no = models.CharField(max_length=12)
    religion = models.CharField(max_length=50)
    cast = models.CharField(max_length=50)
    family_male = models.PositiveIntegerField()
    family_female = models.PositiveIntegerField()
    head_of_family = models.CharField(max_length=100)
    earning_members = models.PositiveIntegerField()

    # Monthly Expenses
    groceries = models.FloatField(default=0.0)
    recharge = models.FloatField(default=0.0)
    electronics = models.FloatField(default=0.0)
    teaching = models.FloatField(default=0.0)
    stationary = models.FloatField(default=0.0)
    clothing = models.FloatField(default=0.0)
    health = models.FloatField(default=0.0)
    others = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "household_data"
    def __str__(self):
        return self.name
    def total_expense(self):
        return sum([
            self.groceries or 0,
            self.recharge or 0,
            self.electronics or 0,
            self.teaching or 0,
            self.stationary or 0,
            self.clothing or 0,
            self.health or 0,
            self.others or 0,
        ])

    def __str__(self):
        return self.name

class Progress_report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=12)
    plan_amount = models.FloatField()
    plan_duration = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "progress_report"
    def __str__(self):
        return self.name