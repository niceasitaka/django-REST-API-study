from django.http.response import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Post

def post_list(request):
	page_data = Paginator(Post.objects.all(), 3)
	page = request.GET.get('page')
	try:
		posts = page_data.page(page)
	# 페이지 첫 접속 시 PageNotAnInteger 오류가 발생할 수 있음
	except PageNotAnInteger:
		posts = page_data.page(1)
	except EmptyPage:
		posts = page_data.page(page_data.num_pages)
		# page_data.num_pages 는 전체 페이지 수를 나타냄

	# range 함수로 는 전체 페이지 수에서 범위를 리스트로 만듬
	# int 는 total_page가 range 함수로 적용되었기 때문에 템플릿에서 함께 연산되려면 int 형으로 변경 필요함
	context = {'post_list':posts, 'current_page':int(page), 'total_page':range(1, page_data.num_pages + 1)}
	
	return render(request, 'post_list.html', context)