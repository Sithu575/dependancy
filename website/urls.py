from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    #path('login/', views.login,name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('register/', views.register_user,name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('add_department/', views.add_department, name='add_department'),
    path('add_organization/', views.add_organization, name='add_organization'),
    path('add_contacts/', views.add_contacts, name='add_contacts'),
    path('add_leads/', views.add_leads, name='add_leads'),
    path('view_leads/<int:pk>', views.view_leads, name='view_leads'),
    path('lead/', views.lead, name='lead'),
    path('lead_approval/<int:pk>', views.lead_approval, name='lead_approval'),
    path('load_organization/', views.load_organization, name='load_organizaton'),
    path('search_lead/', views.search_lead, name='search_lead'),
   
    
]