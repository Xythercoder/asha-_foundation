from django.urls import path

from .views import home_view, signup_view, dashboard_view
from . import views

app_name = "users"

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    
    path('signup/', signup_view, name='sign-up'),
    
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

    path('create/', views.household_create, name='household_create'),
    path('list/', views.household_list, name='household_list'),
    path('update/<int:pk>/', views.household_update, name='household_update'),
    path('delete/<int:pk>/', views.household_delete, name='household_delete'),


    path('progress_create/',  views.progress_report_create, name='progress_report_create'),
    path('progress_list/', views.progress_report_list, name='progress_report_list'),
]
