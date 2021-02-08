"""iscm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from . import settings
from contract import views as contract_view
from account import views as account_view
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='ISCM API')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('', include('account.urls')),
    # path('', include('contract.urls')),
    # path('', include('location.urls')),
    url(r'^login', account_view.account_login, name='account_login'),
    path(r'', include('api.urls')),
    path(r'swagger-docs/', schema_view),
    # url(r'^home$', contract_view.home, name='home'),
    # url(r'^uploads/form/$', contract_view.upload, name='upload'),
    # url(r'^upload/$', views.DocumentView.as_view(), name='file-upload'),
    # other urlpatterns...
    # path('microsoft/', include('microsoft_auth.urls', namespace='microsoft')),
    # url(r'^$',views.userlogin_view,name='userlogin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)