from django.urls import path
from register_app import views

# URL patterns for the registration app
urlpatterns = [
    # Root URL maps to the form view function (registration form)
    # The name='form' allows referring to this URL in templates with {% url 'form' %}
    path('', views.form, name='form'),
    
    # URL pattern for exporting registration data to Excel
    # The name='export_excel' allows referring to this URL in templates with {% url 'export_excel' %}
    path('export/', views.export_to_excel, name='export_excel'),
    
    # URL pattern for viewing all registrations
    path('registrations/', views.all_registrations, name='all_registrations'),
    
    # URL pattern for deleting a registration record
    path('delete/<int:id>/', views.delete_registration, name='delete_registration'),
    
    # URL pattern for deleting all registrations
    path('delete-all/', views.delete_all_registrations, name='delete_all_registrations'),
]