
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='admin_dashboard'),
    path('users/', views.manage_users, name='manage_users'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('users/deactivate/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path('turfs/', views.approve_turfs, name='approve_turfs'),
    path('logs/', views.system_logs, name='system_logs'),
    path('reports/', views.reports, name='reports'),
    path('disputes/', views.dispute_handling, name='dispute_handling'),
     path('reports/', views.view_reports, name='view_reports'), 
]
