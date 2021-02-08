"""
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('state',views.StateView)
router.register('city',views.CityView)
router.register('oploc',views.OperationLocationView)


urlpatterns = [
	path('locapi/',include(router.urls))
]
"""