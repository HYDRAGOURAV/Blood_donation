from typing import Any
from django.db import models

class Donor_data(models.Model):
    S_no = models.IntegerField()
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField()
    address = models.TextField(max_length=100, null = False)
    contact_number = models.BigIntegerField()
    email = models.EmailField(max_length=50, null = False)
    Blood_Group = models.TextField(null = False)
    State = models.CharField(max_length=50 , null = False)
    City = models.CharField(max_length=30, null=False)
    def __str__(self) -> str:
        return Donor_data.name , Donor_data.Blood_Group
    def save(self, *args, **kwargs):
        if not self.pk:  
            last_instance = Donor_data.objects.order_by('-S_no').first()
            if last_instance:
                self.S_no = last_instance.S_no + 1
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Serial Number: {self.S_no}"
    

#  FeedBack Model 

class Feedback(models.Model):
    FeedBack_email = models.EmailField(max_length=50, null=False)
    FeedBack = models.TextField(null=False)
    def __str__(self) -> str:
        return self.FeedBack_email

class contact_details(models.Model):
    User_name = models.CharField(max_length=30)
    User_email = models.EmailField(max_length=30)
    User_message = models.TextField()
    def __str__(self) -> str:
        return self.User_name
    
# Payment gatwway 

class  payment(models.Model):
    D_Name = models.CharField(max_length=50)
    D_email = models.EmailField(max_length=50)
    D_Amount = models.IntegerField()
    TransactionID = models.CharField(max_length=200)
    paid = models.BooleanField(default="false")


class delete_data_req(models.Model):
    SNo = models.IntegerField()
    Delete_Name_req = models.CharField(max_length=30)
    Delete_Contact_req = models.BigIntegerField()
    Delete_EMAIL_req = models.EmailField(max_length=50)
    Delete_city_req = models.CharField(max_length=20)
    Delete_address_req = models.CharField(max_length=60)
    Delete_Reason = models.TextField()
    def __str__(self) -> str:
        return self.Delete_Name_req