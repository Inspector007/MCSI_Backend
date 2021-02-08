from django.shortcuts import render
from rest_framework import serializers
from .models import ContractType,RateType,SkillLevel,Designation,\
    Contract,ContractDetail,Document,DetailAttCapture,Vertical,KPICategory,\
    KPI,KPIFrequency,KPIDetail,Capture_Daily_KPI,InvoiceMaster,\
    AdditionalCharges,InvoiceHeaderMaster,InvoiceDetailCapture,AdditionalContractField,\
    Contract_Percentage_Field

class ContractTypeSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ContractType
        fields = ('contracttypeid','url','cnttypename','cnttypecode')

class RateTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = RateType
        fields = ('ratetypeid','ratetypename','ratetypecode','contracttypeid')

class SkillLevelSerializers(serializers.ModelSerializer):

    class Meta:
        model = SkillLevel
        fields = ('skillid','skillname','skillcode','contractflag')


class DesignationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Designation
        fields = ('designation_id','designation_name','designation_code')


class ContractSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ('contractid','contractwith','cost',\
            'contracttype','locationcust','relatedcontract','customer','ba',\
        	'oppourtunityid','betterpalcesiteid','vertical','bonus','bonusduration',\
            'address1','address2','city','servicetype','panno','gstinno',\
            'place_of_supply_city','place_of_supply_state','address_of_delivery_city','address_of_delivery_state',\
        	'startdate','enddate','closedate','extenddate',\
        	'approvedby','approvestatus','remark','doclink1','doclink2',\
            'doclink3','doclink4')


class ContractDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = ContractDetail
        fields = ('contractdetid','requirequantity','contract',\
            'contacttype','skilllevel','designation','startquantity','endquantity',\
        	'uom','upperdev','lowerdev','ratetype','fixedcost','ot','adhoc','margintype',\
        	'marginvalue','isapplicablecomrange','billingcycle',\
        	'finalsubmissionflag','remark','aadhaar_data')

class AdditionalContractFieldSerializers(serializers.ModelSerializer):

    class Meta:
        model = AdditionalContractField
        fields = ('contractaddfieldid','contract','description','cost')

class Contract_Percentage_FieldSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contract_Percentage_Field
        fields = ('contract_per_loc_id','contract','state','city','percentage')


class DocumentSerializers(serializers.ModelSerializer):
    # contractid = serializers.ReadOnlyField(source='contractid.contractid')
    class Meta:
        model = Document
        fields = ('contractid', 'description', 'document','document1','document2')

class DetailAttCaptureSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = DetailAttCapture
        fields = ('id','contractid','date','skillid','designation','skillcount','skillotcount','extrashift')


class VerticalSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Vertical
        fields = ('verticalCode','verticalName','verticalShortName')


class KPICategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = KPICategory
        fields = ('kpicatCode','kpicatName')


class KPISerializer(serializers.ModelSerializer):

    class Meta:
        model = KPI
        fields = ('kpiCode','kpiName','category','status','description')


class KPIFrequencySerializer(serializers.ModelSerializer):

    class Meta:
        model = KPIFrequency
        fields = ('kpifreqid','contract','kpi','inputfrequency','outputfrequency')


class KPIDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = KPIDetail
        fields = ('kpidetid','contract','kpi','uom','targetdate','typeoftarget','target1')


class Capture_Daily_KPISerializer(serializers.ModelSerializer):

    class Meta:
        model = Capture_Daily_KPI
        fields = ('contractid','date','kpiid','actualcount')


class  InvoiceMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceMaster
        fields = ('invoiceid','contractid','finaltotal','selectedrowids')


class  AdditionalChargesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdditionalCharges
        fields = ('invoiceid','headerName','additionalCost')


class  InvoiceHeaderMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceHeaderMaster
        fields = ('stateid','address','gst','cin')

class InvoiceDetailCaptureSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceDetailCapture
        fields = ('contractid','contractTypeName','oppourtunityId','location',\
            'invoiceDate','skillName','designation','attendenceCount',\
            'cost','totalcost','status','rowInvoiceFlag')


