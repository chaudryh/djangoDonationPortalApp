from django.conf.urls import url,include
from django.contrib import admin

from Cart import views
from User import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('donate/', views.donate, name='donate'),
    url('donation/', views.donation, name='donation'),
    url('edit_user/(?P<pk>\d+)/$', views.edit_user, name='edit_user'),
    url('^delete-entry/(?P<pk>\d+)/$', views.delete_user, name='delete_user'),
    url('^delete-entry/(?P<id>\d+)/$', views.delete_donation, name='delete_donation'),
    url('^delete-entry/(?P<id>\d+)/$', views.delete_donation_type, name='delete_donation_type'),
    url('add_user/', views.add_user, name='add_user'),
    url('donation_detail/(?P<id>\d+)/$', views.donation_detail, name='donation_detail'),
    url(r'^cart/', include(('Cart.urls','cart'), namespace='cart')),
    url('admintemplate/', views.admintemplate, name='admintemplate'),
    url('userManagement/', views.user_Management, name='userManagement'),
    url('donationManagement/', views.donation_Management, name='donationManagement'),
    url('accounts/', include('django.contrib.auth.urls')),
    url('donationTypeManagement/', views.donation_Type_Management, name='donationTypeManagement'),
    url('addDonationType/', views.add_donation_type, name='addDonationType'),

    url('^$', views.home, name='home'),



]

