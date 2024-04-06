
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('check/',views.check, name='check'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register',views.register_user, name='register'),
    path('record/<int:pk>',views.customer_record, name='record'),
    path('add/',views.add_record, name='add'),
    path('delete_record/<int:pk>',views.delete_customer_record, name='delete_record'),
    path('update/<int:pk>',views.update_record, name='update'),
    ]


