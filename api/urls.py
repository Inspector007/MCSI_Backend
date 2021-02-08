from django.urls import path, include
from account import views as accview
from contract import views as conview
from location import views as locview
from rest_framework import routers
from django.conf.urls import url


contract_count = conview.ContractView.as_view({
    'get': 'allContractCount'
})

active_contract_count = conview.ContractView.as_view({
    'get': 'activeContractCount'
})

close_contract_count = conview.ContractView.as_view({
    'get': 'closeContractCount'
})

cust_contract_count = conview.ContractView.as_view({
    'get': 'allCustomerContractCount'
})

active_cust_contract_count = conview.ContractView.as_view({
    'get': 'activeCustomerContractCount'
})

close_cust_contract_count = conview.ContractView.as_view({
    'get': 'closeCustomerContractCount'
})

ba_contract_count = conview.ContractView.as_view({
    'get': 'allBAContractCount'
})

active_ba_contract_count = conview.ContractView.as_view({
    'get': 'activeBAContractCount'
})

close_ba_contract_count = conview.ContractView.as_view({
    'get': 'closeBAContractCount'
})

productattactivecount = conview.ContractView.as_view({
    'get': 'productattactivecount'
})

productattpendingcount = conview.ContractView.as_view({
    'get': 'productattpendingcount'
})

invoicegeneration = conview.ContractView.as_view({
    'get': 'invoicegeneration'
})

invoicegenerationwithdate = conview.ContractView.as_view({
    'get': 'invoicegenerationwithdate'
})


consolidatedinvoicegenerationwithdate = conview.ContractView.as_view({
    'get': 'consolidatedinvoicegenerationwithdate'
})


active_contract = conview.ContractView.as_view({
    'get': 'activeContract'
})

close_contract = conview.ContractView.as_view({
    'get': 'closeContract'
})

customerbaContract = conview.ContractView.as_view({
    'get': 'customerbaContract'
})

contractfilter = conview.ContractView.as_view({
    'get': 'contractfilter'
})

getoppourtunitydata = conview.ContractView.as_view({
	'get' : 'getoppourtunitydata'
	})

getContractDetail = conview.ContractDetailView.as_view({
    'get': 'getContractDetail'
})

getContractDetail_output_based_pricing = conview.ContractDetailView.as_view({
    'get': 'getContractDetail_output_based_pricing'
})

getAdditionalContractField = conview.AdditionalContractFieldView.as_view({
    'get': 'getAdditionalContractField'
})


additionalContractFieldCapture = conview.AdditionalContractFieldView.as_view({
    'post': 'additionalContractFieldCapture'
})


getContractpercentageField = conview.Contract_Percentage_FieldView.as_view({
    'get': 'getContractpercentageField'
})


percentageContractFieldCapture = conview.Contract_Percentage_FieldView.as_view({
    'post': 'percentageContractFieldCapture'
})


getkpiDetail = conview.KPIDetailView.as_view({
    'get': 'getkpiDetail'
})


getkpiFrequency = conview.KPIFrequencyView.as_view({
    'get': 'getkpiFrequency'
})


attDetail = conview.DetailAttCaptureView.as_view({
    'get': 'attDetail'
})


getdailykpiDetail = conview.Capture_Daily_KPIView.as_view({
    'get': 'getdailykpiDetail'
})


getkpiGraphApi = conview.Capture_Daily_KPIView.as_view({
    'get': 'getkpiGraphApi'
})


consolidatedBAAttDetail = conview.DetailAttCaptureView.as_view({
    'get': 'consolidatedBAAttDetail'
})


capture_att_detail_api = conview.DetailAttCaptureView.as_view({
    'get': 'capture_att_detail_api'
})


manual_attcapture_detail_api = conview.DetailAttCaptureView.as_view({
    'get': 'manual_attcapture_detail_api'
})


contractDetailCapture = conview.ContractDetailView.as_view({
    'post': 'contractDetailCapture'
})


kpiDetailCapture = conview.KPIDetailView.as_view({
    'post': 'kpiDetailCapture'
})


kpiDetailExcelCapture = conview.KPIDetailView.as_view({
    'post': 'kpiDetailExcelCapture'
})


kpiFrequencyCapture = conview.KPIFrequencyView.as_view({
    'post': 'kpiFrequencyCapture'
})


attDetailCapture = conview.DetailAttCaptureView.as_view({
    'post': 'attDetailCapture'
})

createInvoiceMaster_basedonpercentage = conview.InvoiceMasterView.as_view({
    'post': 'createInvoiceMaster_basedonpercentage'
})

getInvoiceDetailCaptureRow = conview.InvoiceMasterView.as_view({
    'get': 'getInvoiceDetailCaptureRow'
})

getInvoiceAnnextureDetailRow = conview.InvoiceMasterView.as_view({
    'get': 'getInvoiceAnnextureDetailRow'
})

getAdditionalChargesDetail = conview.AdditionalChargesView.as_view({
    'get': 'getAdditionalChargesDetail'
})

additionalchargesCapture = conview.AdditionalChargesView.as_view({
    'post': 'additionalchargesCapture'
})

dailykpiCapture = conview.Capture_Daily_KPIView.as_view({
    'post': 'dailykpiCapture'
})


# account_login = accview.UserLocationCustomerView.as_view({
#     'post': 'account_login'
# })

customeratlocation = accview.UserLocationCustomerView.as_view({
    'get': 'customeratlocation'
})

customerslocation = accview.UserLocationCustomerView.as_view({
    'get': 'customerslocation'
})

get_betterplace_vendordata = accview.BAView.as_view({
    'get': 'get_betterplace_vendordata'
})

get_vendor_onsite = accview.BAView.as_view({
    'get': 'get_vendor_onsite'
})

sapuserlogin = accview.UserView.as_view({
    'post': 'sapuserlogin'
})

ratetypedetail = conview.RateTypeView.as_view({
    'get': 'getratetypeDetail'
})

skillleveldetail = conview.SkillLevelView.as_view({
    'get': 'getskilllevelDetail'
})

getlistcity = locview.CityView.as_view({
	'get': 'listcity'
})

getIndustryName = locview.LabourCost_State_IndustryWiseView.as_view({
	'get': 'getIndustryName'
})

getLabourCostIndustryWise = locview.LabourCost_State_IndustryWiseView.as_view({
	'get': 'getLabourCostIndustryWise'
})

getoploc = locview.OperationLocationView.as_view({
	'get': 'oploc_filter'
	})

get_vaayu_routing_response = locview.OperationLocationView.as_view({
	'get': 'vaayu_routing_response'
	})

getsiteiddata = locview.OperationLocationView.as_view({
	'get': 'getsiteiddata'
	})

getsitedata = locview.OperationLocationView.as_view({
	'get': 'getsitedata'
	})

get_pan_gstinno_list = locview.Invoice_Header_LocationView.as_view({
	'post': 'get_pan_gstinno_list'
	})


router = routers.DefaultRouter()
router.register('type',conview.ContractTypeView)
router.register('rate',conview.RateTypeView)
router.register('sklevel',conview.SkillLevelView)
router.register('designation',conview.DesignationView)
router.register('contract',conview.ContractView)
# router.register('contract/count',views.ContractView)
router.register('detail',conview.ContractDetailView)
router.register('additionalfield',conview.AdditionalContractFieldView)
router.register('Contract_Percentage_FieldView',conview.Contract_Percentage_FieldView)
router.register('upload',conview.DocumentView)
router.register('attcapture',conview.DetailAttCaptureView)
router.register('vertical',conview.VerticalView)

router.register('kpicategory',conview.KPICategoryView)
router.register('kpi',conview.KPIView)
router.register('kpifrequency',conview.KPIFrequencyView)
router.register('kpidetail',conview.KPIDetailView)
router.register('dailykpientry',conview.Capture_Daily_KPIView)
router.register('invoicemaster',conview.InvoiceMasterView)
router.register('additionalcharges',conview.AdditionalChargesView)
router.register('invoiceheadermaster',conview.InvoiceHeaderMasterView)

router.register('users',accview.UserView)
router.register('access',accview.AccessView)
router.register('useraccess',accview.UserAccessView)
router.register('customer',accview.CustomerView)
router.register('customermaster',accview.CustomerMasterView)
router.register('internalorders',accview.InternalOrdersView)
router.register('ba',accview.BAView)
router.register('ulc',accview.UserLocationCustomerView)
# router.register('login',accview.UserLoginAPIView)

router.register('state',locview.StateView)
router.register('labourcost',locview.LabourCost_State_IndustryWiseView)
router.register('city',locview.CityView)
router.register('oploc',locview.OperationLocationView)
router.register('invoiceloc',locview.Invoice_Header_LocationView)

urlpatterns = [
	# url(r'login/$',accview.UserLoginAPIView.as_view(),name='login'),
	path('rest-auth/', include('rest_auth.urls')),
	url(r'api/custatlocation/(?P<locid>[0-9]{0,5})/$', customeratlocation, name='customeratlocation'),
	url(r'api/customerslocation/(?P<custid>[0-9]{0,5})/$', customerslocation, name='customerslocation'),

	url(r'api/custba/(?P<checkbacust>[0-1]{1,2})/$', customerbaContract, name='customerbaContract'),
	# url(r'api/contractfilter/(?P<contractwith>[0-9]{1,2})&(?P<status>[0-9]{1,2})&(?P<location>[0-9]{1,4})/$', contractfilter, name='contractfilter'),
	url(r'api/contractfilter/(?P<contractwith>[0-9]{1,2})&(?P<status>[0-9]{1,2})&(?P<location>[0-9]{1,4})&(?P<oppid>[0-9A-Za-z]{10,15})&(?P<contractid>[0-9A-Za-z:-]{1,40})/$', contractfilter, name='contractfilter'),

	url(r'api/opportunity/(?P<oppid>[0-9A-Za-z]{1,15})/$', getoppourtunitydata, name='getoppourtunitydata'),

	url(r'api/contractdetail/(?P<contractid>[0-9A-Za-z:-]{1,40})/$', getContractDetail, name='getContractDetail'),
	url(r'api/contractdetailoutputbased/(?P<contractid>[0-9A-Za-z:-]{1,40})/$', getContractDetail_output_based_pricing, name='getContractDetail_output_based_pricing'),

	url(r'api/contractaddfield/(?P<contractid>[0-9A-Za-z:-]{1,40})/$', getAdditionalContractField, name='getAdditionalContractField'),
	url(r'api/percentagecontractfield/(?P<contractid>[0-9A-Za-z:-]{1,40})/$', getContractpercentageField, name='getContractpercentageField'),
	url(r'api/getkpidetail/(?P<contractid>[0-9A-Za-z:-]{1,40})/$', getkpiDetail, name='getkpiDetail'),
	url(r'api/getkpifrequency/(?P<contractid>[0-9A-Za-z:-]{1,40})/$', getkpiFrequency, name='getkpiFrequency'),
	url(r'api/attdetail/(?P<contractid>[0-9A-Za-z:-]{1,40})/(?P<date_att>\d{4}-\d{2}-\d{2})/$', attDetail, name='attDetail'),
	url(r'api/script/capture_att_detail_api/(?P<date_att>\d{2}-\d{2}-\d{4})/$', capture_att_detail_api, name='capture_att_detail_api'),
    url(r'api/script/manual_attcapture_detail_api/(?P<siteid>[0-9A-Za-z]{15,30})/(?P<contractid>[0-9A-Za-z:-]{1,40})/(?P<date_att>\d{2}-\d{2}-\d{4})/$', manual_attcapture_detail_api, name='manual_attcapture_detail_api'),

	url(r'api/getdailykpidetail/(?P<contractid>[0-9A-Za-z:-]{1,40})/(?P<date_att>\d{4}-\d{2}-\d{2})/$', getdailykpiDetail, name='getdailykpiDetail'),
	url(r'api/getkpigraphapi/(?P<contractid>[0-9A-Za-z:-]{1,40})/(?P<kpicode>[A-Za-z0-9]{1,20})/$', getkpiGraphApi, name='getkpiGraphApi'),
	url(r'api/consolidatedbaattdetail/(?P<contractid>[0-9A-Za-z:-]{1,40})/(?P<date_att>\d{4}-\d{2}-\d{2})/$', consolidatedBAAttDetail, name='consolidatedBAAttDetail'),
	url(r'api/condetailcapt/$', contractDetailCapture, name='contractDetailCapture'),
	url(r'api/contractaddfieldcapt/$', additionalContractFieldCapture, name='additionalContractFieldCapture'),
	url(r'api/percentagecontractfieldcapt/$', percentageContractFieldCapture, name='percentageContractFieldCapture'),
	url(r'api/kpicapt/$', kpiDetailCapture, name='kpiDetailCapture'),
	url(r'api/kpiexcelcapt/$', kpiDetailExcelCapture, name='kpiDetailExcelCapture'),
	url(r'api/kpifrequencycapt/$', kpiFrequencyCapture, name='kpiFrequencyCapture'),
	url(r'api/attdetailcapt/$', attDetailCapture, name='attDetailCapture'),
	url(r'api/dailykpicapt/$', dailykpiCapture, name='dailykpiCapture'),
	url(r'api/getinvoiceheaderdata/$', get_pan_gstinno_list, name='get_pan_gstinno_list'),

	# url(r'contractApi/actcontract/(?P<date>[-\d]+)/$', active_contract, name='active_contract'),
	url(r'api/ctrcount/$', contract_count, name='contract_count'),
	url(r'api/actctrcount/$', active_contract_count, name='active_contract_count'),
	url(r'api/clsctrcount/$', close_contract_count, name='close_contract_count'),

	url(r'api/custctrcount/$', cust_contract_count, name='cust_contract_count'),
	url(r'api/actcustctrcount/$', active_cust_contract_count, name='active_cust_contract_count'),
	url(r'api/clscustctrcount/$', close_cust_contract_count, name='close_cust_contract_count'),

	url(r'api/bactrcount/$', ba_contract_count, name='ba_contract_count'),
	url(r'api/actbactrcount/$', active_ba_contract_count, name='active_ba_contract_count'),
	url(r'api/clsbactrcount/$', close_ba_contract_count, name='close_ba_contract_count'),
	url(r'api/proattactivecount/$', productattactivecount, name='productattactivecount'),
	url(r'api/proattpendingcount/$', productattpendingcount, name='productattpendingcount'),
	url(r'api/oplocfilter/$', getoploc, name='getoploc'),
	url(r'api/getvaayuroutingresponse/$', get_vaayu_routing_response, name='get_vaayu_routing_response'),
	url(r'api/actcontract/$', active_contract, name='active_contract'),
	url(r'api/clscontract/$', close_contract, name='close_contract'),
	url(r'iscmsapapi/api/sapv1/Login/$', sapuserlogin, name='sapuserlogin'),

	# url(r'api/getinvoice/(?P<contractid>[0-9A-Za-z:-]{1,40})&\
		# (?P<startdate>^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$)\
		# &(?P<enddate>^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$)/$',\
		# invoicegeneration, name='invoicegeneration'),

	url(r'api/getinvoice/(?P<contractid>[0-9A-Za-z:-]{1,40})/$', invoicegeneration, name='invoicegeneration'),
	url(r'api/getrangeinvoice/(?P<contractid>[0-9A-Za-z:-]{1,40})/(?P<invoice_start_date>\d{4}-\d{2}-\d{2})/(?P<invoice_end_date>\d{4}-\d{2}-\d{2})/$', invoicegenerationwithdate, name='invoicegenerationwithdate'),
	url(r'api/getconsolidatedinvoice/(?P<contractid>[0-9A-Za-z:-]{1,40})/(?P<invoice_start_date>\d{4}-\d{2}-\d{2})/(?P<invoice_end_date>\d{4}-\d{2}-\d{2})/$', consolidatedinvoicegenerationwithdate, name='consolidatedinvoicegenerationwithdate'),

	url(r'api/getinvoicedetailcapturerow/(?P<rowids>[0-9-]{1,200})/$', getInvoiceDetailCaptureRow, name='getInvoiceDetailCaptureRow'),
	url(r'api/getinvoiceannexturerow/(?P<invoicemasterid>[0-9-A-Za-z:_-]{1,200})/$', getInvoiceAnnextureDetailRow, name='getInvoiceAnnextureDetailRow'),
	url(r'api/additionalchargesdetail/(?P<invoiceid>[0-9A-Za-z:_-]{1,40})/$', getAdditionalChargesDetail, name='getAdditionalChargesDetail'),
	url(r'api/additionalchargescapt/$', additionalchargesCapture, name='additionalchargesCapture'),
	url(r'api/createinvoicemaster/$', createInvoiceMaster_basedonpercentage, name='createInvoiceMaster_basedonpercentage'),

	url(r'api/getratetype/(?P<contracttypeid>[0-9]{1,5})/$', ratetypedetail, name='ratetypedetail'),
	url(r'api/getskilllevel/(?P<contractid>[0-9A-Za-z:-]{1,40})/$', skillleveldetail, name='skillleveldetail'),

	url(r'api/getcitylist/(?P<stateid>[0-9]{1,4})/$', getlistcity, name='listcity'),

	url(r'api/getindustrylist/$', getIndustryName, name='getIndustryName'),
	# (?# url(r'api/getsiteidlist/(?P<siteid>[0-9]{1,60})/(?P<sitename>[0-9A-Za-z&, ]{1,80})/$', getsiteiddata, name='getsiteiddata'),)
	url(r'api/getsiteidlist/(?P<siteid>[0-9]{1,60})/$', getsiteiddata, name='getsiteiddata'),
	url(r'api/getsitelist/$', getsitedata, name='getsitedata'),
	url(r'api/getvendoridlist/(?P<vendorid>[0-9]{1,60})/$', get_betterplace_vendordata, name='get_betterplace_vendordata'),
	url(r'api/filtervendorlist/(?P<siteid>[0-9]{1,60})/$', get_vendor_onsite, name='get_vendor_onsite'),

	url(r'api/getlabourcostlist/(?P<industryname>[a-zA-Z ]{1,60})/$', getLabourCostIndustryWise, name='getLabourCostIndustryWise'),

	# url(r'api/login/$', account_login, name='account_login'),
	url(r'api/',include(router.urls)),
]
