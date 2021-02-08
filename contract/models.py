from django.db import models
from account.models import UserLocationCustomer, Customer, BA
from django.utils import timezone
# Create your models here.
from location.models import State
import datetime



contractwithchoices = ((0,'Customer'),
		(1,'BA'),
		)
kpistatuschoices = ((0,'InActive'),
		(1,'Active'),
		)
skilllevelchoices = ((0,'Skilled'),
		(1,'SemiSkilled'),
		(2,'UnSkilled'),
		)
bonusdurchoices = (('month','Month'),
		('quarter','Quarter'),
		('half','Half'),
		('year','Year'),
		)

targetchoices = (('0','Daily'),
		('1','Monthly'),
		('2','Quaterly'),
		('3','Yearly'),
		)


class ContractType(models.Model):
	contracttypeid = models.IntegerField(primary_key=True)
	cnttypename = models.CharField(max_length=30)
	cnttypecode = models.CharField(max_length=5)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.cnttypecode

class RateType(models.Model):
	ratetypeid = models.IntegerField(primary_key=True)
	ratetypename = models.CharField(max_length=30)
	ratetypecode = models.CharField(max_length=5)
	contracttypeid = models.ForeignKey(ContractType,on_delete=models.CASCADE, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.ratetypecode


class SkillLevel(models.Model):
	skillid = models.AutoField(primary_key=True)
	skillname = models.CharField(max_length=30,null=True,blank=True)
	skillcode = models.CharField(max_length=5,null=True,blank=True)
	contractflag = models.CharField(max_length=5,default=1,null=True,blank=True)
	# skilllevel = models.CharField(max_length=5,choices=skilllevelchoices,default=0,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return ("{0}".format(self.skillname))

class Designation(models.Model):
	designation_id = models.AutoField(primary_key=True)
	designation_name = models.CharField(max_length=30,null=True,blank=True)
	designation_code = models.CharField(max_length=5,null=True,blank=True)
	# skilllevel_fk = models.ForeignKey(SkillLevel,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return ("{0}".format(self.designation_name))


class Contract(models.Model):
	contractid = models.CharField(primary_key=True,max_length=50)
	contractwith = models.CharField(verbose_name='contract with',choices = contractwithchoices,max_length=5) # BA/Customer
	relatedcontract = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True)
	cost = models.FloatField(null=True,blank=True)
	fixedcostrate = models.FloatField(null=True,blank=True)
	oppourtunityid = models.CharField(max_length=20,null=True)
	betterpalcesiteid = models.CharField(max_length=50,null=True,blank=True)
	vertical = models.CharField(null=True,blank=True,max_length=50)
	bonus = models.IntegerField(null=True,blank=True)
	bonusduration = models.CharField(max_length=10,choices=bonusdurchoices,default='month')
	startdate = models.DateField()
	enddate = models.DateField()
	closedate = models.DateField(default=datetime.date(2021,3,31))
	extenddate = models.DateField(default=datetime.date(2021,3,31))
	approvedby = models.CharField(max_length=45,null=True,blank=True)
	approvestatus = models.SmallIntegerField(null=True,blank=True)
	remark = models.CharField(max_length=200,null=True,blank=True)
	contracttype = models.ForeignKey(ContractType,on_delete=models.CASCADE)
	locationcust = models.ForeignKey(UserLocationCustomer,on_delete=models.CASCADE)
	customer = models.ForeignKey(Customer,null=True, blank= True, on_delete=models.CASCADE)
	ba = models.ForeignKey(BA,null=True, blank= True, on_delete=models.CASCADE)
	address1 = models.CharField(max_length=100,null=True) # new
	address2 = models.CharField(max_length=100,null=True) # new
	city = models.CharField(max_length=30,null=True) # new
	servicetype = models.CharField(max_length=100,null=True) # new
	panno = models.CharField(max_length=10,null=True, blank=True) # new
	gstinno = models.CharField(max_length=15,null=True, blank=True) # new
	place_of_supply_city = models.CharField(max_length=30,null=True, blank=True) # new
	place_of_supply_state = models.CharField(max_length=30,null=True, blank=True) # new
	address_of_delivery_city = models.CharField(max_length=30,null=True, blank=True) # new
	address_of_delivery_state = models.CharField(max_length=30,null=True, blank=True) # new
	doclink1 = models.CharField(max_length=500, blank = True, null=True)
	doclink2 = models.CharField(max_length=500, blank = True, null=True)
	doclink3 = models.CharField(max_length=500, blank = True, null=True)
	doclink4 = models.CharField(max_length=500, blank = True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return '{0}-{1}'.format(self.contractid,self.contractwith)

	def save(self,*args,**kwargs):
		from datetime import datetime
		if self.relatedcontract is not None or self.relatedcontract: 
			contractLocation = Contract.objects.get(contractid = self.relatedcontract.contractid)
			self.locationcust = contractLocation.locationcust
		if self.contractwith == 0:
			if self.contractid == '123456':
				self.contractid = '{0}-{1}-{2}-{3}'.format(self.customer.custcode if self.customer.custcode \
					else self.customer.custname[:7].replace(' ','-'),'MLL',\
					str(datetime.now().date()),''.join(str(datetime.now().time()).split('.')[0].split(':')))
		if self.contractwith == 1:
			if self.contractid == '123456':
				if '(' in self.ba.baname[:7]:
					bacode_change = self.ba.baname[:7].replace('(','-')
				self.contractid = '{0}-{1}-{2}-{3}'.format(self.ba.bacode if self.ba.bacode else bacode_change.replace(' ','-'),\
					'MLL' if self.customer is None else self.customer.custcode ,\
					str(datetime.now().date()),''.join(str(datetime.now().time()).split('.')[0].split(':')))
		super().save(*args, **kwargs)

class ContractDetail(models.Model):
	contractdetid = models.AutoField(primary_key=True)
	contract = models.ForeignKey(Contract,on_delete=models.	CASCADE)
	contacttype = models.ForeignKey(ContractType,on_delete=models.CASCADE) # need to be removed
	ratetype = models.ForeignKey(RateType,on_delete=models.CASCADE)
	skilllevel = models.ForeignKey(SkillLevel,on_delete=models.CASCADE)
	designation = models.ForeignKey(Designation,on_delete=models.CASCADE,default=None)
	requirequantity = models.IntegerField(null=True,blank=True)
	startquantity = models.IntegerField(null=True,blank=True)
	endquantity = models.IntegerField(null=True,blank=True)
	uom = models.CharField(null=True,blank=True,max_length=20)
	upperdev = models.FloatField(null=True,blank=True)
	lowerdev = models.FloatField(null=True,blank=True)
	fixedcost = models.FloatField(null=True,blank=True)
	ot = models.FloatField(null=True,blank=True,default=0.0)
	adhoc = models.FloatField(null=True,blank=True,default=0.0)
	margintype = models.CharField(max_length=5,null=True,blank=True)
	marginvalue = models.FloatField(null=True,blank=True)
	isapplicablecomrange = models.SmallIntegerField(null=True,blank=True)
	billingcycle = models.CharField(max_length=50,null=True,blank=True)
	finalsubmissionflag = models.SmallIntegerField(null=True,blank=True)
	aadhaar_data = models.TextField(null=True,blank=True)
	remark = models.CharField(max_length=200,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return str(self.contractdetid)


from encrypted_model_fields.fields import EncryptedCharField
class ContractDetail_Reference_Aadharid(models.Model):
	contractdetailid_fk = models.ForeignKey(ContractDetail,on_delete=models.CASCADE,default=None)
	aadhaarid = EncryptedCharField(max_length=3)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	class Meta:
		managed = True
		db_table = 'contractdetail_aadhaar'

	def __str__(self):
		return str(self.aadhaarid)


class AdditionalContractField(models.Model):
	contractaddfieldid = models.AutoField(primary_key=True)
	contract = models.ForeignKey(Contract,on_delete=models.	CASCADE)
	description = models.CharField(max_length=200,null=True,blank=True)
	cost = models.FloatField(null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return str(self.contractaddfieldid)

class Contract_Percentage_Field(models.Model):
	contract_per_loc_id = models.AutoField(primary_key=True)
	contract = models.ForeignKey(Contract,on_delete=models.	CASCADE)
	state = models.CharField(max_length=200,null=True,blank=True)
	city = models.CharField(max_length=200,null=True,blank=True)
	percentage = models.FloatField(null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return str(self.contract_per_loc_id)


class DetailAttCapture(models.Model):
	contractid = models.ForeignKey(Contract,on_delete=models.CASCADE)
	date = models.DateField(default='1900-01-01')
	skillid = models.ForeignKey(SkillLevel,on_delete=models.CASCADE)
	designation = models.ForeignKey(Designation,on_delete=models.CASCADE,default=None)
	skillcount = models.IntegerField(null=True,blank=True)
	skillotcount = models.IntegerField(null=True,blank=True)
	extrashift = models.IntegerField(null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return 'contractid-{0} skillid-{1}'.format(self.contractid,self.skillid)

class Vertical(models.Model):
	verticalCode = models.CharField(primary_key=True,max_length=3)
	verticalName = models.CharField(max_length=50,null=True,blank=True)
	verticalShortName = models.CharField(max_length=20,null=True,blank=True)
	# created = models.DateTimeField(auto_now_add=True)
	# createdby = models.CharField(max_length=20)
	# updated = models.DateTimeField(auto_now=True)
	# updatedby = models.CharField(max_length=20)


	def __str__(self):
		return '{0}-{1}'.format(self.verticalCode,self.verticalName)

class InvoiceUtility(models.Model):
	contractid = models.ForeignKey(Contract,on_delete=models.CASCADE)
	contractTypeName = models.CharField(max_length=50,blank=False,null=False)
	oppourtunityId = models.CharField(max_length=50,blank=False,null=False)
	location = models.CharField(max_length=50,blank=True,null=True)
	invoiceStatrtDate = models.DateField()
	invoiceEndDate = models.DateField()
	invoiceGenrationDate = models.DateField()
	status = models.CharField(max_length=2)
	grandTotal = models.FloatField()
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)


	def __str__(self):
		return '{0} -- {1} -- {2}'.format(self.contractid, self.invoiceGenrationDate, self.contractTypeName) 

	def save(self,*args,**kwargs):
		if self.invoiceStatrtDate > self.invoiceEndDate:
			return {'msg': 'startdate should be less than enddate'}
		super().save(*args,**kwargs)


class InvoiceDetailCapture(models.Model):
	contractid = models.ForeignKey(Contract,on_delete=models.CASCADE)
	contractTypeName = models.CharField(max_length=50,blank=False,null=False)
	oppourtunityId = models.CharField(max_length=50,blank=False,null=False)
	location = models.CharField(max_length=50,blank=True,null=True)
	invoiceDate = models.DateField()
	skillName = models.CharField(max_length=50,blank=False,null=False)
	designation = models.CharField(max_length=50,blank=False,null=False)
	attendenceCount = models.IntegerField()
	cost = models.FloatField()
	totalcost = models.FloatField()
	status = models.CharField(max_length=2)
	rowInvoiceFlag = models.CharField(max_length=2)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)


	def __str__(self):
		return '{0} -- {1} -- {2}'.format(self.contractid, self.invoiceDate, self.contractTypeName) 


class InvoiceMaster(models.Model):
	invoiceid = models.CharField(primary_key=True,max_length=50)
	contractid = models.ForeignKey(Contract,on_delete=models.CASCADE)
	finaltotal = models.FloatField(default = 0.0)
	selectedrowids = models.CharField(max_length=300,blank=True,null=True)
	state = models.CharField(max_length=70,blank=True,null=True)
	city = models.CharField(max_length=70,blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)
	def __str__(self):
		return '{0}-{1}'.format(self.invoiceid,self.contractid)

	# def save(self,*args,**kwargs):
	# 	from datetime import datetime
		
	# 	# if self.invoiceid == '123456':
	# 	# 	self.invoiceid = '{0}-{1}-{2}'.format('invoice','MLL',\
	# 	# 		str(datetime.now().date()),''.join(str(datetime.now().time()).split('.')[0].split(':')))
	# 	import pdb;pdb.set_trace();


	# 	con_per_field_objs = Contract_Percentage_Field.objects.filter(contract = self.contractid)
	# 	rowidslist = self.selectedrowids.split('-')
	# 	for i in rowidslist:
	# 		try:
	# 			inv_det_capt_obj = InvoiceDetailCapture.objects.get(id = i)
	# 			inv_det_capt_obj.rowInvoiceFlag = 1
	# 			inv_det_capt_obj.save()
	# 		except:
	# 			pass
	# 	if con_per_field_objs.count() > 0:
	# 		for con_per_field_obj in con_per_field_objs:
	# 			invoice_master_obj_new = InvoiceMaster()
	# 			invoice_master_obj_new.invoiceid = self.invoiceid+str("_{0}_{1}".format(con_per_field_obj.city,con_per_field_obj.state))
	# 			invoice_master_obj_new.contractid = self.contractid
	# 			invoice_master_obj_new.finaltotal = (self.finaltotal * con_per_field_obj.percentage) / 100
	# 			invoice_master_obj_new.state = con_per_field_obj.state
	# 			invoice_master_obj_new.city = con_per_field_obj.city
	# 			invoice_master_obj_new.selectedrowids = self.selectedrowids
	# 			invoice_master_obj_new.save()				
	# 	else:				
	# 		super().save(*args, **kwargs)


class AdditionalCharges(models.Model):
	invoiceid = models.ForeignKey(InvoiceMaster,on_delete=models.CASCADE)
	headerName = models.CharField(max_length=30,blank=False,null=False)
	additionalCost = models.FloatField(default = 0.0)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)
	
	def __str__(self):
		return '{0}-{1}'.format(self.invoiceid,self.header_name)


class InvoiceHeaderMaster(models.Model):
	stateid = models.ForeignKey(State,on_delete=models.CASCADE)
	address = models.CharField(max_length=300,blank=False,null=False)
	gst = models.CharField(max_length=30,blank=False,null=False)
	cin = models.CharField(max_length=30,blank=False,null=False)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)
	
	def __str__(self):
		return '{0}-{1}'.format(self.stateid,self.address)


class KPICategory(models.Model):
	kpicatCode = models.CharField(primary_key=True,max_length=20,blank=False, null=False)	
	kpicatName = models.CharField(max_length=30,blank=False, null=False)	
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.kpicatName


class KPI(models.Model):
	kpiCode = models.CharField(primary_key=True,max_length=20,blank=False, null=False)	
	kpiName = models.CharField(max_length=30,blank=False, null=False)	
	category = models.ForeignKey(KPICategory,on_delete=models.CASCADE, null=True)
	status = models.CharField(max_length=20,choices=kpistatuschoices,default=1, blank=True,null=True)
	description = models.CharField(max_length=100,blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)
	
	def __str__(self):
		return self.kpiCode


class KPIFrequency(models.Model):
	kpifreqid = models.AutoField(primary_key=True)
	contract = models.ForeignKey(Contract,on_delete=models.CASCADE)
	kpi = models.ForeignKey(KPI,on_delete=models.CASCADE)
	inputfrequency = models.CharField(max_length=30,blank=False,null=False)
	outputfrequency = models.CharField(max_length=30,blank=False,null=False)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.kpi.kpiName


class KPIDetail(models.Model):
	kpidetid = models.AutoField(primary_key=True)
	contract = models.ForeignKey(Contract,on_delete=models.CASCADE)
	kpi = models.ForeignKey(KPI,on_delete=models.CASCADE)
	uom = models.CharField(max_length=30,blank=False,null=False)
	targetdate = models.DateField(default=timezone.now)
	target1 = models.FloatField(blank=False,null=False)
	typeoftarget = models.CharField(max_length=30,choices=targetchoices,null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.kpi.kpiName


class Capture_Daily_KPI(models.Model):
	contractid = models.ForeignKey(Contract,on_delete=models.CASCADE)
	date = models.DateField()
	kpiid = models.ForeignKey(KPI,on_delete=models.CASCADE)
	actualcount = models.IntegerField(null=True,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.actualcount


class Document(models.Model):
	# contractid = models.ForeignKey(Contract,unique=True,on_delete=models.CASCADE)
	contractid = models.OneToOneField(Contract,on_delete=models.CASCADE)
	description = models.CharField(max_length=255, blank=True)
	document = models.FileField(upload_to='documents/')
	document1 = models.FileField(upload_to='documents/',null=True,blank=True)
	document2 = models.FileField(upload_to='documents/',null=True,blank=True)
	uploaded_at = models.DateTimeField(auto_now_add=True)
	created = models.DateTimeField(auto_now_add=True)
	createdby = models.CharField(max_length=20)
	updated = models.DateTimeField(auto_now=True)
	updatedby = models.CharField(max_length=20)

	def __str__(self):
		return self.description
