"""
from django.urls import path, include
from django.conf.urls import url

from . import views
from rest_framework import routers

customeratlocation = views.UserLocationCustomerView.as_view({
    'get': 'customeratlocation'
})
customerslocation = views.UserLocationCustomerView.as_view({
    'get': 'customerslocation'
})


router = routers.DefaultRouter()
router.register('users',views.UserView)
router.register('access',views.AccessView)
router.register('useraccess',views.UserAccessView)
router.register('customer',views.CustomerView)
router.register('ba',views.BAView)
router.register('ulc',views.UserLocationCustomerView)


urlpatterns = [
	url(r'accapi/custatlocation/(?P<locid>[0-9]{0,5})/$', customeratlocation, name='customeratlocation'),
	url(r'accapi/customerslocation/(?P<custid>[0-9]{0,5})/$', customerslocation, name='customerslocation'),
	path('accapi/',include(router.urls))
]
"""