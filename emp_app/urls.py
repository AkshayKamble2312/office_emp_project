from django.contrib import admin
from django.urls import path,include
from. import views


admin.site.site_header = "Raj Infotech Admin"
admin.site.site_title = "Raj Infotech Admin Portal"
admin.site.index_title = "Welcome to Raj Infotech"

urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.loginuser, name='loginuser'),
    path('logout',views.logoutuser, name='logout'),
    path('all_emp',views.all_emp, name='all_emp'),
    path('add_emp',views.add_emp, name='add_emp'),
    path('remove_emp',views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>',views.remove_emp, name='remove_emp'),
    path('update_emp',views.update_emp, name='update_emp'),
    path('filter_emp',views.filter_emp, name='filter_emp'),
]
