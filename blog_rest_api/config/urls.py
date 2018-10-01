from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

from post_service import views

schema_view = get_swagger_view(title='REST API TEST')

# config 의 urls 에서 namespace 를 사용하려면 app_name 지정 필수
urlpatterns = [
    path('admin/', admin.site.urls),
	path('board/', include('post_service.urls', namespace='post_service')),
	path('user/', include('user_manager.urls', namespace='user_manager')),
	
	path('rest-swagger/', schema_view),
	path('rest-api/', include('rest_framework.urls')),
	path('api/post/', views.Post_api.as_view()),
]
