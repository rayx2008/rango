from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class Bill(models.Model):
	timestamp = models.DateTimeField()
	creator = models.TextField()
	bill_of_lading_no = models.TextField()
	plan_wt = models.DecimalField(0,max_digits=10,decimal_places = 3)
	finish_wt = models.DecimalField(0,max_digits=10,decimal_places = 3)
	balance_user_name = models.TextField()
	def __unicode__(self):
		return self.creator

class BillAdmin(admin.ModelAdmin):
	list_display = ('bill_of_lading_no','plan_wt','finish_wt','balance_user_name')

admin.site.register(Bill,BillAdmin)