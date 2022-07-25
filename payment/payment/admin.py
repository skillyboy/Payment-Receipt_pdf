from django.contrib import admin
from .models import *

# Register your models here.
class ProcessorAdmin(admin.ModelAdmin):
    list_display = ('id','name','value')
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','fee')
    
class Transactiondmin(admin.ModelAdmin):
    list_display = ('id','user','processor','confirmation_code','amount','status','date')
   
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','pending_transactions_id','paid_transactions_id','total_paid_amount','username','last_name','full_name')
   
class PollAdmin(admin.ModelAdmin):
    list_display = ('id','user','question','answer1','answer2','answer3','answer4')
   
    
admin.site.register(Processor,ProcessorAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Transaction,Transactiondmin)
admin.site.register(UserProfile,UserProfileAdmin)
