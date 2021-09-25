from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    middle_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32)
    name_extension = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=120, blank=True)
    gender = models.CharField(max_length=32, choices=GENDER, blank=True)
    civil_status = models.CharField(max_length=12, choices=CIV_STAT, blank=True)
    birth_date = models.DateField()
    # contact_number = models.PhoneNumberField(null-False, blank=False, unique=False)
    email = models.EmailField(blank=True)
    role=models.ForeignKey(Role, on_delete=models.PROTECT)
    
    def __str__(self):
        return '%s, %s %s' % (self.last_name, self.first_name, self.middle_name)
    
    
    def get_payments(self):
        return self.paymentdetails.select_related('payor')
    
    
    
class Designation(models.Model):
    designation_name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    
    def __str__(self):
        return self.designation_name
    
    
    
class Agent(models.Model):
    # first_name = models.CharField(max_length=32)
    # middle_name = models.CharField(max_length=32)
    # last_name = models.CharField(max_length=32)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.user)
        
        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Agent.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.agent.save()
    
    
    
class Credits(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    owner = models.ForeignKey(Agent, on_delete=models.PROTECT)
    
    
    
class PremiumAmount(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    
    
    def __str__(self):
        return str(self.amount)
    
    
    
class CutoffPeriod(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    
    
    def __str__(self):
        return '%s to %s' % (self.from_date, self.to_date)
    
    
    
class ClientTagging(models.Model):
    tag_name = models.CharField(max_length=32)
    tag_description = models.CharField(max_length=32)
    
    
    def __str__(self):
        return self.tag_name
    
    
    
class PaymentType(models.Model):
    type_name = models.CharField(max_length=32)
    
    
    def __str__(self):
        return self.type_name
    
    
    
class PaymentDetails(models.Model):
    payor = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='payor')
    encoder_branch = models.ForeignKey(Branch, related_name='encoder', on_delete=models.PROTECT)
    membership_branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    date_of_payment = models.DateField()
    cutoff_period = models.ForeignKey(CutoffPeriod, on_delete=models.PROTECT)
    premium_paid = models.ForeignKey(PremiumAmount, on_delete=models.PROTECT)
    auth_agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    tagging = models.ForeignKey(ClientTagging, on_delete=models.PROTECT)
    beneficiary1 = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='beneficiary1')
    beneficiary2 = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='beneficiary2')
    
    
    def __str__(self):
        return '%s %s' % (self.date_of_payment, self.payor)
    