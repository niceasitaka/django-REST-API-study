from django.contrib import admin
from django.urls import path, include

# config 의 urls 에서 namespace 를 사용하려면 app_name 지정 필수
urlpatterns = [
    path('admin/', admin.site.urls),
	path('board/', include('post_service.urls', namespace='post_service')),
	path('user/', include('user_manager.urls', namespace='user_manager'))
]
