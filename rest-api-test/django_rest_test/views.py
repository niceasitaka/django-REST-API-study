from django.http.response import HttpResponse

from .models import Post

def blog_page(request):
	post_list = Post.objects.all()
	
	return HttpResponse('hello!' + post_list[0].title)