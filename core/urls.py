from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.views.generic import RedirectView

schema_view = get_schema_view(
   openapi.Info(
      title="Employee API",
      default_version='v1',
      description="API documentation for the Employee Management System.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[],  # Swagger itself does not need auth
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('employees.urls')),
    path('api/attendance/', include('attendance.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Redirect root to Swagger
    path('', RedirectView.as_view(url='swagger/')),
]
