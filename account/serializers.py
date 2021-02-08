from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import serializers
from .models import User,Access,UserAccess,Customer,\
    CustomerMaster,InternalOrders,BA,UserLocationCustomer
from django.contrib import admin
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q
from django.conf import settings
from rest_framework import serializers
from rest_framework.authtoken.models import Token


admin.autodiscover()

from rest_framework import generics, permissions, serializers

#from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
DUser = get_user_model()

class UserLoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        required=False,
        allow_blank=True,
        write_only=True,
    )

    email = serializers.EmailField(
        required=False,
        allow_blank=True,
        write_only=True,
        label="Email Address"
    )

    token = serializers.CharField(
        allow_blank=True,
        read_only=True
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta(object):
        model = DUser
        fields = ['email', 'username', 'password', 'token']

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password', None)

        if not email and not username:
            raise serializers.ValidationError("Please enter username or email to login.")

        user = DUser.objects.filter(
            Q(email=email) | Q(username=username)
        ).exclude(
            email__isnull=True
        ).exclude(
            email__iexact=''
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("This username/email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Invalid credentials.")

        if user_obj.is_active:
            import pdb;pdb.set_trace()
            token, created = Token.objects.get_or_create(user=user_obj)
            data['token'] = token
        else:
            raise serializers.ValidationError("User not active.")

        return data


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('userid','firstname','lastname','mobileno','worklocation')

class AccessSerializers(serializers.ModelSerializer):

    class Meta:
        model = Access
        fields = ('accessid','accname','accdescription')


class UserAccessSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserAccess
        fields = ('id','user','access','location')


class CustomerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('custid','custcode','custname','custcontactname','email','status')


class CustomerMasterSerializers(serializers.ModelSerializer):

    class Meta:
        model = CustomerMaster
        fields =('CUST_CODE','EVENT','GRP_BP','NAME','NAME_2',\
            'CARE_OF','STREET','STREET_4','STREET_5','DIST',\
            'PO_CODE','CITY','COUNTRY','REGION','MOB_NO',\
            'CONTCT_PRSN','EMAIL','EXTR_BP','EXTR_ADRS',\
            'TAX_CAT','TAX_NUM','CUST_CLS','LUT_NUM',\
            'LTA_NUM','PAN','GRP_KEY','INDSTRY_CODE',\
            'CO_CODE','INDUSTRY','RECON_GL','PYMT_TRM',\
            'NOT_RELSD','CUST_BLK')


class InternalOrdersSerializers(serializers.ModelSerializer):

    class Meta:
        model = InternalOrders
        fields = ('INTRNL_ORDR','EVENT','CONTRL_AREA',\
            'ORDR_TYPE','INTRNL_ORDR_DESCR','CO_CODE',\
            'PRFT_CNTR','PRSN_RESPNSBL','HARMONY_IO',\
            'ACT_ASG','CUSTOMER','ACVTY','CLUSTER',\
            'BRANCH','GROUP_INT','TAX_CLASSIFICATION',\
            'NETWORK_IND','OPPORTUNITY_ID','SUB_ACVTY',\
            'SCD_VERTICAL','LOCATION','STATUS','CUST_PAN',\
            'CUST_GRP','ORDR_CTGRY','PLANT','STATISTICAL',\
            'COST_CNTR','BUSNS_SEGMNT','PRM_VERTICAL',\
            'INDUSTRY','GROUP_EXT','CUSTOMER_ENTITY',\
            'CUSTOMER_STATE','IDT_OP_SERVICE_CLASS',\
            'DELVR_ADDRS','CREATED_DATE','UPDATED_DATE')

class BASerializers(serializers.ModelSerializer):

    class Meta:
        model = BA
        fields = ('baid','bttrplce_vendorid','bttrplce_vendorname','bacode','baname','bacontactname','email','status')


class UserLocationCustomerSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserLocationCustomer
        fields = ('ulcpkey','location','user')#'customer'