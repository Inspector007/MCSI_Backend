from django.db import models

# Create your models here.

class State(models.Model):
	stateid = models.IntegerField(primary_key=True)
	statecode = models.CharField(null=False,blank=False,max_length=5)
	statename = models.CharField(verbose_name='State Name',max_length=25)
	statecountry = models.CharField(verbose_name='Country',max_length=30)
	skilled_labour_cost = models.FloatField(default=0.0)
	unskilled_labour_cost = models.FloatField(default=0.0)
	semiskilled_labour_cost = models.FloatField(default=0.0)
	lat = models.FloatField(default=0.0)
	lng = models.FloatField(default=0.0)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.statecode

class LabourCost_State_IndustryWise(models.Model):
	statecode = models.CharField(null=False,blank=False,max_length=5)
	statename = models.CharField(verbose_name='State Name',max_length=50,null=False,blank=False,default='No Data')
	cityname = models.CharField(verbose_name='City Name',max_length=50,null=False,blank=False,default='No Data')
	statecountry = models.CharField(verbose_name='Country',max_length=30)
	skilled_labour_cost = models.FloatField(default=0.0)
	unskilled_labour_cost = models.FloatField(default=0.0)
	semiskilled_labour_cost = models.FloatField(default=0.0)
	lat = models.FloatField(default=0.0)
	lng = models.FloatField(default=0.0)
	industryType = models.CharField(null=False,blank=False,max_length=60)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.statecode


class City(models.Model):
	cityid = models.AutoField(primary_key=True)
	citycode = models.CharField(null=False,blank=False,max_length=5)
	cityname = models.CharField(verbose_name='City Name',max_length=25)
	citystate = models.ForeignKey(State,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.citycode

class OperationLocation(models.Model):
	oplocationid = models.IntegerField(primary_key=True)
	betterplace_siteid = models.CharField(max_length=50,verbose_name='Site Id',default='No ID')
	betterplace_sitename = models.CharField(max_length=50,verbose_name='Site Name',default='No Data')
	oploccode = models.CharField(unique=True,max_length=7,verbose_name='Location Code')
	oploclat = models.FloatField(verbose_name='Latitude',null=True,blank=True)
	oploclong = models.FloatField(verbose_name='Longitude',null=True,blank=True)
	oplocaddress = models.TextField(verbose_name='Operation Address',max_length=200)
	oploccity = models.ForeignKey(City,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)


	def __str__(self):
		return self.oplocaddress


class Invoice_Header_Location(models.Model):
	locationid = models.AutoField(primary_key=True)
	custname = models.CharField(max_length=50,verbose_name='Location Code')
	loccode = models.CharField(max_length=7,verbose_name='Location Code')
	gstin_no = models.CharField(max_length=15,verbose_name='GSTIN No')
	pan_no = models.CharField(max_length=10,verbose_name='PAN No')
	locaddress = models.TextField(verbose_name='Operation Address',max_length=200)
	locstate = models.ForeignKey(State,on_delete=models.CASCADE)
	loccity = models.ForeignKey(City,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)


	def __str__(self):
		return self.locaddress
