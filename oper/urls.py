"""simplecrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.decorators import login_required
from oper import views as oper_views

urlpatterns = [
    url(r'^$', oper_views.ProdutoList.as_view(), name='produto_list'),
    url(r'^add/$', login_required(oper_views.ProdutoCreate.as_view(),
        login_url='account_login'),
        name='produto_add'
        ),
    url(r'^edit/(?P<pk>\d+)$', login_required(oper_views.ProdutoUpdate.as_view(),
        login_url='account_login'),
        name='produto_edit'
        ),
    url(r'^delete/(?P<pk>\d+)$', login_required(oper_views.ProdutoDelete.as_view(),
        login_url='account_login'),
        name='produto_delete'
        )

]
