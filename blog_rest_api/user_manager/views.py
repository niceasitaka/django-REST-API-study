from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

from .forms import LoginForm, JoinForm

# Create your views here.

def login(request):
	context = {'login_form':LoginForm}
	return render(request, 'login_form.html', context)
	
def login_validate(request):
	login_form_data = LoginForm(request.POST)
	
	if login_form_data.is_valid():
		# authenticate() 함수는 username과 password 등, 여러가지 파라메터를 통하여 인증 과정을 수행
		# django.contrib.auth.models 에 포함된 User 모델의 데이터로 검증을 수행
		# username 이나 password에 login_form_data 인스턴스 내용들 할당 시, cleaned_data(사전형) 로 id 와 password 지정 필요
		user = auth.authenticate(username=login_form_data.cleaned_data['id'], 
									password=login_form_data.cleaned_data['password'])
		
		if user is not None:
			# 계정 활성화 여부 체크
			if user.is_active:
				auth.login(request, user)
				
				return redirect('post_service:index')
		else:
			return HttpResponse('사용자가 없거나 비밀번호를 잘못 입력하였습니다.')
	else:
		return HttpResponse('로그인 폼이 비정상 입니다.')
	
	return HttpResponse('알 수 없는 오류 입니다.')
	
def join_page(request):
	# POST로 넘어온 데이터는 회원 가입 로직으로 처리
	if request.method == 'POST':
		form_data = JoinForm(request.POST)
		
		if form_data.is_valid():
			username = form_data.cleaned_data['id']
			password = form_data.cleaned_data['password']
			password_check = form_data.cleaned_data['password_check']
			# 입력한 비밀번호와 재확인 내용이 같은지 확인
			if password == password_check:
				User.objects.create_user(username=username, password=password)			
				return redirect('user_manager:login')
			else:
				return HttpResponse('비밀번호와 비밀번호 확인의 내용이 다릅니다.')
	# POST 이외의 메소드로 넘어오면 빈 form 처리
	else:
		form_data = JoinForm()

	context = {'join_form':JoinForm}
	return render(request, 'join_page.html', context)