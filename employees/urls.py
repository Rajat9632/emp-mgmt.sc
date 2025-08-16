# employees/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'performance', views.PerformanceViewSet)

urlpatterns = [
    # URLs for the ViewSets
    path('', include(router.urls)),

    # URL for the analytics data endpoint
    path('analytics/employees-per-department/', views.department_employee_count, name='department-employee-count'),
    
    # URL for attendance analytics
    path('analytics/attendance-summary/', views.attendance_summary, name='attendance-summary'),

    # URL for the HTML charts page
    path('charts/', views.charts_page_view, name='charts-page'),
    
]
