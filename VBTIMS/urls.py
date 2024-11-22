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
from NormalUser import views as n_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', v_views.homepage, name='homepage'),
    path('my_events/', v_views.my_events, name='my_events'),
    path('onaction/', v_views.onaction, name='onaction'),
    path('noaction/', v_views.noaction, name='noaction'),
    path('', v_views.selectMode, name='selectMode'),
    path('about_us/', v_views.about_us, name='about_us'),
    path('add_incident/', v_views.add_incident, name='add_incident'),
    path('delete_incident/<str:id>/', v_views.delete_incident, name='delete_incident'),
    path('edit_incident/<str:id>/', v_views.edit_incident, name='edit_incident'),
    path('login/', v_views.login_page, name='login_page'),
    path('signup/<str:user_type>/', v_views.sign_up, name='signup_page'),
    path('logout/', v_views.logout_view, name='logout'),
    path('completed/', v_views.completed, name='completed'),
    path('search/', v_views.search_events, name='search'),
    path('profile/', v_views.profile_view, name='profile'),
    path('event_details/<str:id>/', v_views.event_details, name='event_details'),

    path('homepage_volunteer/', n_views.homepage_volunteer,name='homepage_vol'),
    path('aboutus_volunteer/', n_views.about_us_volunteer, name='aboutus_vol'),
    path('assign_volunteer/<str:id>/', n_views.assign_volunteer, name='assign_volunteer'),
    path('unassign_volunteer/<str:id>/', n_views.unassign_volunteer, name='unassign_volunteer'),
    path('logout_volunteer/', n_views.logout_volunteer, name='logout_volunteer'),
    path('complete_volunteer/<str:id>/', n_views.complete_volunteer, name='complete_volunteer'),
    path('search_vol/', n_views.search_events_volunteer, name='search_vol'),
    path('event_details_vol/<str:id>', n_views.event_details_volunteer, name='event_details_vol'),
    path('profile_volunteer/', n_views.profile_view_volunteer, name='profile_vol'),
    path('my_involvements/', n_views.my_involvements, name='my_involvements'),
    path('on_action_volunteer/', n_views.on_action_volunteer, name='on_action_vol'),
    path('no_action_volunteer/', n_views.no_action_volunteer, name='no_action_vol'),
    path('completed_volunteer/', n_views.completed_volunteer, name='completed_vol'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)