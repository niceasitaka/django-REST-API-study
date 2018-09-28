from django.urls import path, include

from . import views

# config 의 urls 에서 namespace 를 사용하려면 app_name 지정 필수
app_name = 'post_service'
urlpatterns = [
	path('', views.post_list, name='index'),
]