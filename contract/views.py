from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, serializers
import calendar
from datetime import datetime

from iscm.utility import find_user_locationlist
from .models import Document,ContractType,RateType,SkillLevel,Designation,\
	Contract,ContractDetail,DetailAttCapture,Vertical,\
	KPICategory,KPI,KPIFrequency,KPIDetail,Capture_Daily_KPI,\
	InvoiceMaster,AdditionalCharges,InvoiceHeaderMaster, AdditionalContractField, \
	Contract_Percentage_Field, InvoiceDetailCapture
from . serializers import ContractTypeSerializers,RateTypeSerializers,SkillLevelSerializers,\
		DesignationSerializer, ContractSerializers, ContractDetailSerializers,\
		DocumentSerializers,DetailAttCaptureSerializers,VerticalSerializers,\
		KPICategorySerializer,KPISerializer,KPIFrequencySerializer,KPIDetailSerializer,\
		Capture_Daily_KPISerializer,InvoiceMasterSerializer,AdditionalChargesSerializer,\
		InvoiceHeaderMasterSerializer, AdditionalContractFieldSerializers, Contract_Percentage_FieldSerializers
from .forms import DocumentForm

from datetime import datetime,timedelta
# Create your views here.


def call_screen_msg():
	print("hey I am here")

def call_screen_msg1():
	print("hey I am here 2")


class ContractTypeView(viewsets.ModelViewSet):
	"""
		Get contract type like manpower, Fixed price, o/p based pricing
		Perform Add, Update, Delete operation
	"""
	queryset = ContractType.objects.all()
	serializer_class = ContractTypeSerializers
	filter_backends = (filters.SearchFilter,)
	search_fields = ('cnttypename', 'cnttypecode')

	def create(self, request, format=None):
		serializer = ContractTypeSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class RateTypeView(viewsets.ModelViewSet):
	"""
		Get Rate
		Perform Add, Update, Delete operation
	"""
	queryset = RateType.objects.all()
	serializer_class = RateTypeSerializers

	def create(self, request, format=None):
		serializer = RateTypeSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)




	def getratetypeDetail(self, request, *args, **kwargs):
		"""
		Get ratetype detail using contracttypeid
		"""
		chkcontracttype = self.kwargs['contracttypeid']
		ratettype_detail = RateType.objects.filter(contracttypeid = chkcontracttype)
		serializer = RateTypeSerializers(ratettype_detail, many=True)
		return Response(serializer.data)


class SkillLevelView(viewsets.ModelViewSet):
	"""
		Get skill level
		Perform Add, Update, Delete operation
	"""
	queryset = SkillLevel.objects.all()
	serializer_class = SkillLevelSerializers

	def create(self, request, format=None):
		serializer = SkillLevelSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


	def getskilllevelDetail(self, request, *args, **kwargs):
		"""
		Get Skill level using contractid with contract detail
		"""
		getcontractdetail = self.kwargs['contractid']
		contract_detail = ContractDetail.objects.filter(contract = getcontractdetail).values_list('skilllevel')
		filter_skilllevel = SkillLevel.objects.filter(skillid__in = contract_detail)
		serializer = SkillLevelSerializers(filter_skilllevel, many=True)
		return Response(serializer.data)


class DesignationView(viewsets.ModelViewSet):
	"""
		Get skill level
		Perform Add, Update, Delete operation
	"""
	queryset = Designation.objects.all()
	serializer_class = DesignationSerializer

	def create(self, request, format=None):
		serializer = DesignationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class ContractView(viewsets.ModelViewSet):
	"""
		Get Contract
		Perform Add, Update, Delete operation
	"""
	# permission_classes = (permissions.IsAuthenticated, )
	# permission_classes = (permissions.AllowAny, )


	queryset = Contract.objects.all()
	serializer_class = ContractSerializers

	# permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


	def create(self, request, format=None):
		serializer = ContractSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)



	def allContractCount(self, request):
		"""
		Gives All contract count in string format
		"""

		contract_count = Contract.objects.all().count()
		return Response(str(contract_count))

	def activeContractCount(self, request, *args, **kwargs):
		"""
		Gives Active contract count in string format
		"""
		act_contract_count = Contract.objects.filter(startdate__lt =\
		 datetime.today().date(), enddate__gt = \
		 datetime.today().date()).count()
		return Response(str(act_contract_count))

	def closeContractCount(self, request, *args, **kwargs):
		"""
		Gives closed contract count in string format
		"""
		close_contract_count = Contract.objects.filter(closedate__lt =\
		 datetime.today().date()).count()
		return Response(str(close_contract_count))


	def allCustomerContractCount(self, request):
		"""
		Gives All customer contract count in string format
		"""

		contract_count = Contract.objects.filter(contractwith = '0').count()
		return Response(str(contract_count))

	def activeCustomerContractCount(self, request, *args, **kwargs):
		"""
		Gives Active customer contract count in string format
		"""
		act_contract_count = Contract.objects.filter(contractwith = '0',startdate__lt =\
		 datetime.today().date(), enddate__gt = \
		 datetime.today().date()).count()
		return Response(str(act_contract_count))

	def closeCustomerContractCount(self, request, *args, **kwargs):
		"""
		Gives closed customer contract count in string format
		"""
		close_contract_count = Contract.objects.filter(contractwith = '0',enddate__lt = \
				datetime.today().date()).count()
		return Response(str(close_contract_count))

	def allBAContractCount(self, request):
		"""
		Gives All ba contract count in string format
		"""

		print('rolename aaya- {0} -- '.format(request.META['QUERY_STRING']))

		contract_count = Contract.objects.filter(contractwith = '1').count()
		return Response(str(contract_count))

	def activeBAContractCount(self, request, *args, **kwargs):
		"""
		Gives Active ba contract count in string format
		"""
		act_contract_count = Contract.objects.filter(contractwith = '1',startdate__lt =\
		 datetime.today().date(), enddate__gt = \
		 datetime.today().date()).count()
		return Response(str(act_contract_count))

	def closeBAContractCount(self, request, *args, **kwargs):
		"""
		Gives closed ba contract count in string format
		"""
		close_contract_count = Contract.objects.filter(contractwith = '1',enddate__lt = \
				datetime.today().date()).count()
		return Response(str(close_contract_count))


	def activeContract(self, request, *args, **kwargs):
		"""
		Gives active contract details
		"""
		act_contract = Contract.objects.filter(startdate__lt =\
		 datetime.today().date(), enddate__gt = \
		 datetime.today().date())
		serializer = ContractSerializers(act_contract, many=True)
		return Response(serializer.data)

	def closeContract(self, request, *args, **kwargs):
		"""
		Gives closed contract details
		"""
		close_contract = Contract.objects.filter(closedate__lt =\
		 datetime.today().date())
		serializer = ContractSerializers(close_contract, many=True)
		return Response(serializer.data)

	def customerbaContract(self, request, *args, **kwargs):
		"""
		Pass checkbacust parameter with 0(Customer) or 1(BA) value
		It will return contract as per parameter value
		"""
		chkbacust = self.kwargs['checkbacust']
		custba_contract = Contract.objects.filter(contractwith = chkbacust)
		serializer = ContractSerializers(custba_contract, many=True)
		return Response(serializer.data)

	def contractfilter(self, request, *args, **kwargs):
		"""
		Pass all parameter values in number format
		like contractwith is 0 or 1, 0 is customer and 1 is BA
		status # active - 1 , expired - 2, expiring in 90 days - 3
		location will pass as number format
		"""
		# import pdb;pdb.set_trace()
		userid = request.META['QUERY_STRING']#.split('-')[1].strip(' 	')
		print('rolename aaya- {0} -- userid {1}'.format(request.META['QUERY_STRING'],userid))
		locationlist = find_user_locationlist()

		chkbacust = self.kwargs['contractwith']
		checkflag = int(self.kwargs['status'])
		location = self.kwargs['location']
		opportunityid = self.kwargs['oppid']
		contractid = self.kwargs['contractid']
		# import pdb;pdb.set_trace()
		custba_contract = Contract.objects.filter(contractwith = chkbacust, locationcust__in = locationlist).order_by('-created')
		if (opportunityid == None or opportunityid == '0000000000') and (contractid == None or contractid == '0000000000'):
			custba_contract = Contract.objects.filter(contractwith = chkbacust, locationcust__in = locationlist).order_by('-created')
		elif contractid != None or contractid != '0000000000':
			custba_contract = Contract.objects.filter(contractwith = chkbacust, contractid = contractid, locationcust__in = locationlist).order_by('-created')
		elif opportunityid != None or opportunityid != '0000000000':
			custba_contract = Contract.objects.filter(contractwith = chkbacust, oppourtunityid = opportunityid, locationcust__in = locationlist).order_by('-updated')
		# elif (opportunityid != None or opportunityid != '0000000000') and (contractid != None or contractid != '000000000'):
		# 	custba_contract = Contract.objects.filter(contractwith = chkbacust, contractid = contractid, oppourtunityid = opportunityid, locationcust__in = locationlist)
		# elif (opportunityid != None or opportunityid != '0000000000') and (contractid == None or contractid == '000000000'):
		# 	custba_contract = Contract.objects.filter(contractwith = chkbacust, oppourtunityid = opportunityid, locationcust__in = locationlist)
		else:
			custba_contract = Contract.objects.filter(contractwith = chkbacust, locationcust__in = locationlist).order_by('-created')

		if checkflag == 1: #active
			ctrctflt = custba_contract.filter(startdate__lt =\
				datetime.today().date(), enddate__gt = \
				datetime.today().date()).order_by('-created')
		elif checkflag == 2: #expired
			ctrctflt = custba_contract.filter(enddate__lt = \
				datetime.today().date()).order_by('-created')
		elif checkflag == 3: #expiring in 90 days
			ctrctflt = custba_contract.filter(enddate__gt = \
				datetime.today().date(),enddate__lt = \
				datetime.today().date() + timedelta(days = 90)).order_by('-created')
		else:
			ctrctflt = custba_contract

		if location == '0' or location == None or location == '':
			serializer = ContractSerializers(ctrctflt, many=True)
		else:
			contractfilter = ctrctflt.filter(locationcust = location)
			serializer = ContractSerializers(contractfilter, many=True)

		return Response(serializer.data)

	def getoppourtunitydataNew(self,request,*args,**kwargs):
		import json
		import os
		path = os.path.abspath(__file__).split('views.py')[0]
		with open(path+'rfpapi.json') as json_file:
			data = json.load(json_file)
		opportunity_dict = data[0]['OpportunityList']
		opportunityid = self.kwargs['oppid']
		opp_new_dict = {oppdata['OPP_ID']:oppdata for oppdata in opportunity_dict}
		if opportunityid in opp_new_dict.keys():
			opportunity_data = opp_new_dict[opportunityid]
			return Response({'custname':opportunity_data['ACC_NAME'],\
				'vertical':opportunity_data['VERTICAL_NAME'],'remark':opportunity_data['OPP_DESC']})
		else:
			return Response({'error':'Invalid opportunityid'})

	def getoppourtunitydata(self,request,*args,**kwargs):
		import json
		# import os
		from iscm.settings import strOpplink
		import urllib.request
		opportunityid = self.kwargs['oppid']

		strOpplink = strOpplink
		if strOpplink == "http://103.81.89.7/cashAPI/api/APIOpportunityDetails?Opp_id={0}&ApiKey=superapi00000":
			opportunity_dict = urllib.request.urlopen(strOpplink.format(opportunityid)).read()
			opportunity_dict = str(opportunity_dict,'utf-8')
		else:
			opportunity_dict = urllib.request.urlopen(strOpplink.format(opportunityid)).read()
			opportunity_dict = str(opportunity_dict,'utf-8')

		# import pdb;pdb.set_trace()
		opportunityjson = json.loads(opportunity_dict)
		opportunitydata = opportunityjson['data']
		if opportunityjson['status'] == 'S' and opportunityjson['error'] == '':
			return Response({'custname':opportunitydata['Customer_name'],\
				'vertical':opportunitydata['VERTICAL_NAME'],\
				'Address1':opportunitydata['Address1'],\
				'Address2':opportunitydata['Address2'],\
				'city_name':opportunitydata['City_Name'],\
				'remark':opportunitydata['Opp_Description']})
		else:
			return Response({'error':'Invalid opportunityid'})

	def productattactivecount(self,request,*args,**kwargs):
		"""this function gives the
			count of active BA."""
		bacontract = Contract.objects.filter(contractwith = '1', relatedcontract__isnull=False)
		bacontractcount = bacontract.count()
		attdetailobject = DetailAttCapture.objects.filter(\
			contractid__in = bacontract).values_list('contractid', flat=True)
		attdetailobjectcount = len(set(attdetailobject))
		return Response(str(attdetailobjectcount))

	def productattpendingcount(self,request,*args,**kwargs):
		"""this function gives the
			count of those BA which has no
			record in Detailattcapture table"""
		bacontract = Contract.objects.filter(contractwith = '1', relatedcontract__isnull=False)
		bacontractcount = bacontract.count()
		attdetailobject = DetailAttCapture.objects.filter(\
			contractid__in = bacontract).values_list('contractid', flat=True)
		attdetailobjectcount = len(set(attdetailobject))
		return Response(str(bacontractcount - attdetailobjectcount))

		#'BA3-MLL-2019-05-0309'  BA3-MLL-2019-05-0605' 01-04-2019' '31-04-2019'
	def invoicegeneration(self, request, *args, **kwargs):

		# import pdb;pdb.set_trace()
		from contract.models import InvoiceUtility
		contractid = self.kwargs['contractid']
		# contractid = 'BA3-MLL-2019-05-0605'
		invoice_st_date = str(datetime.today().date().replace(day=1)) #self.kwargs['startdate']
		invoice_end_date = str(datetime.today().date()) #self.kwargs['enddate']
		contract_obj = Contract.objects.get(contractid = contractid)
		contract_det_objs = ContractDetail.objects.filter(contract = contract_obj)
		contract_att_objs = DetailAttCapture.objects.filter(contractid = contract_obj,\
		 date__gte = invoice_st_date,date__lte= invoice_end_date).order_by('date')
		invoice_dict = {}
		grand_total = 0.0
		if contract_obj.contracttype.cnttypecode == 'MNP':
			invoice_list, grand_total = manpowerinvoicefun(contract_det_objs, contract_att_objs)
		elif contract_obj.contracttype.cnttypecode == 'FXP':
			invoice_list, grand_total = fixedrateinvoicefun(contract_det_objs, contract_att_objs)
		elif contract_obj.contracttype.cnttypecode == 'OBPR':
			invoice_list, grand_total = outputbasedinvoicefun(contract_det_objs, contract_att_objs)
		else:
			pass
		invoice_dict['contractid'] = contractid
		invoice_dict['contracttype'] = contract_obj.contracttype.cnttypename
		invoice_dict['opportunityid'] = contract_obj.oppourtunityid
		invoice_dict['location'] = contract_obj.locationcust.location.oplocaddress
		invoice_dict['invoicestartdate'] = invoice_st_date
		invoice_dict['invoiceenddate'] = invoice_end_date
		invoice_dict['invoicegenrationdate'] = datetime.today().date()
		invoice_dict['invoicelist'] = invoice_list
		invoice_dict['grand_total'] = str(grand_total)

		invoice_obj_dict = {}
		# import pdb;pdb.set_trace()
		invoice_st_date_frmt = datetime.strptime(invoice_st_date,'%Y-%m-%d').date()
		invoice_end_date_frmt = datetime.strptime(invoice_end_date,'%Y-%m-%d').date()
		invoice_obj_dict['contractid'] = contract_obj
		invoice_obj_dict['contractTypeName'] = invoice_dict['contracttype']
		invoice_obj_dict['location'] = invoice_dict['location']
		invoice_obj_dict['oppourtunityId'] = invoice_dict['opportunityid']
		invoice_obj_dict['invoiceStatrtDate'] = invoice_st_date
		invoice_obj_dict['invoiceEndDate'] = invoice_end_date
		invoice_obj_dict['invoiceGenrationDate'] = invoice_dict['invoicegenrationdate']
		invoice_obj_dict['status'] = 0
		invoice_obj_dict['grandTotal'] = invoice_dict['grand_total']

		# import pdb;pdb.set_trace()
		print(InvoiceUtility.objects.filter(contractid = contract_obj.contractid, location = invoice_dict['location'],\
			invoiceStatrtDate__gte = invoice_st_date_frmt, invoiceEndDate__lte = invoice_end_date_frmt).count())

		if InvoiceUtility.objects.filter(contractid = contract_obj.contractid, location = invoice_dict['location'],\
			invoiceStatrtDate__gte = invoice_st_date_frmt, invoiceEndDate__lte = invoice_end_date_frmt).count() == 0:
			InvoiceUtility(**invoice_obj_dict).save()
		else:
			pass
		print(invoice_dict)

		return Response(invoice_dict)

	def invoicegenerationwithdate(self, request, *args, **kwargs):
		"""
		Get Filtered invoice as per given date range
		Date Should be in yyyy-mm-dd format
		"""
		# import pdb;pdb.set_trace()
		from contract.models import InvoiceUtility,InvoiceDetailCapture
		contractid = self.kwargs['contractid']
		# contractid = 'BA3-MLL-2019-05-0605'
		invoice_st_date = self.kwargs['invoice_start_date']
		invoice_end_date = self.kwargs['invoice_end_date']
		contract_obj = Contract.objects.get(contractid = contractid)
		contract_det_objs = ContractDetail.objects.filter(contract = contract_obj)
		contract_att_objs = DetailAttCapture.objects.filter(contractid = contract_obj,\
		 date__gte = invoice_st_date,date__lte= invoice_end_date).order_by('date')
		invoice_dict = {}
		grand_total = 0.0
		if contract_obj.contracttype.cnttypecode == 'MNP':
			invoice_list, grand_total = manpowerinvoicefun(contract_det_objs, contract_att_objs)
		elif contract_obj.contracttype.cnttypecode == 'FXP':
			invoice_list, grand_total = fixedrateinvoicefun(contract_det_objs, contract_att_objs)
		elif contract_obj.contracttype.cnttypecode == 'OBPR':
			invoice_list, grand_total = outputbasedinvoicefun(contract_det_objs, contract_att_objs)
		else:
			pass
		invoice_dict['contractid'] = contractid
		invoice_dict['contracttype'] = contract_obj.contracttype.cnttypename
		invoice_dict['opportunityid'] = contract_obj.oppourtunityid
		invoice_dict['location'] = contract_obj.locationcust.location.oplocaddress
		invoice_dict['invoicestartdate'] = invoice_st_date
		invoice_dict['invoiceenddate'] = invoice_end_date
		invoice_dict['invoicegenrationdate'] = datetime.today().date()
		invoice_dict['invoicelist'] = invoice_list
		invoice_dict['grand_total'] = str(grand_total)

		invoice_obj_dict = {}
		new_invoice_list = []
		# import pdb;pdb.set_trace()

		for invoice_entry in invoice_list:
			invoice_obj_dict['contractid'] = contract_obj
			invoice_obj_dict['contractTypeName'] = invoice_dict['contracttype']
			invoice_obj_dict['oppourtunityId'] = invoice_dict['opportunityid']
			invoice_obj_dict['location'] = invoice_dict['location']
			invoice_obj_dict['invoiceDate'] = invoice_entry['date']
			invoice_obj_dict['skillName'] = invoice_entry['skillname']
			invoice_obj_dict['designation'] = invoice_entry['designation']
			invoice_obj_dict['attendenceCount'] = invoice_entry['skillcount']
			invoice_obj_dict['cost'] = invoice_entry['fixedcost']
			invoice_obj_dict['totalcost'] = invoice_entry['total']
			invoice_obj_dict['rowInvoiceFlag'] = 0
			invoice_obj_dict['status'] = 0

		# import pdb;pdb.set_trace()
		# print(InvoiceUtility.objects.filter(contractid = contract_obj.contractid, location = invoice_dict['location'],\
		# 	invoiceStatrtDate__gte = invoice_st_date_frmt, invoiceEndDate__lte = invoice_end_date_frmt).count())

		# if InvoiceUtility.objects.filter(contractid = contract_obj.contractid, location = invoice_dict['location'],\
		# 	invoiceStatrtDate__gte = invoice_st_date_frmt, invoiceEndDate__lte = invoice_end_date_frmt).count() == 0:
		# 	InvoiceUtility(**invoice_obj_dict).save()

		# import pdb;pdb.set_trace()
			# print(InvoiceDetailCapture.objects.filter(contractid = contract_obj.contractid, location = invoice_dict['location'],))
			# import pdb;pdb.set_trace()
			try:
				print(InvoiceDetailCapture.objects.get(contractid = contract_obj.contractid, location = invoice_dict['location'],\
				invoiceDate = invoice_entry['date'], skillName = invoice_entry['skillname'],\
				 designation = invoice_entry['designation']))
				invoice_det_capt = InvoiceDetailCapture.objects.get(contractid = contract_obj.contractid, location = invoice_dict['location'],\
				invoiceDate = invoice_entry['date'], skillName = invoice_entry['skillname'],\
				 designation = invoice_entry['designation'])
				print("try")
				# import pdb;pdb.set_trace()
				invoice_det_capt.attendenceCount = invoice_entry['skillcount']
				invoice_det_capt.cost = invoice_entry['fixedcost']
				invoice_det_capt.totalcost = invoice_entry['total']
				# invoice_det_capt.rowInvoiceFlag = 0
				if invoice_det_capt.attendenceCount == None:
					invoice_det_capt.attendenceCount = 0
				invoice_det_capt.save()
				print(invoice_det_capt.id)
				invoice_entry['id'] = invoice_det_capt.id
				invoice_entry['flag'] = invoice_det_capt.rowInvoiceFlag
				new_invoice_list.append(invoice_entry)

			except Exception as e:
				print(e)
				new_invoice_capt_obj = InvoiceDetailCapture(**invoice_obj_dict)
				new_invoice_capt_obj.save()
				id_new = new_invoice_capt_obj.id
				print(id_new)
				invoice_entry['id'] = id_new
				invoice_entry['flag'] = 0
				new_invoice_list.append(invoice_entry)

			# if InvoiceDetailCapture.objects.filter(contractid = contract_obj.contractid, location = invoice_dict['location'],\
			# 	invoiceDate = invoice_entry['date'], skillName = invoice_entry['skillname'],\
			# 	 designation = invoice_entry['designation']).count == 0:
			# 	InvoiceDetailCapture(**invoice_obj_dict).save()
			# else:
			# 	invoice_det_capt = InvoiceDetailCapture.objects.get(contractid = contract_obj.contractid, location = invoice_dict['location'],\
			# 	invoiceDate = invoice_entry['date'], skillName = invoice_entry['skillname'],\
			# 	 designation = invoice_entry['designation'])
			# 	invoice_det_capt.delete()
			# 	InvoiceDetailCapture(**invoice_obj_dict).save()

		invoice_dict['invoicelist'] = new_invoice_list

		print(invoice_dict)

		return Response(invoice_dict)


	def consolidatedinvoicegenerationwithdate(self, request, *args, **kwargs):
		"""
		Get Filtered invoice as per given date range
		Date Should be in yyyy-mm-dd format
		"""
		# import pdb;pdb.set_trace()
		from contract.models import InvoiceUtility
		contractid = self.kwargs['contractid']
		# contractid = 'BA3-MLL-2019-05-0605'
		invoice_st_date = self.kwargs['invoice_start_date']
		invoice_end_date = self.kwargs['invoice_end_date']

		consolidatCustomerbainvoicelist = []

		customerinvoicedetail = customerBAinvoicing(contractid,invoice_st_date,invoice_end_date)
		customerinvoicedetail['customer'] = 'yes'
		consolidatCustomerbainvoicelist.append(customerinvoicedetail)
		get_ba_detail = Contract.objects.filter(relatedcontract = contractid)
		list_of_ba = get_ba_detail.values_list('contractid')
		bacount = len(list_of_ba)
		count = 0
		if len(list_of_ba) > 0:
			for ba in list_of_ba:
				customerinvoicedetail = None
				customerinvoicedetail = customerBAinvoicing(ba[0],invoice_st_date,invoice_end_date)
				customerinvoicedetail['customer'] = 'no'
				consolidatCustomerbainvoicelist.append(customerinvoicedetail)

		return Response(consolidatCustomerbainvoicelist)


def customerBAinvoicing(contractid,invoice_st_date,invoice_end_date):

	contract_obj = Contract.objects.get(contractid = contractid)
	contract_det_objs = ContractDetail.objects.filter(contract = contract_obj)
	contract_att_objs = DetailAttCapture.objects.filter(contractid = contract_obj,\
	 date__gte = invoice_st_date,date__lte= invoice_end_date).order_by('date')
	invoice_dict = {}
	grand_total = 0.0

	if contract_obj.contracttype.cnttypecode == 'MNP':
		invoice_list, grand_total = manpowerinvoicefun(contract_det_objs, contract_att_objs)
	elif contract_obj.contracttype.cnttypecode == 'FXP':
		invoice_list, grand_total = fixedrateinvoicefun(contract_det_objs, contract_att_objs)
	elif contract_obj.contracttype.cnttypecode == 'OBPR':
		invoice_list, grand_total = outputbasedinvoicefun(contract_det_objs, contract_att_objs)
	else:
		pass
	invoice_dict['contractid'] = contractid
	invoice_dict['contracttype'] = contract_obj.contracttype.cnttypename
	invoice_dict['opportunityid'] = contract_obj.oppourtunityid
	invoice_dict['location'] = contract_obj.locationcust.location.oplocaddress
	invoice_dict['invoicestartdate'] = invoice_st_date
	invoice_dict['invoiceenddate'] = invoice_end_date
	invoice_dict['invoicegenrationdate'] = datetime.today().date()
	invoice_dict['invoicelist'] = invoice_list
	invoice_dict['grand_total'] = str(grand_total)

	print(invoice_dict)

	return invoice_dict


def manpowerinvoicefunaggregate(det_objs, att_objs):
	invoice_list = []
	grand_total = 0.0

	for att in att_objs:
		# print('{0} -- {1} -- {2} -- {3}'.format(att.date,att.skillid.skillname,att.skillcount,att.skillotcount))
		try:
			det_obj = det_objs.get(skilllevel = att.skillid, designation = att.designation)
			# print('Cost is - {0} -- {1} -- {2}'.format(det_obj.fixedcost, (det_obj.fixedcost * att.skillcount), att.skillid.skillname))
			if det_obj.ratetype.ratetypecode == 'FRCO':
				invoice_list.append({'date':att.date,'skillname':att.skillid.skillname,\
					'designation':att.designation.designation_name,\
					'skillcount':att.skillcount,'skillotcount':att.skillotcount,\
					'otcost':(det_obj.ot * att.skillotcount * 1.0),'fixedcost':det_obj.fixedcost,\
					'total':(det_obj.fixedcost * att.skillcount * 1.0 + (det_obj.ot * att.skillotcount * 1.0))})
				grand_total += (det_obj.fixedcost * att.skillcount)

			elif det_obj.ratetype.ratetypecode == 'CTRT':
				# import pdb;pdb.set_trace()
				total = det_obj.fixedcost * att.skillcount * 1.0
				margin = total * (float(det_obj.marginvalue)/100)
				margintotal = total + margin
				invoice_list.append({'date':att.date,'skillname':att.skillid.skillname,\
					'designation':att.designation.designation_name,\
					'skillcount':att.skillcount,'skillotcount':att.skillotcount,\
					'otcost':(det_obj.ot * att.skillotcount * 1.0),'fixedcost':det_obj.fixedcost,\
					'total':(margintotal + (det_obj.ot * att.skillotcount * 1.0))})
				grand_total += (margintotal)

			else:
				invoice_list.append({'date':att.date,'skillname':att.skillid.skillname,\
					'designation':att.designation.designation_name,\
					'skillcount':att.skillcount,'skillotcount':att.skillotcount,\
					'otcost':(0.0),'fixedcost':det_obj.fixedcost,\
					'total':(0.0)})
		except:
			invoice_list.append({'date':att.date,'skillname':att.skillid.skillname,\
					'designation':att.designation.designation_name,\
					'skillcount':att.skillcount,'skillotcount':att.skillotcount,\
					'otcost':(0.0),'fixedcost':(0.0),\
					'total':(0.0)})
			pass
			# break


	return invoice_list,grand_total



def fixedrateinvoicefunaggregate(det_objs, att_objs):
	invoice_list = []
	grand_total = 0.0
	try:
		for att in att_objs:
			# print('{0} -- {1} -- {2} -- {3}'.format(att.date,att.skillid.skillname,att.skillcount,att.skillotcount))
			det_obj = det_objs.get(skilllevel = att.skillid, designation = att.designation)
			# print('Cost is - {0} -- {1} -- {2}'.format(det_obj.fixedcost, (det_obj.fixedcost * att.skillcount), att.skillid.skillname))
			if att.skillcount == None:
				att.skillcount = 0
			if det_obj.ratetype.ratetypecode == 'LUMS':
				invoice_list.append({'date':att.date,'skillname':att.skillid.skillname,\
					'designation':att.designation.designation_name,\
					'skillcount':att.skillcount,'skillotcount':att.skillotcount,'otcost':(det_obj.ot * att.skillotcount * 1.0),
					'fixedcost':det_obj.fixedcost,\
					'total':(det_obj.fixedcost * 1.0 + (det_obj.ot * att.skillotcount * 1.0))})
				grand_total += (det_obj.fixedcost * 1.0 + (det_obj.ot * att.skillotcount * 1.0))
			else:
				invoice_list.append({'date':att.date,'skillname':att.skillid.skillname,\
					'designation':att.designation.designation_name,\
					'skillcount':att.skillcount,'skillotcount':att.skillotcount,\
					'otcost':(att.skillotcount * det_obj.ot * 1.0),'fixedcost':det_obj.fixedcost,\
					'total':(det_obj.fixedcost * 1.0) + (att.skillotcount * det_obj.ot * 1.0)})
	except:
		return HttpResponse({'msg':'Error during data fetch'})
	return invoice_list,grand_total


def manpowerinvoicefun(det_objs, att_objs):
	from django.db.models import Sum
	import calendar
	from datetime import datetime
	from calendar import monthrange
	invoice_list = []
	grand_total = 0.0

	# print('{0} -- {1} -- {2} -- {3}'.format(att.date,att.skillid.skillname,att.skillcount,att.skillotcount))

	# det_obj = det_objs.get(skilllevel = att.skillid, designation = att.designation)
	# print('Cost is - {0} -- {1} -- {2}'.format(det_obj.fixedcost, (det_obj.fixedcost * att.skillcount), att.skillid.skillname))
	if att_objs:
		month_id = att_objs[0].date.month
		year_id = att_objs[0].date.year
		total_days = monthrange(year_id,month_id)[1]
		sunday_in_month = len([1 for i in calendar.monthcalendar(year_id,month_id) if i[6] != 0])
		working_days = total_days - sunday_in_month
		for det_obj in det_objs:
			try:
				if det_obj.uom == 'Per Month':
					det_obj.fixedcost = float(det_obj.fixedcost / working_days)
				agg_skill_count = att_objs.filter(skillid = det_obj.skilllevel,designation=det_obj.designation).aggregate(sum_skill=Sum('skillcount'))
				agg_skillot_count = att_objs.filter(skillid = det_obj.skilllevel,designation=det_obj.designation).aggregate(sum_skill_ot=Sum('skillotcount'))
				agg_adhoc_count = att_objs.filter(skillid = det_obj.skilllevel,designation=det_obj.designation).aggregate(sum_adhoc=Sum('extrashift'))
				if det_obj.ratetype.ratetypecode == 'FRCO':
					invoice_list.append({'date':att_objs[0].date,'skillname':det_obj.skilllevel.skillname,\
						'designation':det_obj.designation.designation_name,\
						'skillcount':agg_skill_count['sum_skill'],'skillotcount':agg_skillot_count['sum_skill_ot'],\
						'otcost':(det_obj.ot * agg_skillot_count['sum_skill_ot'] * 1.0),'fixedcost':det_obj.fixedcost,\
						'total':(det_obj.fixedcost * agg_skill_count['sum_skill'] * 1.0 + \
									(det_obj.ot * agg_skillot_count['sum_skill_ot'] * 1.0) + \
									(det_obj.adhoc * agg_adhoc_count['sum_adhoc'] * 1.0) \
									)})
					grand_total += (det_obj.fixedcost * agg_skill_count['sum_skill'])

				elif det_obj.ratetype.ratetypecode == 'CTRT':
					# import pdb;pdb.set_trace()
					total = det_obj.fixedcost * agg_skill_count['sum_skill'] * 1.0
					margin = total * (float(det_obj.marginvalue)/100)
					margintotal = total + margin
					invoice_list.append({'date':att_objs[0].date,'skillname':det_obj.skilllevel.skillname,\
						'designation':det_obj.designation.designation_name,\
						'skillcount':agg_skill_count['sum_skill'],'skillotcount':agg_skillot_count['sum_skill_ot'],\
						'otcost':(det_obj.ot * agg_skillot_count['sum_skill_ot'] * 1.0),'fixedcost':det_obj.fixedcost,\
						'total':(margintotal + (det_obj.ot * agg_skillot_count['sum_skill_ot'] * 1.0) + \
								(det_obj.adhoc * agg_adhoc_count['sum_adhoc'] * 1.0) \
								)})
					grand_total += (margintotal)

				else:
					invoice_list.append({'date':att_objs[0].date,'skillname':det_obj.skilllevel.skillname,\
						'designation':det_obj.designation.designation_name,\
						'skillcount':agg_skill_count['sum_skill'],'skillotcount':agg_skillot_count['sum_skill_ot'],\
						'otcost':(0.0),'fixedcost':det_obj.fixedcost,\
						'total':(0.0)})
			except:
				invoice_list.append({'date':att_objs[0].date,'skillname':det_obj.skilllevel.skillname,\
						'designation':det_obj.designation.designation_name,\
						'skillcount':agg_skill_count['sum_skill'],'skillotcount':agg_skillot_count['sum_skill_ot'],\
						'otcost':(0.0),'fixedcost':(0.0),\
						'total':(0.0)})
				pass
				# break


	return invoice_list,grand_total



def fixedrateinvoicefun(det_objs, att_objs):
	from django.db.models import Sum
	invoice_list = []
	grand_total = 0.0
	if att_objs:
		try:
			for det_obj in det_objs:
				# print('{0} -- {1} -- {2} -- {3}'.format(att.date,att.skillid.skillname,att.skillcount,att.skillotcount))
				# det_obj = det_objs.get(skilllevel = att.skillid, designation = att.designation)
				# print('Cost is - {0} -- {1} -- {2}'.format(det_obj.fixedcost, (det_obj.fixedcost * att.skillcount), att.skillid.skillname))
				agg_skill_count = att_objs.filter(skillid = det_obj.skilllevel,designation=det_obj.designation).aggregate(sum_skill=Sum('skillcount'))
				agg_skillot_count = att_objs.filter(skillid = det_obj.skilllevel,designation=det_obj.designation).aggregate(sum_skill_ot=Sum('skillotcount'))
				if agg_skill_count['sum_skill'] == None:
					agg_skill_count['sum_skill'] = 1
				if agg_skill_count['sum_skill'] >= 1:
					agg_skill_count['sum_skill'] = 1
				if agg_skillot_count['sum_skill_ot'] == None:
					agg_skillot_count['sum_skill_ot'] = 1
				if agg_skillot_count['sum_skill_ot'] >= 1:
					agg_skillot_count['sum_skill_ot'] = 1
				if det_obj.ratetype.ratetypecode == 'LUMS':
					invoice_list.append({'date':att_objs[0].date,'skillname':det_obj.skilllevel.skillname,\
						'designation':det_obj.designation.designation_name,\
						'skillcount':agg_skill_count['sum_skill'],'skillotcount':agg_skillot_count['sum_skill_ot'],'otcost':(det_obj.ot * agg_skillot_count['sum_skill_ot'] * 1.0),
						'fixedcost':det_obj.fixedcost,\
						'total':(det_obj.fixedcost * 1.0 + (det_obj.ot * agg_skillot_count['sum_skill_ot'] * 1.0))})
					grand_total += (det_obj.fixedcost * 1.0 + (det_obj.ot * agg_skillot_count['sum_skill_ot'] * 1.0))
				else:
					invoice_list.append({'date':att_objs[0].date,'skillname':det_obj.skilllevel.skillname,\
						'designation':det_obj.designation.designation_name,\
						'skillcount':agg_skill_count['sum_skill'],'skillotcount':agg_skillot_count['sum_skill_ot'],\
						'otcost':(agg_skillot_count['sum_skill_ot'] * det_obj.ot * 1.0),'fixedcost':det_obj.fixedcost,\
						'total':(det_obj.fixedcost * 1.0) + (agg_skillot_count['sum_skill_ot'] * det_obj.ot * 1.0)})
		except:
			return HttpResponse({'msg':'Error during data fetch'})
	return invoice_list,grand_total

# BA5-MLL-2019-05-0608
def outputbasedinvoicefun(det_objs, productivity_objs):
	invoice_list = []
	grand_total = 0.0
	forcount1 = 0
	forcount2 = 0
	# import pdb;pdb.set_trace()
	try:
		for production in productivity_objs:
			# print('{0} -- {1} -- {2} -- {3}'.format(att.date,att.skillid.skillname,att.skillcount,att.skillotcount))
			detail_objs = det_objs.filter(skilllevel = production.skillid, designation = production.designation)
			# print('Cost is - {0} -- {1} -- {2}'.format(det_obj.fixedcost, (det_obj.fixedcost * att.skillcount), att.skillid.skillname))
			# try:
			forcount1 += 1
			min=[]
			max=[]
			cost=[]
			inp = 0
			if detail_objs:
				for det_obj in detail_objs:
					forcount2 += 1

					if det_obj.ratetype.ratetypecode == 'SBOV':#slabbased ovelap
						if production.skillcount is not None:
							if production.skillcount > det_obj.startquantity and production.skillcount <= det_obj.endquantity:
								invoice_list.append({'date':production.date,'skillname':production.skillid.skillname,\
									'designation':production.designation.designation_name,\
									'skillcount':production.skillcount,'skillotcount':production.skillotcount,\
									'otcost':(det_obj.ot * production.skillotcount * 1.0),\
									'fixedcost':det_obj.fixedcost,'total': (det_obj.fixedcost * production.skillcount * 1.0)})
								grand_total += (det_obj.fixedcost * production.skillcount)
								break
					elif det_obj.ratetype.ratetypecode == 'SBFL':#slabbased Flat
						if production.skillcount == None:
							production.skillcount = 0
						# invoice_list.append({'date':production.date,'skillname':production.skillid.skillname,\
						# 	'skillcount':production.skillcount,'skillotcount':production.skillotcount,\
						# 	'otcost':production.skillotcount,\
						# 	'fixedcost':det_obj.fixedcost,'total': (det_obj.fixedcost * production.skillcount * 1.0)})
						# grand_total += (det_obj.fixedcost * production.skillcount)
						min.append(det_obj.startquantity)
						max.append(det_obj.endquantity)
						cost.append(det_obj.fixedcost)
						inp = production.skillcount

				tot_cost=0

				for i,j,c in zip(max,min,cost):
					if(inp>=i):
						tot_cost=tot_cost+(i-j)*c
						print(tot_cost,"if")

					else:
						tot_cost=tot_cost+(inp-j+1)*c
						print(tot_cost,"else")
						# print(j)
						break
				grand_total += tot_cost

				invoice_list.append({'date':production.date,'skillname':production.skillid.skillname,\
					'designation':production.designation.designation_name,\
					'skillcount':production.skillcount,'skillotcount':production.skillotcount,\
					'otcost':0.0,'fixedcost':0.0,'total': tot_cost})
			else:
				invoice_list.append({'date':production.date,'skillname':production.skillid.skillname,\
					'designation':production.designation.designation_name,\
					'skillcount':production.skillcount,'skillotcount':production.skillotcount,\
					'otcost':0.0, 'fixedcost':0.0,'total': 0.0})
		# except:
		# 	pass
	except:
		return HttpResponse({'msg':'Error during data fetch'})
			# else:
	print("{0} -- {1} -- {2}".format(forcount1,forcount2,invoice_list))
	return invoice_list,grand_total


class AdditionalContractFieldView(viewsets.ModelViewSet):
	"""
		Perform Add, Update, Delete operation
	"""
	queryset = AdditionalContractField.objects.all()
	serializer_class = AdditionalContractFieldSerializers
	# permission_classes = (permissions.IsAuthenticated, )


	def create(self, request, format=None):
		serializer = AdditionalContractFieldSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


	def getAdditionalContractField(self, request, *args, **kwargs):
		"""
		Get Contract detail using contractid
		"""
		getcontractdetail = self.kwargs['contractid']
		contracttype_id = Contract.objects.get(contractid = getcontractdetail).contracttype
		contract_detail = AdditionalContractField.objects.filter(contract = getcontractdetail)

		serializer = AdditionalContractFieldSerializers(contract_detail, many=True)
		return Response(serializer.data)

	def additionalContractFieldCapture(self, request, *args, **kwargs):
		"""
		Capture contractdetail from JSON
		"""
		# import pdb;pdb.set_trace()
		jsonData = request.data
		contractid = jsonData['contractid']
		contractdetaillist = jsonData['condetaillist']
		# import pdb;pdb.set_trace()
		for dt in contractdetaillist:
			try:
				if dt['cost'] == '':
					dt['cost'] = 0

				dt['contract'] = Contract.objects.get(contractid = contractid)

				if 'contractaddfieldid' in dt.keys():
					contractdetail = AdditionalContractField.objects.filter(contractaddfieldid = dt['contractaddfieldid'])
					contractdetail.update(**dt)
				else:
					dtlist = AdditionalContractField(**dt)
					dtlist.save()

			except Exception as e:
				return Response([str(e)],status=status.HTTP_400_BAD_REQUEST)
		return Response(status=status.HTTP_201_CREATED)

class Contract_Percentage_FieldView(viewsets.ModelViewSet):
	"""
		Perform Add, Update, Delete operation
	"""
	queryset = Contract_Percentage_Field.objects.all()
	serializer_class = Contract_Percentage_FieldSerializers
	# permission_classes = (permissions.IsAuthenticated, )


	def create(self, request, format=None):
		serializer = Contract_Percentage_FieldSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


	def getContractpercentageField(self, request, *args, **kwargs):
		"""
		Get Contract detail using contractid
		"""
		getcontractdetail = self.kwargs['contractid']
		contracttype_id = Contract.objects.get(contractid = getcontractdetail).contracttype
		contract_detail = Contract_Percentage_Field.objects.filter(contract = getcontractdetail)

		serializer = Contract_Percentage_FieldSerializers(contract_detail, many=True)
		return Response(serializer.data)

	def percentageContractFieldCapture(self, request, *args, **kwargs):
		"""
		Capture contractdetail from JSON
		"""
		# import pdb;pdb.set_trace()
		jsonData = request.data
		contractid = jsonData['contractid']
		contractdetaillist = jsonData['condetaillist']
		# import pdb;pdb.set_trace()
		for dt in contractdetaillist:
			try:
				if dt['percentage'] == '':
					dt['percentage'] = 0

				dt['contract'] = Contract.objects.get(contractid = contractid)

				if 'contract_per_loc_id' in dt.keys():
					contractdetail = Contract_Percentage_Field.objects.filter(contract_per_loc_id = dt['contract_per_loc_id'])
					contractdetail.update(**dt)
				else:
					dtlist = Contract_Percentage_Field(**dt)
					dtlist.save()

			except Exception as e:
				return Response([str(e)],status=status.HTTP_400_BAD_REQUEST)
		return Response(status=status.HTTP_201_CREATED)


class ContractDetailView(viewsets.ModelViewSet):
	"""
		Perform Add, Update, Delete operation
	"""
	queryset = ContractDetail.objects.all()
	serializer_class = ContractDetailSerializers
	# permission_classes = (permissions.IsAuthenticated, )


	def create(self, request, format=None):
		serializer = ContractDetailSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


	def getContractDetail(self, request, *args, **kwargs):
		"""
		Get Contract detail using contractid
		"""
		getcontractdetail = self.kwargs['contractid']
		contracttype_id = Contract.objects.get(contractid = getcontractdetail).contracttype
		contract_detail = ContractDetail.objects.filter(contract = getcontractdetail)

		if contracttype_id.contracttypeid !=3:
			contract_detail = ContractDetail.objects.filter(contract = getcontractdetail)
			from contract.models import ContractDetail_Reference_Aadharid
			for contractdetail_obj in contract_detail:
				aadhaar_data_list = []
				list_aadhaar = ContractDetail_Reference_Aadharid.objects.filter(contractdetailid_fk = contractdetail_obj)
				if list_aadhaar.count() > 0:
					for aadhaar in list_aadhaar:
						aadhaar_data_list.append(aadhaar.aadhaarid)
					contractdetail_obj.aadhaar_data = ','.join(aadhaar_data_list)
		else:
			"""
				Implement distinct feature to get specific skilllevel
			"""

			contract_detail = contract_detail.order_by('skilllevel')

		serializer = ContractDetailSerializers(contract_detail, many=True)
		return Response(serializer.data)

	def getContractDetail_output_based_pricing(self, request, *args, **kwargs):
		"""
		Get Contract detail using contractid
		"""
		import copy
		contract_detail_temp_list = []
		getcontractdetail = self.kwargs['contractid']
		contracttype_id = Contract.objects.get(contractid = getcontractdetail).contracttype
		contract_detail = ContractDetail.objects.filter(contract = getcontractdetail)
		if contracttype_id.contracttypeid !=3:
			contract_detail = ContractDetail.objects.filter(contract = getcontractdetail)
		else:
			"""
				Implement distinct feature to get specific skilllevel
			"""
			contract_detail = contract_detail.order_by('skilllevel')
			if contract_detail.count() > 1:
				for index,val in enumerate(contract_detail):
					if index == 0:
						contract_detail_temp_list.append(val)
					else:
						if val.skilllevel == contract_detail[index-1].skilllevel and \
							val.designation == contract_detail[index-1].designation:
							pass
						else:
							contract_detail_temp_list.append(val)

		contract_detail_temp = copy.deepcopy(contract_detail)
		# for co in contract_detail:
		# 	l = 0
		# 	for co1 in contract_detail_temp:
		# 		m = 0
		# 		if m==0 and l ==0 and co == co1:
		# 			m += 1
		# 			pass
		# 		if m > 0 and i.contacttype == j.contacttype and i.ratetype == j.ratetype\
		# 		 and i.skilllevel == j.skilllevel and i.designation == j.designation:
		# 			m += 1
		# 			j.delete()
		serializer = ContractDetailSerializers(contract_detail_temp_list, many=True)
		return Response(serializer.data)


	def contractDetailCapture(self, request, *args, **kwargs):
		"""
		Capture contractdetail from JSON
		"""
		# import pdb;pdb.set_trace()
		jsonData = request.data
		contractid = jsonData['contractid']
		contractdetaillist = jsonData['condetaillist']
		# import pdb;pdb.set_trace()
		for dt in contractdetaillist:
			try:
				if dt['startquantity'] == '':
					dt['startquantity'] = 0
				if dt['endquantity'] == '':
					dt['endquantity'] = 0
				if dt['requirequantity'] == '':
					dt['requirequantity'] = 0
				if dt['ot'] == '':
					dt['ot'] = 0
				if dt['adhoc'] == '':
					dt['adhoc'] = 0

				aadhaar_data = dt['aadhaar_data']
				dt['aadhaar_data'] = ''
				dt['startquantity'] = int(dt['startquantity'])
				dt['endquantity'] = int(dt['endquantity'])
				dt['contract'] = Contract.objects.get(contractid = contractid)
				dt['contacttype'] = ContractType.objects.get(contracttypeid = dt['contract'].contracttype.pk)
				dt['ratetype'] = RateType.objects.get(ratetypeid = dt['ratetype'])
				dt['skilllevel'] = SkillLevel.objects.get(skillid = dt['skilllevel'])
				if dt['contract'].contracttype.pk == 3:
					dt['designation'] = Designation.objects.all()[0]
					dt['fixedcost'] = float(dt['fixedcost'])
				else:
					dt['designation'] = Designation.objects.get(designation_id = dt['designation'])
				if 'contractdetid' in dt.keys():
					contractdetail = ContractDetail.objects.filter(contractdetid = dt['contractdetid'])
					update_save_aadhaar(aadhaar_data,contractdetail)
					contractdetail.update(**dt)
				else:
					dtlist = ContractDetail(**dt)
					dtlist.save()
					contractdetail = ContractDetail.objects.filter(contractdetid = dtlist.contractdetid)
					update_save_aadhaar(aadhaar_data,contractdetail)

			except Exception as e:
				return Response([str(e)],status=status.HTTP_400_BAD_REQUEST)
		return Response(status=status.HTTP_201_CREATED)


def update_save_aadhaar(aadhaar_data,contractdetail):
	from contract.models import ContractDetail_Reference_Aadharid
	flag = 0
	flag1 = 0
	if aadhaar_data and contractdetail.count() > 0:
		contractdetail = contractdetail.first()
		aadhaar_list = aadhaar_data.split(',')
		all_aadharid = ContractDetail_Reference_Aadharid.objects.filter(contractdetailid_fk = contractdetail)
		old_aadhaar_list = []
		if all_aadharid.count() == 0:
			for aadhaar_id in aadhaar_list:
				ContractDetail_Reference_Aadharid(contractdetailid_fk = contractdetail,
					aadhaarid = aadhaar_id).save()
		else:
			for aadhaar_id in aadhaar_list:
				flag = 0
				for aadhaar_obj in all_aadharid:
					if aadhaar_obj.aadhaarid == aadhaar_id:
						flag = 1
						old_aadhaar_list.append(aadhaar_id)
				if flag == 1:
					continue
				else:
					ContractDetail_Reference_Aadharid(contractdetailid_fk = contractdetail,
					aadhaarid = aadhaar_id).save()
			old_aadhaar_list.extend(aadhaar_list)
			#delete unneccecssry aadhaarid
			all_aadhaarid_new = ContractDetail_Reference_Aadharid.objects.filter(contractdetailid_fk = contractdetail)
			for aa_id in all_aadhaarid_new:
				flag1 = 0
				for oo_aad in old_aadhaar_list:
					if aa_id.aadhaarid == oo_aad:
						flag1 = 1
				if flag1 == 0:
					aa_id.delete()
	if aadhaar_data == None or aadhaar_data is None or aadhaar_data == '':
		contractdetail = contractdetail.first()
		all_aadharid = ContractDetail_Reference_Aadharid.objects.filter(contractdetailid_fk = contractdetail)
		for del_aadhaar_data in all_aadharid:
			del_aadhaar_data.delete()


# class DocumentView(APIView):
# 	parser_classes = (MultiPartParser, FormParser)

# 	def get(self, request, *args):
# 		document = Document.objects.all()
# 		serializer = DocumentSerializers(document, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, *args, **kwargs):
# 		doc_serializer = DocumentSerializers(data=request.data)
# 		if doc_serializer.is_valid():
# 			doc_serializer.save()
# 			return Response(doc_serializer.data, status=status.HTTP_201_CREATED)
# 		else:
# 			return Response(doc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentView(viewsets.ModelViewSet):
	queryset = Document.objects.all()
	# lookup_field = 'contractid'
	serializer_class = DocumentSerializers

	def retrieve(self, request, pk=None):
		contractid = self.kwargs['pk']
		instance = self.get_queryset().filter(contractid = contractid)
		serializer = DocumentSerializers(instance, many=True)
		return Response(serializer.data)

	def update(self, request, *args, **kwargs):
		contractid = self.kwargs['pk']
		# instance = self.get_object(contractid = contractid)
		try:
			instance = self.get_queryset().filter(contractid = contractid)[0]
		except:
			return Response({"msg":'No data Found'})
		serializer = DocumentSerializers(instance=instance,data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data)

	def delete(self, request, *args, **kwargs):
		instance = self.get_queryset()[0]
		instance.document.delete(True)
		instance.document1.delete(True)
		instance.document2.delete(True)
		instance.delete()
		if instance == None:
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)


def home(request):
	documents = Document.objects.all()
	return render(request, 'contract/home.html', { 'documents': documents })

def upload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = DocumentForm()
	return render(request, 'contract/upload.html', {
		'form': form
	})


# class ContractView(APIView):

#     def get_object(self, pk):
#         try:
#             return Contract.objects.get(pk=pk)
#         except Contract.DoesNotExist:
#             raise Http404

# 	def get(self, request):
#         contract_all = contract.objects.all()
#         serializer = ContractSerializers(contract_all, many = True)
#         return Response(serializer.data)

#     def get(self, request, pk, format=None):
#         contract = self.get_object(pk)
#         serializer = ContractSerializers(contract)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ContractSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk, format=None):
#         contract = self.get_object(pk)
#         serializer = ContractSerializers(contract, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         contract = self.get_object(pk)
#         contract.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class DetailAttCaptureView(viewsets.ModelViewSet):
	"""
		API for attendance capture
		Perform Add, Update, Delete operation
	"""
	queryset = DetailAttCapture.objects.all()
	serializer_class = DetailAttCaptureSerializers

	def create(self, request, format=None):
		serializer = DetailAttCaptureSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


	def attDetail(self, request, *args, **kwargs):
		"""
		Get Attendance detail using contractid and date
		where date format should be yyyy-mm-dd format
		"""
		contractid = self.kwargs['contractid']
		date_att = self.kwargs['date_att']
		from datetime import datetime, timedelta
		date_att1 = datetime.strptime(date_att,'%Y-%m-%d').date() + timedelta(days=5)


		att_detail = DetailAttCapture.objects.filter(contractid = contractid, date__gte = date_att, date__lte = date_att)
		serializer = DetailAttCaptureSerializers(att_detail, many=True)
		return Response(serializer.data)


	def consolidatedBAAttDetail(self, request, *args, **kwargs):
		"""
		Get Attendance detail using contractid and date
		where date format should be yyyy-mm-dd format
		"""
		from datetime import datetime, timedelta
		contractid = self.kwargs['contractid']
		date_att = self.kwargs['date_att']
		date_att1 = datetime.strptime(date_att,'%Y-%m-%d').date() + timedelta(days=5)


		"""
		{
			"id": 72,
			"contractid": "nocustcode-MLL-2019-06-20-081311",
			"date": "2019-06-19",
			"skillid": 6,
			"skillcount": 560,
			"skillotcount": 0,
			"extrashift": 0
		}
		"""
		get_ba_detail = Contract.objects.filter(relatedcontract = contractid)
		list_ba_att_consolidated = []

		from django.db.models import Sum
		list_of_ba = get_ba_detail.values_list('contractid')
		ba_att_detail = DetailAttCapture.objects.filter(contractid__in = list_of_ba, date__gte = date_att,date__lte = date_att)

		list_of_skill = set(ba_att_detail.values_list('skillid'))
		countid = 1000
		for skill in list_of_skill:
			dict_ba_att_consolidated = {}
			skillcount = ba_att_detail.filter(skillid = skill).aggregate(Sum('skillcount'))
			skillotcount = ba_att_detail.filter(skillid = skill).aggregate(Sum('skillotcount'))
			extrashift = ba_att_detail.filter(skillid = skill).aggregate(Sum('extrashift'))
			dict_ba_att_consolidated['id'] = countid
			dict_ba_att_consolidated['contractid'] = contractid
			dict_ba_att_consolidated['date'] = date_att
			dict_ba_att_consolidated['skillid'] = skill[0]
			dict_ba_att_consolidated['skillcount'] = skillcount['skillcount__sum']
			dict_ba_att_consolidated['skillotcount'] = skillotcount['skillotcount__sum']
			dict_ba_att_consolidated['extrashift'] = extrashift['extrashift__sum']
			list_ba_att_consolidated.append(dict_ba_att_consolidated)
			countid += 1
			# print('skill-{0}, skillcount-{1}, skillotcount-{2}, extrashift-{3}'.format(skill,skillcount,skillotcount,extrashift))


		# for ba_obj in get_ba_detail:
		# 	print('ba Contract ID - {0}'.format(ba_obj.contractid))
		# 	ba_att_detail = DetailAttCapture.objects.filter(contractid = ba_obj.contractid, date = date_att)
		# 	if ba_att_detail:
		# 		for ba_att in ba_att_detail:
		# 			print('"id": {0},"contractid": {1},"date": {2},"skillid": {3},"skillcount": {4},"skillotcount": {5},"extrashift": {6}'.format(ba_att.id,\
		# 			ba_att.contractid,ba_att.date,\
	 #    			ba_att.skillid,ba_att.skillcount,ba_att.skillotcount,ba_att.extrashift))

		# att_detail = DetailAttCapture.objects.filter(contractid = contractid, date = date_att)
		# serializer = DetailAttCaptureSerializers(att_detail, many=True)
		# return Response(serializer.data)
		print(list_ba_att_consolidated)
		return Response(list_ba_att_consolidated)


	def attDetailCapture(self, request, *args, **kwargs):
		"""
		Capture attendance of contract from JSON
		"""
		jsonData = request.data
		contractid = jsonData['contractid']
		attdetaillist = jsonData['attlist']

		for dt in attdetaillist:
			try:
				dt['contractid'] = Contract.objects.get(contractid = contractid)
				dt['skillid'] = SkillLevel.objects.get(skillid = dt['skillid'])
				dt['designation'] = Designation.objects.get(designation_id = dt['designation'])
				# import pdb;pdb.set_trace()
				if 'id' in dt.keys():
					contractdetail = DetailAttCapture.objects.filter(id = dt['id'], date = dt['date'])
					if contractdetail.count() > 0:
						contractdetail.update(**dt)
					else:
						dtlist = DetailAttCapture(**dt)
						dtlist.save()
				else:
					dtlist = DetailAttCapture(**dt)
					dtlist.save()
			except Exception as e:
				return Response([str(e)],status=status.HTTP_400_BAD_REQUEST)
		return Response(status=status.HTTP_201_CREATED)

	def capture_att_detail_api(self, request, *args, **kwargs):
		"""
		Date format should be in dd-mm-yyyy
		Date format should be in dd-mm-yyyy
		Perform Add, Update, Delete operation
		"""

		from contract.models import DetailAttCapture,Designation,Contract,ContractDetail,SkillLevel
		from account.models import BA,UserLocationCustomer
		from location.models import OperationLocation
		import json
		import urllib.request
		import time
		from datetime import datetime
		# siteid = self.kwargs['siteid']
		# vendorid = self.kwargs['vendorid']
		# contractid = self.kwargs['contractid']

		site_vendor_dict = {}

		all_customer_contract = Contract.objects.filter(contractwith = '0').values_list('contractid')

		all_customer_contract_list = [i[0] for i in all_customer_contract]

		for contractid in all_customer_contract_list:

			get_related_ba_detail = Contract.objects.filter(relatedcontract = contractid).values_list('ba')

			get_related_ba_detail_list = [i[0] for i in get_related_ba_detail]

			site_vendor_dict[contractid] = get_related_ba_detail_list


		# finding siteid and vendorid list

		new_site_vendor_dict = {}
		for contractid,ba_list in site_vendor_dict.items():
			try:
				customer_location = Contract.objects.get(contractid = contractid).locationcust.ulcpkey

				userlocationcutomer = UserLocationCustomer.objects.get(ulcpkey = customer_location)

				oplocation = OperationLocation.objects.get(oplocationid = userlocationcutomer.location.oplocationid)

				siteid = oplocation.betterplace_siteid

				print(siteid)


				vendorid = BA.objects.filter(baid__in = ba_list).values_list('bttrplce_vendorid')

				vendorid_list = [i[0] for i in vendorid]

				print(vendorid_list)
				new_site_vendor_dict[contractid] = {siteid : vendorid_list}



			except:
				print('no map location found')
				pass

		apikey = 'Zsj0+CkJJck1e8fwe1L20Zxpu1pbsnWu/7V16dHBdEir63N6tiiU4ozRi3qBGd6ZBeZaS1EL8bkvtOML6tT1xw=='
		headers = {'apikey' : apikey }
		# date2 = dateime.strptime(date1,'%d-%m-%Y').date()
		# date_att = self.kwargs['date_att']

		date1 = self.kwargs['date_att']
		date1_l = date1.split('-')
		date2 = '{0}-{1}-{2}'.format(date1_l[2],date1_l[1],date1_l[0])

		entry_data_dict = []
		for contractid,site_vendor_dict in new_site_vendor_dict.items():
			print('cotractid {0} site_vendor_dict {1}'.format(contractid,site_vendor_dict))
			if site_vendor_dict:
				for siteid,vendor_list in site_vendor_dict.items():
					if vendor_list:
						for vendorid in vendor_list:
							if vendorid != 'no data' and vendorid != '':
								call_function = betterplace_att_capt(siteid,vendorid,contractid,date1,date2,apikey,headers)
								entry_data_dict.append(new_site_vendor_dict)

		list_ba_att_consolidated = []
		return Response(entry_data_dict)

	def manual_attcapture_detail_api(self, request, *args, **kwargs):
		"""
		Date format should be in dd-mm-yyyy
		Date format should be in dd-mm-yyyy
		Perform Add, Update, Delete operation
		"""
		import time
		from datetime import datetime
		# siteid -6658057086421798976 , contractid - 3M-Indi-MLL-2020-01-21-122406, date
		siteid = date1 = self.kwargs['siteid']
		contractid = self.kwargs['contractid']
		date1 = date1 = self.kwargs['date_att']
		betterplace_att_capt_new(siteid, contractid, date1)
		return Response({"record capture successfully"})


def betterplace_att_capt(siteid,vendorid,contractid,date1,date2,apikey,headers):
	from contract.models import DetailAttCapture,Designation,Contract,ContractDetail,SkillLevel
	from account.models import BA,UserLocationCustomer
	from location.models import OperationLocation
	import json
	import urllib.request
	import time
	from datetime import datetime
	att_url = "https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getRecordSiteVendor?vendor={0}&siteId={1}&startDate={2}&endDate={3}".format(vendorid,siteid,date1,date1)
	req1 = urllib.request.Request(att_url)
	req1.add_header('apikey',apikey)

	#https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getRecordSiteVendor?vendor=10178163594610587744&siteId=16252173452509896464&startDate=05-08-2019&endDate=09-09-2019
	print('vendorid - {0} - siteid - {1}'.format(vendorid,siteid))

	recordsitevendor_dict = urllib.request.urlopen(req1).read()
	time.sleep(5)
	recordsitevendor_dict = str(recordsitevendor_dict,'utf-8')

	recordsitevendor_json = json.loads(recordsitevendor_dict)
	recordsitevendor_data = recordsitevendor_json['data']

	if recordsitevendor_data['attendanceDetails'] is not None:
		print('vendorid - {0} * siteid - {1} * attdata - {2}'.format(vendorid\
		 ,siteid,recordsitevendor_data['attendanceDetails']))
		# get conntract detail data
		contractdetail = ContractDetail.objects.filter(contract = contractid)
		skill_list = [i[0] for i in contractdetail.values_list('skilllevel')]
		designation_list = [i[0] for i in contractdetail.values_list('designation')]
		zip_of_skill_designation = [i for i in zip(skill_list,designation_list)]
		for att_dict in recordsitevendor_data['attendanceDetails']:
			# import pdb;pdb.set_trace()
			print('job funct **** {0}'.format(att_dict['jobfunction']))
			try:
				job_function = Designation.objects.get(designation_name = att_dict['jobfunction']) #designation_id , designation_name
				for i in zip_of_skill_designation:
					if i[1] == job_function.designation_id:
						try:
							get_existing_attdetail = DetailAttCapture.objects.get(contractid= contractid,date= date2,skillid= i[0],designation= i[1])
							get_existing_attdetail.skillcount = int(float(att_dict['regManDays']))
							get_existing_attdetail.skillotcount =  int(float(att_dict['totalOTHrs']))
							get_existing_attdetail.extrashift = int(0)
							get_existing_attdetail.save()
						except:
							print('Not Exist')
							attcapture_obj = DetailAttCapture()
							attcapture_obj.contractid = Contract.objects.get(contractid = contractid)
							attcapture_obj.date = date2
							attcapture_obj.skillid = SkillLevel.objects.get(skillid = i[0])# skillid , skillname
							attcapture_obj.designation = Designation.objects.get(designation_id = i[1]) #designation_id , designation_name
							attcapture_obj.skillcount = int(float(att_dict['regManDays']))
							attcapture_obj.skillotcount =  int(float(att_dict['totalOTHrs']))
							attcapture_obj.extrashift = int(0)
							attcapture_obj.save()
						print('Data Inserted Successfully')
						break
			except:
				print('No job function map')
				pass


def call_betterplace_schedular_fun():
	from contract.models import DetailAttCapture,Designation,Contract,ContractDetail,SkillLevel
	contract_siteid_obj_list = Contract.objects.filter(contractwith = '0').values_list('betterpalcesiteid')
	contract_siteid_list = [i[0] for i in contract_siteid_obj_list if i[0] is not None]
	contract_siteid_list = list(set(contract_siteid_list))
	for siteid in contract_siteid_list:
		contract_list_obj = Contract.objects.filter(betterpalcesiteid = siteid, contractwith = '0')
		# 0 identifies only customer contract
		if contract_list_obj:
			for contract_obj in contract_list_obj:
				contractid = contract_obj.contractid
				betterplace_att_capt_new(siteid, contractid, None)


def betterplace_att_capt_new(siteid, contractid, date2=None):
	from contract.models import DetailAttCapture,Designation,Contract\
		,ContractDetail,SkillLevel,ContractDetail_Reference_Aadharid
	from account.models import BA,UserLocationCustomer
	from location.models import OperationLocation
	import json
	import urllib.request
	import time
	from datetime import datetime
	# att_url = "https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getRecordSiteVendor?vendor={0}&siteId={1}&startDate={2}&endDate={3}".format(vendorid,siteid,date1,date1)

	if date2 is None:
		date1 = str(datetime.today().date())
		date1_str = date1.split('-')
		date1 = date1_str[2]+'-'+date1_str[1]+'-'+date1_str[0]
	else:
		date1 = date2
	siteid = siteid
	apiKey = "Zsj0+CkJJck1e8fwe1L20Zxpu1pbsnWu/7V16dHBdEir63N6tiiU4ozRi3qBGd6ZBeZaS1EL8bkvtOML6tT1xw=="
	att_url = "https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getAttendanceRecordsForSiteVendorBased?siteId={0}&startDate={1}&endDate={2}".format(siteid,date1,date1)
	req1 = urllib.request.Request(att_url)
	req1.add_header('apikey', apiKey)

	recordsitevendor_dict = urllib.request.urlopen(req1).read()
	time.sleep(5)	
	recordsitevendor_dict = str(recordsitevendor_dict,'utf-8')

	recordsitevendor_json = json.loads(recordsitevendor_dict)

	recordsitevendor_data = recordsitevendor_json['data']

	find_customer_ba_contract = Contract.objects.all()
	# find_cust_contract = find_customer_ba_contract.get(contractwith = "0", betterpalcesiteid = siteid)
	# contractid = find_cust_contract.contractid

	contractid = contractid

	if recordsitevendor_data['attendanceVendorsforSite'] is not None:
		# print('siteid - {0} * attdata - {1}'.format(siteid,recordsitevendor_data['attendanceVendorsforSite']))
		print('=====================================================================================================')
		print('siteid - {0} * contractid - {1} date - {2}'.format(siteid,contractid,date1))
		# get ba contract which is related to customer conntract detail data
		related_ba_contract = find_customer_ba_contract.filter(relatedcontract = contractid)
		# customer contract filter
		contractdetail = ContractDetail.objects.filter(contract = contractid)
		skill_list = [i[0] for i in contractdetail.values_list('skilllevel')]
		designation_list = [i[0] for i in contractdetail.values_list('designation')]
		contractdetid_list = [i[0] for i in contractdetail.values_list('contractdetid')]
		zip_of_skill_designation = [i for i in zip(skill_list,designation_list,contractdetid_list)]
		for att_dict in recordsitevendor_data['attendanceVendorsforSite']:
			# import pdb;pdb.set_trace()
			# print('job funct **** {0}'.format(att_dict['attendanceVendorNameFunList']))
			# for i in att_dict['attendanceVendorNameFunList']: print(i['attendanceJobRoleList'])
			try:
				dateX=date1.split('-')
				dateX = dateX[2]+'-'+dateX[1]+'-'+dateX[0]
				all_attdata_on_date = DetailAttCapture.objects.filter(contractid= contractid,date= dateX)
				if all_attdata_on_date:
					print('deleted all data on date {0} and inserting new record'.format(dateX))
					all_attdata_on_date.delete()
				for vendor_att_dict_list in att_dict['attendanceVendorNameFunList']:
					print("vendor Name --->",vendor_att_dict_list['vendorName'])
					if related_ba_contract:
						for ba_contract in related_ba_contract:
							ba_id = ba_contract.ba
							ba_contractid = ba_contract.contractid
							ba_object = BA.get.objects(baid = ba_id)
							ba_name = ba_object.baname
							if ba_name == vendor_att_dict_list['vendorName']:
								# capture BA attendance data from better place id
								call_ba_attendence(ba_contractid, ba_object, date1, vendor_att_dict_list)
								break 
					for vendor_att_dict in vendor_att_dict_list['attendanceJobRoleList']:
						# job_function = Designation.objects.get(designation_name = vendor_att_dict['jobfunction']) #designation_id , designation_name
						job_function = Designation.objects.filter(designation_name = vendor_att_dict['jobfunction']) #designation_id , designation_name
						if job_function:
							for i in zip_of_skill_designation:
								if i[1] == job_function[0].designation_id:
									try:
										dateX=date1.split('-')
										dateX = dateX[2]+'-'+dateX[1]+'-'+dateX[0]
										get_existing_attdetail = DetailAttCapture.objects.get(contractid= contractid,date= dateX,skillid= i[0],designation= i[1])
										all_aadhaar_list_objs = ContractDetail_Reference_Aadharid.objects.filter(
											contractdetailid_fk = contractdetail.get(contractdetid = i[2]))
										print('previous date {0} skill_desi_detid {1} \
											get_existing_attdetail.skillcount {2}'.format(
												dateX,i,get_existing_attdetail.skillcount))
										if all_aadhaar_list_objs.count() > 0:
											all_aadhaar_list = [str(i.aadhaarid) for i in all_aadhaar_list_objs]
											print('aadhaarlist {0}'.format(all_aadhaar_list))
											count = 0
											for betterplace_emp in vendor_att_dict['employeeData']:
												if betterplace_emp['govtId'] in all_aadhaar_list:
													print('matchid {0}'.format(betterplace_emp['govtId']))
													count += 1
											get_existing_attdetail.skillcount += int(float(count))
										else:
											get_existing_attdetail.skillcount += 0
											# get_existing_attdetail.skillcount += int(float(vendor_att_dict['regManDays']))
										print('final count {0}'.format(get_existing_attdetail.skillcount))
										get_existing_attdetail.skillotcount +=  int(float(vendor_att_dict['totalOTHrs']))
										get_existing_attdetail.extrashift += int(0)
										get_existing_attdetail.save()
									except:
										print('Not Exist')
										attcapture_obj = DetailAttCapture()
										attcapture_obj.contractid = Contract.objects.get(contractid = contractid)
										attcapture_obj.date = dateX
										attcapture_obj.skillid = SkillLevel.objects.get(skillid = i[0])# skillid , skillname
										attcapture_obj.designation = Designation.objects.get(designation_id = i[1]) #designation_id , designation_name
										all_aadhaar_list_objs = ContractDetail_Reference_Aadharid.objects.filter(
											contractdetailid_fk = contractdetail.get(contractdetid = i[2]))
										print('previous date {0} skill_desi_detid {1} \
											get_existing_attdetail.skillcount {2}'.format(
												dateX,i,attcapture_obj.skillcount))
										if all_aadhaar_list_objs.count() > 0:
											all_aadhaar_list = [str(i.aadhaarid) for i in all_aadhaar_list_objs]
											count = 0
											for betterplace_emp in vendor_att_dict['employeeData']:
												if betterplace_emp['govtId'] in all_aadhaar_list:
													print('matchid {0}'.format(betterplace_emp['govtId']))
													count += 1
											attcapture_obj.skillcount = int(float(count))
										else:
											attcapture_obj.skillcount = 0
											# attcapture_obj.skillcount = int(float(vendor_att_dict['regManDays']))
										print('final count {0}'.format(attcapture_obj.skillcount))
										attcapture_obj.skillotcount =  int(float(vendor_att_dict['totalOTHrs']))
										attcapture_obj.extrashift = int(0)
										attcapture_obj.save()
									print('Data Inserted Successfully')
									break
			except:
				print('No job function map')
				pass

def call_ba_attendence(ba_contractid, ba_object, date1, vendor_att_dict_list):
	from contract.models import DetailAttCapture,Designation,Contract\
		,ContractDetail,SkillLevel,ContractDetail_Reference_Aadharid
	from account.models import BA,UserLocationCustomer
	from location.models import OperationLocation
	import json
	import urllib.request
	import time
	from datetime import datetime

	contractdetail = ContractDetail.objects.filter(contract = ba_contractid)
	skill_list = [i[0] for i in contractdetail.values_list('skilllevel')]
	designation_list = [i[0] for i in contractdetail.values_list('designation')]
	contractdetid_list = [i[0] for i in contractdetail.values_list('contractdetid')]
	zip_of_skill_designation = [i for i in zip(skill_list,designation_list,contractdetid_list)]
	try:
		dateX=date1.split('-')
		dateX = dateX[2]+'-'+dateX[1]+'-'+dateX[0]
		all_attdata_on_date = DetailAttCapture.objects.filter(contractid= ba_contractid,date= dateX)
		if all_attdata_on_date:
			print('deleted all data on date {0} and inserting new record'.format(dateX))
			all_attdata_on_date.delete()
		for vendor_att_dict in vendor_att_dict_list['attendanceJobRoleList']:
			# job_function = Designation.objects.get(designation_name = vendor_att_dict['jobfunction']) #designation_id , designation_name
			job_function = Designation.objects.filter(designation_name = vendor_att_dict['jobfunction']) #designation_id , designation_name
			if job_function:
				for i in zip_of_skill_designation:
					if i[1] == job_function[0].designation_id:
						try:
							dateX=date1.split('-')
							dateX = dateX[2]+'-'+dateX[1]+'-'+dateX[0]
							get_existing_attdetail = DetailAttCapture.objects.get(contractid= ba_contractid,date= dateX,skillid= i[0],designation= i[1])
							all_aadhaar_list_objs = ContractDetail_Reference_Aadharid.objects.filter(
								contractdetailid_fk = contractdetail.get(contractdetid = i[2]))
							print('previous date {0} skill_desi_detid {1} \
								get_existing_attdetail.skillcount {2}'.format(
									dateX,i,get_existing_attdetail.skillcount))
							if all_aadhaar_list_objs.count() > 0:
								all_aadhaar_list = [str(i.aadhaarid) for i in all_aadhaar_list_objs]
								print('aadhaarlist {0}'.format(all_aadhaar_list))
								count = 0
								for betterplace_emp in vendor_att_dict['employeeData']:
									if betterplace_emp['govtId'] in all_aadhaar_list:
										print('matchid {0}'.format(betterplace_emp['govtId']))
										count += 1
								get_existing_attdetail.skillcount += int(float(count))
							else:
								get_existing_attdetail.skillcount += 0
								# get_existing_attdetail.skillcount += int(float(vendor_att_dict['regManDays']))
							print('final count {0}'.format(get_existing_attdetail.skillcount))
							get_existing_attdetail.skillotcount +=  int(float(vendor_att_dict['totalOTHrs']))
							get_existing_attdetail.extrashift += int(0)
							get_existing_attdetail.save()
						except:
							print('Not Exist')
							attcapture_obj = DetailAttCapture()
							attcapture_obj.contractid = Contract.objects.get(contractid = ba_contractid)
							attcapture_obj.date = dateX
							attcapture_obj.skillid = SkillLevel.objects.get(skillid = i[0])# skillid , skillname
							attcapture_obj.designation = Designation.objects.get(designation_id = i[1]) #designation_id , designation_name
							all_aadhaar_list_objs = ContractDetail_Reference_Aadharid.objects.filter(
								contractdetailid_fk = contractdetail.get(contractdetid = i[2]))
							print('previous date {0} skill_desi_detid {1} \
								get_existing_attdetail.skillcount {2}'.format(
									dateX,i,attcapture_obj.skillcount))
							if all_aadhaar_list_objs.count() > 0:
								all_aadhaar_list = [str(i.aadhaarid) for i in all_aadhaar_list_objs]
								count = 0
								for betterplace_emp in vendor_att_dict['employeeData']:
									if betterplace_emp['govtId'] in all_aadhaar_list:
										print('matchid {0}'.format(betterplace_emp['govtId']))
										count += 1
								attcapture_obj.skillcount = int(float(count))
							else:
								attcapture_obj.skillcount = 0
								# attcapture_obj.skillcount = int(float(vendor_att_dict['regManDays']))
							print('final count {0}'.format(attcapture_obj.skillcount))
							attcapture_obj.skillotcount =  int(float(vendor_att_dict['totalOTHrs']))
							attcapture_obj.extrashift = int(0)
							attcapture_obj.save()
						print('Data Inserted Successfully')
						break
	except:
		print('No job function map')
		pass


def betterplace_att_capt_new_expose(siteid,contractid,date1):
	from contract.models import DetailAttCapture,Designation,Contract,ContractDetail,SkillLevel
	from account.models import BA,UserLocationCustomer
	from location.models import OperationLocation
	import json
	import urllib.request
	import time
	from datetime import datetime
	# att_url = "https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getRecordSiteVendor?vendor={0}&siteId={1}&startDate={2}&endDate={3}".format(vendorid,siteid,date1,date1)
	date1 = str(datetime.today().date())
	date1_str = date1.split('-')
	date1 = date1_str[2]+'-'+date1_str[1]+'-'+date1_str[0]
	siteid = siteid
	apiKey = "Zsj0+CkJJck1e8fwe1L20Zxpu1pbsnWu/7V16dHBdEir63N6tiiU4ozRi3qBGd6ZBeZaS1EL8bkvtOML6tT1xw=="
	att_url = "https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getAttendanceRecordsForSiteVendorBased?siteId={0}&startDate={1}&endDate={2}".format(siteid,date1,date1)
	req1 = urllib.request.Request(att_url)
	req1.add_header('apikey',apiKey)

	recordsitevendor_dict = urllib.request.urlopen(req1).read()
	time.sleep(5)
	recordsitevendor_dict = str(recordsitevendor_dict,'utf-8')

	recordsitevendor_json = json.loads(recordsitevendor_dict)

	recordsitevendor_data = recordsitevendor_json['data']

	find_customer_ba_contract = Contract.objects.all()
	# find_cust_contract = find_customer_ba_contract.get(contractwith = "0", betterpalcesiteid = siteid)
	# contractid = find_cust_contract.contractid
	contractid = contractid

	if recordsitevendor_data['attendanceVendorsforSite'] is not None:
		print('siteid - {0} * attdata - {1}'.format(siteid,recordsitevendor_data['attendanceVendorsforSite']))
		# get conntract detail data
		contractdetail = ContractDetail.objects.filter(contract = contractid)
		skill_list = [i[0] for i in contractdetail.values_list('skilllevel')]
		designation_list = [i[0] for i in contractdetail.values_list('designation')]
		zip_of_skill_designation = [i for i in zip(skill_list,designation_list)]
		for att_dict in recordsitevendor_data['attendanceVendorsforSite']:
			# import pdb;pdb.set_trace()
			print('job funct **** {0}'.format(att_dict['attendanceVendorNameFunList']))
			for i in att_dict['attendanceVendorNameFunList']: print(i['attendanceJobRoleList'])
			try:
				for vendor_att_dict_list in att_dict['attendanceVendorNameFunList']:
					print("vendor Name --->",vendor_att_dict_list['vendorName'])
					for vendor_att_dict in vendor_att_dict_list['attendanceJobRoleList']:
						job_function = Designation.objects.get(designation_name = vendor_att_dict['jobfunction']) #designation_id , designation_name
						for i in zip_of_skill_designation:
							if i[1] == job_function.designation_id:
								try:
									get_existing_attdetail = DetailAttCapture.objects.get(contractid= contractid,date= date1,skillid= i[0],designation= i[1])
									get_existing_attdetail.skillcount = int(float(vendor_att_dict['regManDays']))
									get_existing_attdetail.skillotcount =  int(float(vendor_att_dict['totalOTHrs']))
									get_existing_attdetail.extrashift = int(0)
									# get_existing_attdetail.save()
								except:
									print('Not Exist')
									attcapture_obj = DetailAttCapture()
									attcapture_obj.contractid = Contract.objects.get(contractid = contractid)
									attcapture_obj.date = date1
									attcapture_obj.skillid = SkillLevel.objects.get(skillid = i[0])# skillid , skillname
									attcapture_obj.designation = Designation.objects.get(designation_id = i[1]) #designation_id , designation_name
									attcapture_obj.skillcount = int(float(vendor_att_dict['regManDays']))
									attcapture_obj.skillotcount =  int(float(vendor_att_dict['totalOTHrs']))
									attcapture_obj.extrashift = int(0)
									# attcapture_obj.save()
								print('Data Inserted Successfully')
								break
			except:
				print('No job function map')
				pass

class VerticalView(viewsets.ModelViewSet):
	"""
		Get vertical
		Perform Add, Update, Delete operation
	"""
	queryset = Vertical.objects.all()
	serializer_class = VerticalSerializers

	def create(self, request, format=None):
		serializer = VerticalSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)



class KPICategoryView(viewsets.ModelViewSet):
	"""
		Get KPICategory
		Perform Add, Update, Delete operation
	"""
	queryset = KPICategory.objects.all()
	serializer_class = KPICategorySerializer

	def create(self, request, format=None):
		serializer = KPICategorySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class KPIView(viewsets.ModelViewSet):
	"""
		Get KPI
		Perform Add, Update, Delete operation
	"""
	queryset = KPI.objects.all()
	serializer_class = KPISerializer


	def create(self, request, format=None):
		serializer = KPISerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class KPIFrequencyView(viewsets.ModelViewSet):
	"""
		Get KPIDetail
		Perform Add, Update, Delete operation
	"""
	queryset = KPIFrequency.objects.all()
	serializer_class = KPIFrequencySerializer

	def create(self, request, format=None):
		serializer = KPIFrequencySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


	def getkpiFrequency(self, request, *args, **kwargs):
		"""
		Get Contract detail using contractid
		"""
		getkpifrequency = self.kwargs['contractid']
		kpi_frequency = KPIFrequency.objects.filter(contract = getkpifrequency)

		serializer = KPIFrequencySerializer(kpi_frequency, many=True)
		return Response(serializer.data)

	def kpiFrequencyCapture(self, request, *args, **kwargs):
		"""
		Capture contractdetail from JSON
		"""
		jsonData = request.data
		contractid = jsonData['contractid']
		kpifrequencylist = jsonData['kpifrequencylist']
		# import pdb;pdb.set_trace()
		for dt in kpifrequencylist:
			try:
				dt['contract'] = Contract.objects.get(contractid = contractid)
				dt['kpi'] = KPI.objects.get(kpiCode = dt['kpi'])
				if 'kpifreqid' in dt.keys():
					kpifrequency = KPIFrequency.objects.filter(kpifreqid = dt['kpifreqid'])
					kpifrequency.update(**dt)
				else:
					dtlist = KPIFrequency(**dt)
					dtlist.save()

			except Exception as e:
				return Response([str(e)],status=status.HTTP_400_BAD_REQUEST)
		return Response(status=status.HTTP_201_CREATED)


class KPIDetailView(viewsets.ModelViewSet):
	"""
		Get KPIDetail
		Perform Add, Update, Delete operation
	"""
	queryset = KPIDetail.objects.all()
	serializer_class = KPIDetailSerializer


	def create(self, request, format=None):
		serializer = KPIDetailSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


	def getkpiDetail(self, request, *args, **kwargs):
		"""
		Get Contract detail using contractid
		"""
		getkpidetail = self.kwargs['contractid']
		kpi_detail = KPIDetail.objects.filter(contract = getkpidetail)

		serializer = KPIDetailSerializer(kpi_detail, many=True)
		return Response(serializer.data)

	def kpiDetailCapture(self, request, *args, **kwargs):
		"""
		Capture contractdetail from JSON
		"""
		jsonData = request.data
		contractid = jsonData['contractid']
		kpidetaillist = jsonData['kpidetaillist']
		# import pdb;pdb.set_trace()
		for dt in kpidetaillist:
			try:
				dt['contract'] = Contract.objects.get(contractid = contractid)
				dt['kpi'] = KPI.objects.get(kpiCode = dt['kpi'])
				if 'kpidetid' in dt.keys():
					kpidetail = KPIDetail.objects.filter(kpidetid = dt['kpidetid'])
					kpidetail.update(**dt)
				else:
					dtlist = KPIDetail(**dt)
					dtlist.save()

			except Exception as e:
				return Response([str(e)],status=status.HTTP_400_BAD_REQUEST)
		return Response(status=status.HTTP_201_CREATED)


	def kpiDetailExcelCapture(self, request, *args, **kwargs):
		"""
		Capture contractdetail from JSON
		"""
		# import pdb;pdb.set_trace()
		from django.db.models import Q
		jsonData = request.data
		contractid = jsonData['contractid']
		exceldata = jsonData['exceldata']
		kpicode = jsonData['kpicode']
		startdate = jsonData['start_date'].split('T')[0]
		enddate = jsonData['end_date'].split('T')[0]
		# import pdb;pdb.set_trace()
		det_objs = KPIDetail.objects.filter(Q(contract = contractid) & Q(targetdate__gte = startdate) & Q(targetdate__lte=enddate))
		# count = 0
		if det_objs:
			det_objs.delete()
		if det_objs.count() == 0:
			for key, value in exceldata.items():
				if key != 'kpiCode':
					try:
						det_obj = {}
						det_obj['contract'] = Contract.objects.get(contractid = contractid)
						det_obj['kpi'] = KPI.objects.get(kpiCode = kpicode)
						det_obj['targetdate'] = key.replace('/','-')
						det_obj['target1'] = value
						# if 'kpidetid' in dt.keys():
						# 	kpidetail = KPIDetail.objects.filter(kpidetid = dt['kpidetid'])
						# 	kpidetail.update(**dt)
						# else:
						dtlist = KPIDetail(**det_obj)
						dtlist.save()

					except Exception as e:
						return Response([str(e)],status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({'msg': 'Data Already Exist no new insertion'})
		return Response(status=status.HTTP_201_CREATED)


class Capture_Daily_KPIView(viewsets.ModelViewSet):
	"""
		Get Capture_Daily_KPI
		Perform Add, Update, Delete operation
	"""
	queryset = Capture_Daily_KPI.objects.all()
	serializer_class = Capture_Daily_KPISerializer


	def create(self, request, format=None):
		serializer = Capture_Daily_KPISerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


	def getdailykpiDetail(self, request, *args, **kwargs):
		"""
		Get Attendance detail using contractid and date
		where date format should be yyyy-mm-dd format
		"""
		contractid = self.kwargs['contractid']
		date_att = self.kwargs['date_att']

		daily_kpi_detail = Capture_Daily_KPI.objects.filter(contractid = contractid, date = date_att)
		serializer = Capture_Daily_KPISerializer(daily_kpi_detail, many=True)
		return Response(serializer.data)


	def getkpiGraphApi(self, request, *args, **kwargs):
		"""
		Get Attendance detail using contractid and date
		where date format should be yyyy-mm-dd format
		"""
		from datetime import datetime, timedelta
		from contract.models import KPIFrequency
		from contract.models import KPIDetail
		from django.db.models import Q, Sum
		from dateutil import relativedelta

		# import pdb;pdb.set_trace()
		contractid = self.kwargs['contractid']
		kpiCode = self.kwargs['kpicode']
		kpifreq = KPIFrequency.objects.filter(contract = contractid, kpi = kpiCode)
		graphApiList = []
		if kpifreq:
			if kpifreq.count() == 1:
				if kpifreq[0].inputfrequency == 'day' and kpifreq[0].outputfrequency == 'month':
					kpidetail_objs = KPIDetail.objects.filter(contract = contractid, kpi = kpiCode).order_by()
					dailykpi_objs = Capture_Daily_KPI.objects.filter(contractid = contractid, kpiid = kpiCode).order_by()
					for kpidetail_obj in kpidetail_objs:
						enddate = kpidetail_obj.targetdate + relativedelta.relativedelta(months=+1)
						enddate = enddate + timedelta(days=-1)
						startdate = kpidetail_obj.targetdate
						targetvalue = kpidetail_obj.target1
						actualcount = dailykpi_objs.filter(Q(date__gte = startdate) & Q(date__lte = enddate)).aggregate(actualtargate=Sum('actualcount'))
						actualcount = actualcount['actualtargate']
						if actualcount == None:
							actualcount = 0
						graphApiList.append({'date':startdate,'targatevalue':targetvalue,'actualcount':actualcount})
		# serializer = Capture_Daily_KPISerializer(daily_kpi_detail, many=True)
		if len(graphApiList) == 0:
			return Response([{'date':'1999-01-01','targatevalue':0,'actualcount':0}])
		return Response(graphApiList)

	def dailykpiCapture(self, request, *args, **kwargs):
		"""
		Capture attendance of contract from JSON
		"""
		jsonData = request.data
		contractid = jsonData['contractid']
		dailykpilist = jsonData['dailykpilist']
		for dt in dailykpilist:
			try:
				dt['contractid'] = Contract.objects.get(contractid = contractid)
				dt['kpiid'] = KPI.objects.get(kpiCode = dt['kpiid'])
				if 'id' in dt.keys():
					try:
						dailykpidetail = Capture_Daily_KPI.objects.get(id = dt['id'], date = dt['date'])
						dailykpidetail.actualcount = dt['actualcount']
						# if dailykpidetail.count() > 0:
						dailykpidetail.save()
					except:
						dtlist = Capture_Daily_KPI(**dt)
						dtlist.save()
				else:
					dtlist = Capture_Daily_KPI(**dt)
					dtlist.save()
			except Exception as e:
				return Response([str(e)],status=status.HTTP_400_BAD_REQUEST)
		return Response(status=status.HTTP_201_CREATED)


class InvoiceMasterView(viewsets.ModelViewSet):
	"""
		Get Capture_Daily_KPI
		Perform Add, Update, Delete operation
	"""
	queryset = InvoiceMaster.objects.all()
	serializer_class = InvoiceMasterSerializer

	# def create(self, request, format=None):
	# 	serializer = InvoiceMasterSerializer(data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	msg = []
	# 	if serializer.errors:
	# 		for k,v in serializer.errors.items():
	# 			msg.append(v)
	# 	return Response(msg, status=status.HTTP_400_BAD_REQUEST)

	def createInvoiceMaster_basedonpercentage(self, request, *args, **kwargs):
		"""
		Capture contractdetail from JSON
		"""
		jsonData = request.data
		invoiceid = jsonData['invoiceid']
		contractid = jsonData['contractid']
		finaltotal = jsonData['finaltotal']
		selectedrowids = jsonData['selectedrowids']

		from datetime import datetime

		con_per_field_objs = Contract_Percentage_Field.objects.filter(contract = contractid)
		rowidslist = selectedrowids.split('-')
		for i in rowidslist:
			try:
				inv_det_capt_obj = InvoiceDetailCapture.objects.get(id = i)
				inv_det_capt_obj.rowInvoiceFlag = 1
				inv_det_capt_obj.save()
			except Exception as e:
				return Response([str(e)],status=status.HTTP_400_BAD_REQUEST)
		list_invoice = []
		try:
			contract_obj = Contract.objects.get(contractid = contractid)
			if con_per_field_objs.count() > 0:
				for con_per_field_obj in con_per_field_objs:
					invoice_master_obj_new = InvoiceMaster()

					invoice_master_obj_new.invoiceid = invoiceid+str("_{0}_{1}".format(con_per_field_obj.city,con_per_field_obj.state))
					invoice_master_obj_new.contractid = contract_obj
					invoice_master_obj_new.finaltotal = (finaltotal * con_per_field_obj.percentage) / 100
					invoice_master_obj_new.state = con_per_field_obj.state
					invoice_master_obj_new.city = con_per_field_obj.city
					invoice_master_obj_new.selectedrowids = selectedrowids
					invoice_master_obj_new.save()
					list_invoice.append(invoice_master_obj_new.invoiceid)

		except Exception as e:
			return Response([str(e)],status=status.HTTP_400_BAD_REQUEST)
		return Response([list_invoice],status=status.HTTP_201_CREATED)


	def getInvoiceDetailCaptureRow(self, request, *args, **kwargs):

		from contract.models import InvoiceDetailCapture
		from contract.serializers import InvoiceDetailCaptureSerializer

		rowids = self.kwargs['rowids']
		rowidslist = rowids.split('-')

		# invoice_id = InvoiceMaster.objects.get(invoiceid = invoiceid)
		invoicedetailcapture_detail = InvoiceDetailCapture.objects.filter(id__in = rowidslist)

		serializer = InvoiceDetailCaptureSerializer(invoicedetailcapture_detail, many=True)
		return Response(serializer.data)

	def getInvoiceAnnextureDetailRow(self, request, *args, **kwargs):


		from contract.models import InvoiceDetailCapture
		from contract.serializers import InvoiceDetailCaptureSerializer
		# import pdb;pdb.set_trace()

		invoicemasterid = self.kwargs['invoicemasterid']

		try:
			invoicemaster_obj = InvoiceMaster.objects.get(invoiceid = invoicemasterid)
			rowidslist = (invoicemaster_obj.selectedrowids).split('-')
			invoicedetailcapture_detail = InvoiceDetailCapture.objects.filter(id__in = rowidslist)
		except:
			pass
		# invoice_id = InvoiceMaster.objects.get(invoiceid = invoiceid)

		serializer = InvoiceDetailCaptureSerializer(invoicedetailcapture_detail, many=True)
		return Response(serializer.data)


class AdditionalChargesView(viewsets.ModelViewSet):
	"""
		Get Capture_Daily_KPI
		Perform Add, Update, Delete operation
	"""
	queryset = AdditionalCharges.objects.all()
	serializer_class = AdditionalChargesSerializer

	def create(self, request, format=None):
		serializer = AdditionalChargesSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)

	def getAdditionalChargesDetail(self, request, *args, **kwargs):
		"""
		Get Contract detail using contractid
		"""
		# import pdb;pdb.set_trace()
		invoiceid = self.kwargs['invoiceid']
		invoice_id = InvoiceMaster.objects.get(invoiceid = invoiceid)
		additionalcharges_detail = AdditionalCharges.objects.filter(invoiceid = invoice_id)

		serializer = AdditionalChargesSerializer(additionalcharges_detail, many=True)
		return Response(serializer.data)

	def additionalchargesCapture(self, request, *args, **kwargs):
		"""
		Capture contractdetail from JSON
		"""
		jsonData = request.data
		invoiceid_list = jsonData['invoiceid']
		additionalchargeslist = jsonData['additionalchargeslist']
		for invoiceid in invoiceid_list[0]:
			for at in additionalchargeslist:
				try:
					at['invoiceid'] = InvoiceMaster.objects.get(invoiceid = invoiceid)

					if 'id' in at.keys():
						contractdetail = AdditionalCharges.objects.filter(id = at['id'])
						contractdetail.update(**at)
					else:
						dtlist = AdditionalCharges(**at)
						dtlist.save()

				except Exception as e:
					return Response([str(e)],status=status.HTTP_400_BAD_REQUEST)
		return Response(status=status.HTTP_201_CREATED)


class InvoiceHeaderMasterView(viewsets.ModelViewSet):
	"""
		Get Capture_Daily_KPI
		Perform Add, Update, Delete operation
	"""
	queryset = InvoiceHeaderMaster.objects.all()
	serializer_class = InvoiceHeaderMasterSerializer

	def create(self, request, format=None):
		serializer = InvoiceHeaderMasterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)
