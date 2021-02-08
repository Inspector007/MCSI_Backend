from django.db import models
from datetime import datetime
from location.models import OperationLocation

# Create your models here.

class User(models.Model):
	userid = models.CharField(primary_key=True,max_length=15)
	firstname = models.CharField(verbose_name='First Name',max_length=15,null=True,blank=True)
	lastname = models.CharField(verbose_name='Last Name',max_length=15,null=True,blank=True)
	mobileno = models.CharField(verbose_name='MobileNo.',max_length=10,null=True,blank=True)
	worklocation = models.CharField(verbose_name='worklocation',max_length=20,null=True,blank=True)
	status = models.CharField(max_length=5,null=True,blank=True)
	version = models.CharField(max_length=10,null=True,blank=True)
	password = models.CharField(max_length=15,default='123456')
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.firstname

	# class Meta:
	# 	db_table = 'usertbl'

#User Role data
class Access(models.Model):
	accessid = models.AutoField(primary_key=True)
	accname = models.CharField(verbose_name='role name',max_length=25,null=True,blank=True)
	accdescription = models.CharField(verbose_name='description',max_length=100,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.accname

class UserAccess(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	access = models.ForeignKey(Access,on_delete=models.CASCADE)
	location = models.ForeignKey(OperationLocation,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.access.accname

class Customer(models.Model):
	custid = models.CharField(primary_key=True,max_length=10)
	custcode = models.CharField(verbose_name='customer code',max_length=5,null=True,blank=True)
	custname = models.CharField(max_length=200,null=True,blank=True)
	custcontactname = models.CharField(max_length=30,null=True,blank=True)
	email = models.CharField(max_length=100,null=True,blank=True)
	mobileno = models.CharField(max_length=15,null=True,blank=True)
	status = models.CharField(max_length=50,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.custname


class CustomerMaster(models.Model):
	CUST_CODE = models.CharField(primary_key=True,max_length=10)
	EVENT = models.CharField(verbose_name='event',max_length=3,null=False,blank=False)
	GRP_BP = models.CharField(max_length=4,null=False,blank=False)
	NAME = models.CharField(max_length=35,null=False,blank=False)
	NAME_2 = models.CharField(max_length=35,null=True,blank=True)
	CARE_OF = models.CharField(max_length=40,null=True,blank=True)
	STREET = models.CharField(max_length=60,null=False,blank=False)
	STREET_4 = models.CharField(max_length=40,null=True,blank=True)
	STREET_5 = models.CharField(max_length=40,null=True,blank=True)
	DIST = models.CharField(max_length=40,null=True,blank=True)
	PO_CODE = models.CharField(max_length=10,null=False,blank=False)
	CITY = models.CharField(max_length=10,null=False,blank=False)
	COUNTRY = models.CharField(max_length=3,null=False,blank=False)
	REGION = models.CharField(max_length=3,null=False,blank=False)
	MOB_NO = models.CharField(max_length=12,null=False,blank=False)
	CONTCT_PRSN = models.CharField(max_length=35,null=True,blank=True)
	EMAIL = models.CharField(max_length=150,null=True,blank=True)
	EXTR_BP = models.CharField(max_length=20,null=True,blank=True)
	EXTR_ADRS = models.CharField(max_length=20,null=True,blank=True)
	TAX_CAT = models.CharField(max_length=4,null=True,blank=True)
	TAX_NUM = models.CharField(max_length=60,null=False,blank=False)
	CUST_CLS = models.CharField(max_length=40,null=True,blank=True)
	LUT_NUM = models.CharField(max_length=25,null=True,blank=True)
	LTA_NUM = models.CharField(max_length=25,null=True,blank=True)
	PAN = models.CharField(max_length=40,null=False,blank=False)
	GRP_KEY = models.CharField(max_length=10,null=False,blank=False)
	INDSTRY_CODE = models.CharField(max_length=2,null=True,blank=True)
	CO_CODE = models.CharField(max_length=4,null=False,blank=False)
	INDUSTRY = models.CharField(max_length=65,null=True,blank=True)
	RECON_GL = models.CharField(max_length=10,null=False,blank=False)
	PYMT_TRM = models.CharField(max_length=4,null=True,blank=True)
	NOT_RELSD = models.CharField(max_length=1,null=True,blank=True)
	CUST_BLK = models.CharField(max_length=1,null=True,blank=True)

	def __str__(self):
		return self.CUST_CODE


class InternalOrders(models.Model):
	INTRNL_ORDR = models.CharField(primary_key=True, max_length=12)	
	EVENT = models.CharField(max_length=3,null=True,blank=True)
	CONTRL_AREA = models.CharField(max_length=4,null=False,blank=False)
	ORDR_TYPE = models.CharField(max_length=4,null=True,blank=True)
	INTRNL_ORDR_DESCR = models.CharField(max_length=40,null=False,blank=False)
	CO_CODE = models.CharField(max_length=4,null=False,blank=False)
	PRFT_CNTR = models.CharField(max_length=10,null=False,blank=False)
	PRSN_RESPNSBL = models.CharField(max_length=20,null=True,blank=True)
	HARMONY_IO = models.CharField(max_length=20,null=True,blank=True)
	ACT_ASG = models.CharField(max_length=3,null=False,blank=False)
	CUSTOMER = models.CharField(max_length=18,null=False,blank=False)
	ACVTY = models.CharField(max_length=18,null=False,blank=False)
	CLUSTER = models.CharField(max_length=18,null=False,blank=False)
	BRANCH = models.CharField(max_length=18,null=False,blank=False)
	GROUP_INT = models.CharField(max_length=18,null=False,blank=False)
	TAX_CLASSIFICATION = models.CharField(max_length=18,null=False,blank=False)
	NETWORK_IND = models.CharField(max_length=18,null=False,blank=False)
	OPPORTUNITY_ID = models.CharField(max_length=18,null=False,blank=False)
	SUB_ACVTY = models.CharField(max_length=18,null=False,blank=False)
	SCD_VERTICAL = models.CharField(max_length=18,null=False,blank=False)
	LOCATION = models.CharField(max_length=10,null=True,blank=True)
	STATUS = models.CharField(max_length=4,null=True,blank=True)
	CUST_PAN = models.CharField(max_length=10,null=True,blank=True)
	CUST_GRP = models.CharField(max_length=10,null=True,blank=True)
	ORDR_CTGRY = models.CharField(max_length=2,null=True,blank=True)
	PLANT = models.CharField(max_length=4,null=True,blank=True)
	STATISTICAL = models.CharField(max_length=1,null=True,blank=True)
	COST_CNTR = models.CharField(max_length=10,null=True,blank=True)
	BUSNS_SEGMNT = models.CharField(max_length=18,null=True,blank=True)
	PRM_VERTICAL = models.CharField(max_length=18,null=True,blank=True)
	INDUSTRY = models.CharField(max_length=18,null=True,blank=True)
	GROUP_EXT = models.CharField(max_length=18,null=True,blank=True)
	CUSTOMER_ENTITY = models.CharField(max_length=18,null=True,blank=True)
	CUSTOMER_STATE = models.CharField(max_length=18,null=True,blank=True)
	IDT_OP_SERVICE_CLASS = models.CharField(max_length=18,null=True,blank=True)
	DELVR_ADDRS = models.CharField(max_length=10,null=True,blank=True)
	CREATED_DATE = models.DateTimeField(null=True,blank=True)
	UPDATED_DATE = models.DateTimeField(null=True,blank=True)

	def __str__(self):
		return self.INTRNL_ORDR

class orderdeliveryaddress(models.Model):
	class Meta:
		unique_together = (('INTRNL_ORDR', 'DELVR_ADDRS'),)

	INTRNL_ORDR = models.ForeignKey(InternalOrders,on_delete=models.CASCADE)
	DELVR_ADDRS = models.CharField(max_length=10,null=False,blank=False)
	PRIM_ADDRESS = models.CharField(max_length=1,null=True,blank=True)

	def __str__(self):
		return '{0} - {1}'.format(self.INTRNL_ORDR,self.DELVR_ADDRS)


class BA(models.Model):
	baid = models.CharField(primary_key=True,max_length=10)#
	bttrplce_vendorid = models.CharField(verbose_name='Vendor Id',max_length=60,default = 'no data')#
	bttrplce_vendorname = models.CharField(verbose_name='Vendor Name',max_length=100,default = 'no data')#
	bacode = models.CharField(verbose_name='ba code',max_length=5,null=True,blank=True)
	baname = models.CharField(max_length=150,null=True,blank=True)
	bacontactname = models.CharField(max_length=30,null=True,blank=True)
	email = models.CharField(max_length=100,null=True,blank=True)
	mobileno = models.CharField(max_length=15,null=True,blank=True)
	pancard = models.CharField(max_length=10,null=True,blank=True)
	status = models.CharField(max_length=50,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.baname


class UserLocationCustomer(models.Model):
	ulcpkey = models.AutoField(primary_key=True,max_length=10)
	location = models.ForeignKey(OperationLocation,on_delete=models.CASCADE)
	# customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return str(self.location)

# class UserLocationCustomer(models.Model):
#
