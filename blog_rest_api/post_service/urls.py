from django.urls import path, include

from post_service import views

# config 의 urls 에서 namespace 를 사용하려면 app_name 지정 필수
app_name = 'post_service'
urlpatterns = [
	path('', views.post_list, name='index'),
	path('login/', views.login, name='login'),
	path('login/validate/', views.login_validate, name='login_validate'),
]