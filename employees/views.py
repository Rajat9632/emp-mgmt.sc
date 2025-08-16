# employees/views.py

from django.shortcuts import render
from django.db.models import Count
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Department, Employee, Performance
from .serializers import DepartmentSerializer, EmployeeSerializer, PerformanceSerializer
from attendance.models import Attendance

# --- API ViewSets ---

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department']
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'date_of_joining']

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

# --- Analytics and Page Views ---

@api_view(['GET'])
def department_employee_count(request):
    """
    API endpoint that returns the count of employees for each department.
    """
    data = Department.objects.annotate(employee_count=Count('employees')).values('name', 'employee_count')
    return Response(data)

@api_view(['GET'])
def attendance_summary(request):
    """
    API endpoint that returns attendance summary statistics.
    """
    from datetime import date
    
    # Overall attendance summary
    attendance_data = Attendance.objects.values('status').annotate(count=Count('id'))
    summary = {item['status']: item['count'] for item in attendance_data}
    
    # Today's attendance summary
    today_attendance = Attendance.objects.filter(date=date.today()).values('status').annotate(count=Count('id'))
    today_summary = {item['status']: item['count'] for item in today_attendance}
    
    return Response({
        'overall': summary,
        'today': today_summary
    })

def charts_page_view(request):
    """
    A view to render the HTML page that will contain our charts.
    """
    return render(request, 'charts.html')
