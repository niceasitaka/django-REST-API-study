from django.http.response import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import auth

from .models import Post
from .forms import LoginForm

def post_list(request):
	page_data = Paginator(Post.objects.all(), 3)
	page = request.GET.get('page')
	
	# /board/ 페이지 접속 시 page 변수에 none이 할당되어 int로 변환 불가한 오류뜸
	# 아래처럼 page가 none일 경우 첫페이지로 볼 수 있도록 if 처리
	if page is None:
		page = 1
	
	try:
		posts = page_data.page(page)
	# 페이지 첫 접속 시 page가 int 형이 아니므로 except 처리함
	except PageNotAnInteger:
		posts = page_data.page(1)
	except EmptyPage:
		posts = page_data.page(page_data.num_pages)
		# page_data.num_pages 는 전체 페이지 수를 나타냄

	# range 함수로 는 전체 페이지 수에서 범위를 리스트로 만듬
	# int 는 total_page가 range 함수로 적용되었기 때문에 템플릿에서 함께 연산되려면 int 형으로 변경 필요함
	context = {'post_list':posts, 'current_page':int(page), 'total_page':range(1, page_data.num_pages + 1)}
	
	return render(request, 'post_list.html', context)
	
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
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		