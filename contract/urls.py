"""
from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url


contract_count = views.ContractView.as_view({
    'get': 'allContractCount'
})

active_contract_count = views.ContractView.as_view({
    'get': 'activeContractCount'
})

close_contract_count = views.ContractView.as_view({
    'get': 'closeContractCount'
})

active_contract = views.ContractView.as_view({
    'get': 'activeContract'
})

close_contract = views.ContractView.as_view({
    'get': 'closeContract'
})

customerbaContract = views.ContractView.as_view({
    'get': 'customerbaContract'
})

custContractDetail = views.ContractDetailView.as_view({
    'get': 'custContractDetail'
})

router = routers.DefaultRouter()
router.register('type',views.ContractTypeView)
router.register('rate',views.RateTypeView)
router.register('sklevel',views.SkillLevelView)
router.register('contract',views.ContractView)
# router.register('contract/count',views.ContractView)
router.register('detail',views.ContractDetailView)
router.register('upload',views.DocumentView)


urlpatterns = [
	url(r'contractApi/count/$', contract_count, name='contract_count'),
	url(r'contractApi/custba/(?P<checkbacust>[0-1]{1,2})/$', customerbaContract, name='customerbaContract'),
	url(r'contractApi/contractdetail/(?P<chkcustdetail>[0-9]{1,6})/$', custContractDetail, name='custContractDetail'),
	# url(r'contractApi/actcontract/(?P<date>[-\d]+)/$', active_contract, name='active_contract'),
	url(r'contractApi/actctrcount/$', active_contract_count, name='active_contract_count'),
	url(r'contractApi/clsctrcount/$', close_contract_count, name='close_contract_count'),
	url(r'contractApi/actcontract/$', active_contract, name='active_contract'),
	url(r'contractApi/clscontract/$', close_contract, name='close_contract'),
	url(r'contractApi/',include(router.urls)),
]
"""