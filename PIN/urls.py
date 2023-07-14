"""
URL configuration for PIN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import home, origen, cervezas, eventos, noticias, contacto, chopp, lager, malzbier 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home.as_view(), name = "landing_page"),
    path("origen", origen.as_view(), name = "origen"),
    path("cervezas", cervezas.as_view(), name = "cervezas"),
    path("eventos", eventos.as_view(), name = "eventos"),
    path("noticias", noticias.as_view(), name = "noticias"),
    path("contacto", contacto.as_view(), name = "contacto"),
    path("chopp", chopp.as_view(), name = "chopp"),
    path("lager", lager.as_view(), name = "lager"),
    path("malzbier", malzbier.as_view(), name = "malzbier"),
]
