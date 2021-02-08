from django.shortcuts import render
from rest_framework import serializers
from .models import State,City,OperationLocation,\
	LabourCost_State_IndustryWise,Invoice_Header_Location

class StateSerializers(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('stateid','statecode','statename','statecountry','skilled_labour_cost',\
            'unskilled_labour_cost','semiskilled_labour_cost','lat','lng')

class LabourCost_State_IndustryWiseSerializers(serializers.ModelSerializer):

    class Meta:
        model = LabourCost_State_IndustryWise
        fields = ('id','statecode','statename','statecountry','skilled_labour_cost',\
        	'unskilled_labour_cost','semiskilled_labour_cost','lat','lng','industryType','cityname')


class CitySerializers(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('cityid','citycode','cityname','citystate')
        

class OperationLocationSerializers(serializers.ModelSerializer):

    class Meta:
        model = OperationLocation
        fields = ('oplocationid','betterplace_siteid','betterplace_sitename','oploccode','oploclat','oploclong','oplocaddress','oploccity')


class Invoice_Header_LocationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Invoice_Header_Location
        fields = ('locationid','custname','loccode','gstin_no','pan_no','locaddress','locstate','loccity')