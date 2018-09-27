from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

from django_rest_test import views

schema_view = get_swagger_view(title='REST API TEST')

urlpatterns = [
	path('admin/', admin.site.urls),
	path('rest-swagger/', schema_view),
	path('rest-api/', include('rest_framework.urls')),
	
	path('blog/', views.blog_page),
	
	path('api/blog/', views.Blog_api.as_view()),
]
