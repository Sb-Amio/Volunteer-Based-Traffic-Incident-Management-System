"""
URL configuration for VBTIMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from Volunteer import views as v_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v_views.homepage, name='homepage'),
    path('my_events/', v_views.my_events, name='my_events'),
    path('onaction/', v_views.onaction, name='onaction'),
    path('noaction/', v_views.noaction, name='noaction'),
    path('selectMode/', v_views.selectMode, name='selectMode'),
    path('about_us/', v_views.about_us, name='about_us'),
    path('add_incident/', v_views.add_incident, name='add_incident'),
    path('delete_incident/<str:id>', v_views.delete_incident, name='delete_incident'),
    path('edit_incident/<str:id>', v_views.edit_incident, name='edit_incident'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)