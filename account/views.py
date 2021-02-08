from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import User,Access,UserAccess,Customer,CustomerMaster,\
		InternalOrders,BA,UserLocationCustomer
from . serializers import UserSerializers,AccessSerializers,\
		UserAccessSerializers,BASerializers,\
		CustomerSerializers,UserLocationCustomerSerializers,\
		CustomerMasterSerializers,InternalOrdersSerializers,\
		UserLoginSerializer

from django.contrib import admin
admin.autodiscover()

from rest_framework import generics, permissions, serializers
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
import json
from django.views.decorators.csrf import csrf_exempt
import requests
from iscm.middleware import *
# Create your views here.


@csrf_exempt
def account_login(request):
	if request.method == 'POST':
		print(request.body)
		data12 = {}
		login_dict = json.loads(str(request.body,'utf-8'))
		# login_dict = json.loads(request.body)
		username = login_dict['username']
		password = login_dict['password']
		# devicetype = request.POST['devicetype']
		devicetype = 'web'

		login_api_response = login_api(username,password,devicetype)
		if login_api_response["status"] == "success":
			return HttpResponse(json.dumps(login_api_response))
		else:
			return HttpResponse(json.dumps(login_api_response))
			# return HttpResponse(json.dumps('no record found'))
	else:
		return HttpResponse(json.dumps({"status":"Fail","userid":"","authToken":"","appid":"","deviceType":""}))


class UserLoginAPIView(APIView):
	"""
	Endpoint for user login. Returns authentication token on success.
	"""

	permission_classes = (permissions.AllowAny, )
	serializer_class = UserLoginSerializer

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid(raise_exception=True):
			return Response(serializer.data, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(viewsets.ModelViewSet):
	# permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	# permission_classes = (permissions.IsAuthenticated, )
	"""
		Get User data
		Perform Add, Update, Delete operation
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializers


	def create(self, request, format=None):
		serializer = UserSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)

	def sapuserlogin(self, request, *args, **kwargs):
		"""
		SAP USER login from JSON
		"""
		jsonData = request.data
		userid = jsonData['user']
		password = jsonData['password']
		companyname = "MAHINDRA LOGISTICS LTD"
		companycode = "MLL"
		jsondata_response = {}
		api_key = 'oFvyg2g1ffj9DkKw2fTtQZStzZd3hPYt02mF5qvtV9o=QfYSSaBLXdCrFkzqlKM2xGiOx8NF4eug/CtOwyyMBdA='
		try:
			sapuserobject = self.queryset.get(userid = userid)
			if sapuserobject:
				if password == sapuserobject.password:
					jsondata_response['user'] = {}
					jsondata_response['user']['UserName'] = userid
					jsondata_response['user']['Api_Key'] = api_key
					jsondata_response['user']['CompanyName'] = companyname
					jsondata_response['user']['CompanyCode'] = companycode
					# {
					# 	"user": {
					# 	"UserName": userid,
					# 	"Api_Key": "nEuxf2g1ffj9DkKw2fTtQZStzZd3hPYt02mF5qvtV9o=QfYSSaBLXdCrFkzqlKM2xGiOx8NF4eug/CtOwyyMBdA=",
					# 	"CompanyName": "MAHINDRA LOGISTICS LTD",
					# 	"CompanyCode": "MLL"
					# 	}
					# }	
					return HttpResponse(json.dumps(jsondata_response)		)
		except Exception as e:
			record = {}
			record['api_key'] = 'null'
			record['MSG_SNO'] = '400'
			record['MSG_TYP'] = 'E'
			record['MESSAGE'] = ''
			error1 = {
				"Key": "password",
				"Message": "The password field is required."
			}
			record['Validation'] = [error1]
			jsondata_response['Record'] = record
			return HttpResponse(json.dumps(jsondata_response))

		# 	{
		# 		"Record": {
		# 		"api_key": "null",
		# 		"MSG_SNO": "400",
		# 		"MSG_TYP": "E",
		# 		"MESSAGE": "",
		# 		"Validation": [
		# 		{
		# 			"Key": "password",
		# 			"Message": "The password field is required."
		# 		}
		# 			]
		# 		}
		# }
		# return Response(status=status.HTTP_201_CREATED)
	# def account_login(self, request):
	# 	API_ENDPOINT = "http://10.175.2.29:8080/login"
	# 	import pdb;pdb.set_trace()
	# 	if request.method == 'POST':
	# 		print(request.body)
	# 		data12 = {}
	# 		data12 = request.body
	# 		username = ''
	# 		password = ''
	# 		detvicetype = ''
	# 		data = {'username':username,
	# 				'password':password,
	# 				'detvicetype':detviceType,
	# 					}

	# 		response = requests.post(url = API_ENDPOINT, data = data)
	# 		valList = []
	# 		if len(valList) > 0:
	# 			return HttpResponse(json.dumps(valList))
	# 		else:
	# 			return HttpResponse(json.dumps('no record found'))
	# 	else:
	# 		return HttpResponse("error")



class AccessView(viewsets.ModelViewSet):
	"""
		Get Access type example HR, Commercial, admin
		Perform Add, Update, Delete operation
	"""
	# permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	# permission_classes = (permissions.IsAuthenticated, )
	queryset = Access.objects.all()
	serializer_class = AccessSerializers


	def create(self, request, format=None):
		serializer = AccessSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)



class UserAccessView(viewsets.ModelViewSet):
	"""
		Provide User access
		Perform Add, Update, Delete operation
	"""
	# permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	# permission_classes = (permissions.AllowAny, )
	queryset = UserAccess.objects.all()
	serializer_class = UserAccessSerializers


	def create(self, request, format=None):
		serializer = UserAccessSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class CustomerView(viewsets.ModelViewSet):
	"""
		Customer Example Amazon, Flipkart,
		Perform Add, Update, Delete operation
	"""
	# permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializers


	def create(self, request, format=None):
		serializer = CustomerSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class CustomerMasterView(viewsets.ModelViewSet):
	"""
		Customer Example Amazon, Flipkart,
		Perform Add, Update, Delete operation
	"""
	# permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset = CustomerMaster.objects.all()
	serializer_class = CustomerMasterSerializers


	def create(self, request, format=None):
		if request.data['Record']['MOB_NO'] == '' or request.data['Record']['MOB_NO'] == None:
			request.data['Record']['MOB_NO'] = '9999999999'
		serializer = CustomerMasterSerializers(data=request.data['Record'])
		if serializer.is_valid():
			serializer.save()
			json_response_data = {
			"Record": {
				"CUST_CODE": serializer.data['CUST_CODE'],
				"MSG_SNO": "200",
				"MSG_TYP": "S",
				"MESSAGE": "Your request completed successfully."
  				}
			}
			return Response(json_response_data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append({"Key" : k,"Message": v[0]})
			json_response_data = {
		  	"Record": {
				"CUST_CODE": serializer.data['CUST_CODE'],
				"MSG_SNO": "400",
				"MSG_TYP": "E",
				"MESSAGE": "Failed to process your request",		
				"Validation": msg,
			}
		}
		return Response(json_response_data, status=status.HTTP_400_BAD_REQUEST)


class InternalOrdersView(viewsets.ModelViewSet):
	"""
		Customer Example Amazon, Flipkart,
		Perform Add, Update, Delete operation
	"""
	# permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset = InternalOrders.objects.all()
	serializer_class = InternalOrdersSerializers


	def create(self, request, format=None):
		serializer = InternalOrdersSerializers(data=request.data['Record'])
		from account.models import orderdeliveryaddress
		intrnl_order = request.data['Record']['INTRNL_ORDR']
		get_order_del_address = orderdeliveryaddress.objects.filter(INTRNL_ORDR = intrnl_order)
		dlvr_address = request.data['Record']['DELVR_ADDRS']
		request.data['Record']['DELVR_ADDRS'] = ''
		if serializer.is_valid():
			serializer.save()
			get_intrnal_order_obj = self.queryset.get(INTRNL_ORDR = intrnl_order)
			if get_order_del_address.count() == 0:
				if len(dlvr_address) > 0:
					for d_address in dlvr_address:
						orderdeliveryaddress_obj = orderdeliveryaddress()		
						orderdeliveryaddress_obj.INTRNL_ORDR = get_intrnal_order_obj
						orderdeliveryaddress_obj.DELVR_ADDRS = d_address['DELIVERY_ADDRESS']
						orderdeliveryaddress_obj.PRIM_ADDRESS = d_address['PRIM_ADDRESS']		
						orderdeliveryaddress_obj.save()
			else:
				for i in get_order_del_address:
					i.delete()
				if len(dlvr_address) > 0:
					for d_address in dlvr_address:
						orderdeliveryaddress_obj = orderdeliveryaddress()		
						orderdeliveryaddress_obj.INTRNL_ORDR = get_intrnal_order_obj
						orderdeliveryaddress_obj.DELVR_ADDRS = d_address['DELIVERY_ADDRESS']
						orderdeliveryaddress_obj.PRIM_ADDRESS = d_address['PRIM_ADDRESS']		
						orderdeliveryaddress_obj.save()
			json_response_data = {
			"Record": {
				"INTRNL_ORDR": serializer.data['INTRNL_ORDR'],
				"MSG_SNO": "200",
				"MSG_TYP": "S",
				"MESSAGE": "Your request completed successfully."
  				}
			}
			return Response(json_response_data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append({"Key" : k,"Message": v[0]})
			json_response_data = {
		  	"Record": {
				"INTRNL_ORDR": serializer.data['INTRNL_ORDR'],
				"MSG_SNO": "400",
				"MSG_TYP": "E",
				"MESSAGE": "Failed to process your request",		
				"Validation": msg,
				}
			}
		return Response(json_response_data, status=status.HTTP_400_BAD_REQUEST)


class BAView(viewsets.ModelViewSet):
	"""
		BA(Business Associate) Example
		Perform Add, Update, Delete operation
	"""
	queryset = BA.objects.all()
	serializer_class = BASerializers


	def create(self, request, format=None):
		serializer = BASerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)

	def create_ba_from_baportal(self,request,*args,**kwargs):
		import json

	def get_betterplace_vendordata(self,request,*args,**kwargs):
		import json
		# import os
		# from iscm.settings import strOpplink
		import urllib.request
		vendorid = self.kwargs['vendorid']

		# strOpplink = strOpplink
		# if strOpplink == "http://103.81.89.7/cashAPI/api/APIOpportunityDetails?Opp_id={0}&ApiKey=superapi00000":
		vendorid_url = "https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getVendorIDNames"
		apikey = 'Zsj0+CkJJck1e8fwe1L20Zxpu1pbsnWu/7V16dHBdEir63N6tiiU4ozRi3qBGd6ZBeZaS1EL8bkvtOML6tT1xw=='
		headers = {'apikey' : apikey }
		req = urllib.request.Request(vendorid_url)
		req.add_header('apikey',apikey)
		vendorlist_dict = urllib.request.urlopen(req).read()
		vendorlist_dict = str(vendorlist_dict,'utf-8')

		# import pdb;pdb.set_trace()
		vendor_json = json.loads(vendorlist_dict)
		vendor_data = vendor_json['data']['listofVendors']
		# import pdb;pdb.set_trace()
		filter_vendor_list = []
		print('before count {0}'.format(len(vendor_data)))
		ba_serializer_data = BA.objects.all().values_list('bttrplce_vendorid')
		vendorid_List = set([i[0] for i in ba_serializer_data])
		if vendorid == '0000':
			for i in vendor_data:
				if i['vendorId'] not in vendorid_List:
					filter_vendor_list.append(i)
		else:
			for i in vendor_data:
				if i['vendorId'] not in vendorid_List or i['vendorId'] == vendorid:
					filter_vendor_list.append(i)

		print('after count {0}'.format(len(filter_vendor_list)))

		# if opportunityjson['status'] == 'S' and opportunityjson['error'] == '':
		return Response(filter_vendor_list)

	def get_vendor_onsite(self,request,*args,**kwargs):
		import json
		import urllib.request
		import time
		siteid = self.kwargs['siteid']
		apikey = 'Zsj0+CkJJck1e8fwe1L20Zxpu1pbsnWu/7V16dHBdEir63N6tiiU4ozRi3qBGd6ZBeZaS1EL8bkvtOML6tT1xw=='
		headers = {'apikey' : apikey }

		vendorid_url = "https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getVendorIDNames"
		req = urllib.request.Request(vendorid_url)
		req.add_header('apikey',apikey)
		vendorlist_dict = urllib.request.urlopen(req).read()
		vendorlist_dict = str(vendorlist_dict,'utf-8')

		# import pdb;pdb.set_trace()
		vendor_json = json.loads(vendorlist_dict)
		vendor_data = vendor_json['data']['listofVendors']
		filter_vendor_list = []
		#https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getRecordSiteVendor?vendor=10178163594610587744&siteId=16252173452509896464&startDate=05-08-2019&endDate=09-09-2019
		for i in vendor_data:
			print('vendorid - {0} - siteid - {1}'.format(i['vendorName'],siteid))
			att_url = "https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getRecordSiteVendor?vendor={0}&siteId={1}&startDate=05-08-2019&endDate=09-09-2019".format(i['vendorId'],siteid)
			req1 = urllib.request.Request(att_url)
			req1.add_header('apikey',apikey)
			recordsitevendor_dict = urllib.request.urlopen(req1).read()
			time.sleep(5)
			recordsitevendor_dict = str(recordsitevendor_dict,'utf-8')

			recordsitevendor_json = json.loads(recordsitevendor_dict)
			recordsitevendor_data = recordsitevendor_json['data']

			if recordsitevendor_data['attendanceDetails'] is not None:
				print('vendorid - {0} * siteid - {1} * attdata - {2}'.format(i['vendorName']\
					,siteid,recordsitevendor_data['attendanceDetails']))
				filter_vendor_list.append(recordsitevendor_data['vendor'])
			else:
				print('vendorid - {0} * siteid - {1} * attdata - {2}'.format(i['vendorName']\
					,siteid,recordsitevendor_data['attendanceDetails']))
				# filter_vendor_list.append(recordsitevendor_data['vendor'])


		# filter_vendor_list = vendor_list(apikey,vendor_data,siteid)

		return Response(filter_vendor_list)

def vendor_list(apikey,vendor_data,siteid):
	import json
	import urllib.request
	import time
	filter_vendor_list = []
	for i in vendor_data:
		print('vendorid - {0} - siteid - {1}'.format(i['vendorName'],siteid))
		att_url = "https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getRecordSiteVendor?vendor={0}8&siteId={1}&startDate=03-05-2019&endDate=30-07-2019".format(i['vendorId'],siteid)
		req1 = urllib.request.Request(att_url)
		req1.add_header('apikey',apikey)
		recordsitevendor_dict = urllib.request.urlopen(req1).read()
		time.sleep(10)
		recordsitevendor_dict = str(recordsitevendor_dict,'utf-8')

		recordsitevendor_json = json.loads(recordsitevendor_dict)
		recordsitevendor_data = recordsitevendor_json['data']

		if recordsitevendor_data['attendanceDetails'] is not None:
			print('vendorid - {0} * siteid - {1} * attdata - {2}'.format(i['vendorName']\
				,siteid,recordsitevendor_data['attendanceDetails']))
			filter_vendor_list.append(recordsitevendor_data['vendor'])
		else:
			pass

	return filter_vendor_list


class UserLocationCustomerView(viewsets.ModelViewSet):
	queryset = UserLocationCustomer.objects.all()
	serializer_class = UserLocationCustomerSerializers


	def create(self, request, format=None):
		serializer = UserLocationCustomerSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


	def customeratlocation(self,request,*args,**kwargs):
		"""
		API to find Customer at given location
		Provide locationid to locid parameter
		"""
		locationid = self.kwargs['locid']
		location = self.queryset.filter(location=locationid)
		serializer = UserLocationCustomerSerializers(location,many=True)
		return Response(serializer.data)

	def customerslocation(self, request, *args, **kwargs):
		"""
		API to find customers all location
		Provide customerid to custid parameter
		"""
		from location.models import OperationLocation
		from location.serializers import OperationLocationSerializers
		from iscm.utility import find_user_locationlist

		customerid = self.kwargs['custid']
		userid = request.META['QUERY_STRING']
		# print('list me aaya rolename- {0} -- userid {1}'.format(request.META['QUERY_STRING'],userid))
		locationlist = find_user_locationlist()

		# customer = self.queryset.filter(customer=customerid)
		# loc_id = self.queryset.filter(customer=customerid).values_list('location',flat=True)
		# loc_id = self.queryset.all().values_list('location',flat=True)
		location = OperationLocation.objects.filter(oplocationid__in = locationlist)
		serializer = OperationLocationSerializers(location,many=True)
		return Response(serializer.data)
