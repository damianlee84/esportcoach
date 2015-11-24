from django.db import models
from django.conf import settings
from datetime import date, datetime
from calendar import monthrange

class Signup(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=50, blank = False, null=False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now="True")

    mmr = models.CharField(max_length=50, blank = False, null=False)
    server = models.CharField(max_length=50, blank = False, null=False)
    hero = models.CharField(max_length=50, blank = False, null=False)
    rating = models.PositiveIntegerField(blank = False, null=False)
    reputation = models.PositiveIntegerField(blank = False, null=False)
    students = models.CharField(max_length=50, blank = False, null=False)
    pricerate = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.full_name



class User(models.Model):
    username = models.CharField(primary_key=True, max_length = 100, blank = False, null = False)
    password = models.CharField(max_length = 100, blank = False, null = False)
    email = models.CharField(max_length = 100, blank = False, null = False)
    name = models.CharField(max_length = 100, blank = False, null = False)
    def __str__(self):
        return self.username + " " + self.email + " " + self.name

class Coach(models.Model):
   username = models.ForeignKey(User)
   MMR = models.IntegerField(default=0,  blank = False, null = False)
   hero = models.CharField(max_length = 500, blank = False, null = False)
   rank = models.IntegerField(default = 0)
   server = models.CharField(max_length = 50, blank = False, null = False)
   rating = models.IntegerField(default = 5,  blank = False, null = False)
   hour_rate = models.FloatField(default = 0.00)
   def __str__(self):
        return self.username + " " + self.hero + " " + self.rank + " " + self.server + " " + self.server + " " + self.hour_rate

class Tutee(models.Model):
    username = models.ForeignKey(User)

class Admin(models.Model):
    username = models.ForeignKey(User)

class register(models.Model):
    username = models.ForeignKey(User)
    rdate = models.DateTimeField(auto_now_add = False, auto_now = "True")

class transaction(models.Model):
    def __init__(self, *args, **kwargs):
        super(transaction, self).__init__(*args, **kwargs)
        
        import stripe
        stripe.api.key = settings.STRIPE_API_KEY
        self.stripe = stripe
        
    #transaction number    
    transaction_id = models.CharField(max_length = 32)
    transaction_date = models.models.DateTimeField(auto_now_add = True, auto_now=False)
    
    
        
        
        
        
        
        
        
        
    
