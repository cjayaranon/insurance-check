from django.db import models

# Create your models here.



class Role(models.Model):
    role_name = models.CharField(max_length=32)
    role_definitiion = models.CharField(max_length=32)

    def __str__(self):
        return self.role_name



class Branch(models.Model):
    branch_name = models.CharField(max_length=32)
    address = models.CharField(max_length=120)
    
    def __str__(self):
        return self.branch_name



class Client(models.Model):
    GENDER = (
        ('MALE', 'He/Him'),
        ('FEMALE', 'She/Her'),
        ('OTHER', 'Other'),
        ('NOT_SAY', 'Prefer Not To Say'),
    )
    
    CIV_STAT = (
        ('SINGLE', 'Single'),
        ('MARRIED', 'Married'),
        ('SEPARATED', 'Separated'),
        ('WIDOWED', 'Widowed/Widower'),
        ('OTHER', 'Other')
    )
    iaccs_id = models.IntegerField(default=0)
    membership_branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    name_extension = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=120)
    gender = models.CharField(max_length=32, choices=GENDER)
    civil_status = models.CharField(max_length=12, choices=CIV_STAT)
    birth_date = models.DateField()
    # contact_number = models.PhoneNumberField(null-False, blank=False, unique=False)
    email = models.EmailField()
    role=models.ForeignKey(Role, on_delete=models.PROTECT)
    
    # def __str__(self):
    #     return 'Policy: ' + self.name
    
    
    
class Designation(models.Model):
    designation_name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    
    def __str__(self):
        return self.designation_name
    
    
    
class Agent(models.Model):
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.last_name + str(self.id)
    
    
    
class Credits(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    owner = models.ForeignKey(Agent, on_delete=models.PROTECT)
    
    
    
class PremiumAmount(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    
    
    
class CutoffPeriod(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    
    
    
class ClientTagging(models.Model):
    tag_name = models.CharField(max_length=32)
    tag_description = models.CharField(max_length=32)
    
    
    
class PaymentType(models.Model):
    type_name = models.CharField(max_length=32)
    
    
    
class PaymentDetails(models.Model):
    payor = models.ForeignKey(Client, on_delete=models.PROTECT)
    encoder_branch = models.ForeignKey(Branch, related_name='encoder', on_delete=models.PROTECT)
    membership_branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    date_of_payment = models.DateField()
    cutoff_period = models.ForeignKey(CutoffPeriod, on_delete=models.PROTECT)
    premium_paid = models.ForeignKey(PremiumAmount, on_delete=models.PROTECT)
    auth_agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    tagging = models.ForeignKey(ClientTagging, on_delete=models.PROTECT)
    