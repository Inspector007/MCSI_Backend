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
from .models import State,City,OperationLocation,LabourCost_State_IndustryWise,\
	Invoice_Header_Location
from . serializers import StateSerializers,CitySerializers,\
		OperationLocationSerializers,LabourCost_State_IndustryWiseSerializers,\
		Invoice_Header_LocationSerializers
from iscm.utility import find_user_locationlist


# Create your views here.

class StateView(viewsets.ModelViewSet):
	"""
		State API example 'Maharashtra','Gujrat','Uttar pradesh'
		Perform Add, Update, Delete operation 
	"""
	queryset = State.objects.all()
	serializer_class = StateSerializers


class LabourCost_State_IndustryWiseView(viewsets.ModelViewSet):
	"""
		Labour Cost API for industrywise cost filtering example 'Maharashtra','Gujrat','Uttar pradesh'
		Perform Add, Update, Delete operation 
	"""
	queryset = LabourCost_State_IndustryWise.objects.all()
	serializer_class = LabourCost_State_IndustryWiseSerializers

	def create(self, request, format=None):
		serializer = LabourCost_State_IndustryWiseSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


	def getIndustryName(self, request, *args, **kwargs):
		allIndustryName = self.queryset.values_list('industryType')
		IndustryList = set([i[0] for i in allIndustryName])
		return Response(IndustryList)

	def getLabourCostIndustryWise(self, request, *args, **kwargs):
		industryName = self.kwargs['industryname']
		# stateName = self.kwargs['statename']
		getstatelabourcost = self.queryset.filter(industryType = industryName)
		serializer = self.serializer_class(getstatelabourcost, many=True)
		return Response(serializer.data)


class CityView(viewsets.ModelViewSet):
	"""
		City API example 'Mumbai','Ahnadabad','Lucknow' 
		Perform Add, Update, Delete operation 
	"""
	queryset = City.objects.all()
	serializer_class = CitySerializers

	def create(self, request, format=None):
		serializer = CitySerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


	def listcity(self,request,*args, **kwargs):
		stateid = self.kwargs['stateid']
		getcity = self.queryset.filter(citystate = stateid)
		serializer = self.serializer_class(getcity, many=True)
		return Response(serializer.data)

class Invoice_Header_LocationView(viewsets.ModelViewSet):
	"""
		City API example 'Mumbai','Ahnadabad','Lucknow' 
		Perform Add, Update, Delete operation 
	"""
	queryset = Invoice_Header_Location.objects.all()
	serializer_class = Invoice_Header_LocationSerializers

	def create(self, request, format=None):
		serializer = Invoice_Header_LocationSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)


	def get_pan_gstinno_list(self,request,*args, **kwargs):
		from contract.models import Contract
		jsonData = request.data
		contractid = jsonData['contractid']
		invoiceid = jsonData['invoiceid']

		invoiceid_list = invoiceid.split('_')
		city = invoiceid_list[1]
		state = invoiceid_list[2]
		# import pdb;pdb.set_trace()
		contract_obj = Contract.objects.get(contractid = contractid)
		customer_name = contract_obj.customer.custname
		getcity = self.queryset.filter(custname = customer_name,locstate=state,loccity=city)

		serializer = self.serializer_class(getcity, many=True)
		return Response(serializer.data)

	# # def create(self, request, *args, **kwargs):
	# # 	userid = request.META['QUERY_STRING'].split('-')[1].strip(' 	')
	# # 	print('rolename aaya- {0} -- userid {1}'.format(request.META['QUERY_STRING'],userid))
	# # 	import pdb;pdb.set_trace()
	# # 	serializer = self.get_serializer(data=request.DATA, 
	# # 									 files=request.FILES)
	# # 	return Response(serializer.data, status=status.HTTP_201_CREATED,
	# # 						headers=headers)
	# def perform_create(self, serializer):
	# 	# import pdb;pdb.set_trace()
	# 	userid = self.request.META['QUERY_STRING'].split('-')[1].strip(' 	')
	# 	serializer.save(createdby=userid)

	# def update(self, request, pk=None):
	# 	# import pdb;pdb.set_trace()
	# 	from location.models import State
	# 	userid = self.request.META['QUERY_STRING'].split('-')[1].strip(' 	')
	# 	queryset = self.queryset.get(cityid = pk)
	# 	queryset.updatedby = userid
	# 	print('user id -- {0} --- {1}'.format(userid, queryset.updatedby))
	# 	queryset.cityid = request.data['cityid']
	# 	queryset.citycode = request.data['citycode']
	# 	queryset.cityname = request.data['cityname']
	# 	queryset.citystate = State.objects.get(stateid = request.data['citystate'])
	# 	queryset.save()
	# 	# serializer = self.serializer_class(instance=queryset,data=request.data)
	# 	serializer = self.serializer_class(queryset)
	# 	return Response(serializer.data)

	# 	# # serializer.is_valid(raise_exception=True)
	# 	return Response(serializer.data)


class OperationLocationView(viewsets.ModelViewSet):
	"""
		Operation Location API Example 'Malad','Goregaon','AHM1' etc. 
		Perform Add, Update, Delete operation 
	"""
	queryset = OperationLocation.objects.all()
	serializer_class = OperationLocationSerializers

	
	def create(self, request, format=None):
		serializer = OperationLocationSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		msg = []
		if serializer.errors:
			for k,v in serializer.errors.items():
				msg.append(v)
		return Response(msg, status=status.HTTP_400_BAD_REQUEST)

	def getsitedata(self,request,*args,**kwargs):
		import json
		# import os
		# from iscm.settings import strOpplink
		import urllib.request

		# strOpplink = strOpplink
		# if strOpplink == "http://103.81.89.7/cashAPI/api/APIOpportunityDetails?Opp_id={0}&ApiKey=superapi00000":
		siteid_url = "https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getSiteIDNames"
		apikey = 'Zsj0+CkJJck1e8fwe1L20Zxpu1pbsnWu/7V16dHBdEir63N6tiiU4ozRi3qBGd6ZBeZaS1EL8bkvtOML6tT1xw=='
		headers = {'apikey' : apikey }
		req = urllib.request.Request(siteid_url)
		req.add_header('apikey',apikey)
		siteidlist_dict = urllib.request.urlopen(req).read()
		siteidlist_dict = str(siteidlist_dict,'utf-8')
		
		# import pdb;pdb.set_trace()
		siteid_json = json.loads(siteidlist_dict)
		siteid_data = siteid_json['data']['listofSites']

		return Response(siteid_data)


	def getsiteiddata(self,request,*args,**kwargs):
		import json
		# import os
		# from iscm.settings import strOpplink
		import urllib.request
		siteid = self.kwargs['siteid']

		# strOpplink = strOpplink
		# if strOpplink == "http://103.81.89.7/cashAPI/api/APIOpportunityDetails?Opp_id={0}&ApiKey=superapi00000":
		siteid_url = "https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getSiteIDNames"
		apikey = 'Zsj0+CkJJck1e8fwe1L20Zxpu1pbsnWu/7V16dHBdEir63N6tiiU4ozRi3qBGd6ZBeZaS1EL8bkvtOML6tT1xw=='
		headers = {'apikey' : apikey }
		req = urllib.request.Request(siteid_url)
		req.add_header('apikey',apikey)
		siteidlist_dict = urllib.request.urlopen(req).read()
		siteidlist_dict = str(siteidlist_dict,'utf-8')
		
		# import pdb;pdb.set_trace()
		siteid_json = json.loads(siteidlist_dict)
		siteid_data = siteid_json['data']['listofSites']
		# import pdb;pdb.set_trace()
		filter_siteid_list = []
		print('before count {0}'.format(len(siteid_data)))
		oploc_serializer_data = OperationLocation.objects.all().values_list('betterplace_siteid')
		siteid_List = set([i[0] for i in oploc_serializer_data])
		if siteid == '0000':
			for i in siteid_data:
				if i['siteId'] not in siteid_List:
					filter_siteid_list.append(i)
		else:
			for i in siteid_data:
				if i['siteId'] not in siteid_List or i['siteId'] == siteid:
					filter_siteid_list.append(i)

		print('after count {0}'.format(len(filter_siteid_list)))

		# if opportunityjson['status'] == 'S' and opportunityjson['error'] == '':
		return Response(filter_siteid_list)


	# def create(self, request, *args, **kwargs):
	# 	userid = request.META['QUERY_STRING'].split('-')[1].strip(' 	')
	# 	print('rolename aaya- {0} -- userid {1}'.format(request.META['QUERY_STRING'],userid))
	# 	import pdb;pdb.set_trace()
	# 	serializer = self.get_serializer(data=request.DATA, 
	# 									 files=request.FILES)
	# 	return Response(serializer.data, status=status.HTTP_201_CREATED,
	# 						headers=headers)
	# def perform_create(self, serializer):
	# 	import pdb;pdb.set_trace()
	# 	serializer.save()

	def oploc_filter(self, request):
		userid = request.META['QUERY_STRING']
		print('list me aaya rolename- {0} -- userid {1}'.format(request.META['QUERY_STRING'],userid))
		locationlist = find_user_locationlist()
		# import pdb;pdb.set_trace()
		filter_queryset = self.queryset.filter(oplocationid__in = locationlist)
		serializer = self.serializer_class(filter_queryset, many=True)
		return Response(serializer.data)

	# def retrieve(self, request, pk=None):
	#     queryset = User.objects.all()
	#     user = get_object_or_404(queryset, pk=pk)
	#     serializer = UserSerializer(user)
	#     return Response(serializer.data)
	

	def vaayu_routing_response(self,request):
		import json
		from call_routing_api import routing_response
		with open('/home/administrator/Documents/ISCM2/iscm/routing_multi_emp.json') as json_file:
			data = json.load(json_file)

		routing_response_json = routing_response(data)
		

		return Response(routing_response_json)