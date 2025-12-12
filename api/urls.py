from django.urls import path
from .views import EmployeeListCreateView, EmployeeDetailView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view()),     # GET, POST
    path('employee/<int:pk>/', EmployeeDetailView.as_view()), # GET, PUT, DELETE
]