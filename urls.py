"""rentame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from inicio import views
from django.conf import settings 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name="Principal"),
    path('administrador/',views.administrador,name="Admin"),
    path('cabañas/',views.cabañas,name="Cabañas"),
    path('contactanos/',views.contacto,name="Contactanos"),
    path('nosotros/',views.nosotros,name="Nosotros"),
    path('ayuda/',views.ayuda,name="Ayuda"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
