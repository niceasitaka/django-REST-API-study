from django.urls import path, include

from . import views

# config 의 urls 에서 namespace 를 사용하려면 app_name 지정 필수
app_name = 'user_manager'
urlpatterns = [
	path('login/', views.login, name='login'),
	path('login/validate/', views.login_validate, name='login_validate'),
	path('join/', views.join_page, name='join'),
]