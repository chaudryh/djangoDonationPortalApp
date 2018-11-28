from django.conf.urls import url
from django.contrib import admin
from django.urls import include

from User import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url('signup/', views.signup, name='signup'),
    url('donation/', views.donation, name='donation'),
    url('edit_user/', views.edit_user, name='user_edit'),
    url('admin/auth/user/', views.donation_detail, name='delete_user'),
    url('donation_detail/(?P<id>\d+)/$', views.donation_detail, name='donation_detail'),
    url('admintemplate/', views.admintemplate, name='admintemplate'),
    url('userManagement/', views.user_Management, name='userManagement'),
    url('donationManagement/', views.donation_Management, name='donationManagement'),
    url('accounts/', include('django.contrib.auth.urls')),
    url('^$', views.home, name='home'),

]

