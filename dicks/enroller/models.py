from django.db import models

# Create your models here.



class Role(models.Model):
    role_name = models.CharField(max_length=32)
    role_definitiion = models.CharField(max_length=32)



class Client(models.Model):
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    name_extension = models.CharField(max_length=12)
    address = models.CharField(max_length=None)
    gender = models.CharField(max_length=32)
    civil_status = models.CharField(max_length=12)
    birth_date = models.DateField()
    # contact_number = models.PhoneNumberField(null-False, blank=False, unique=False)
    email = modes.EmailField()
    # role=models.ForeignKey(Role)
    
    
    
class Branch(models.Model)
    branch_name = models.CharField(max_length=32)
    address = models.CharField(max_length=None)
    
    
    
class Designation(models.Model):
    designation_name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    
    
    
class Credits(models.Model):
    amount = models.DecimalField(max_digits=None, decimal_places=10)
    # owner = models.ForeignKey(Agent)
    
    
    
class Agent(model.Models):
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    # branch = models.ForeignKey(Branch)
    # designation = models.ForeignKey(Designation)