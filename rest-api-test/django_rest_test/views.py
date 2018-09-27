from django.http.response import HttpResponse

from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

from .models import Post
from .serializers import PostSerializer

def blog_page(request):
	post_list = Post.objects.all()
	return HttpResponse('hello!' + post_list[0].title)

# 아래 내용은 serializers.py 로 옮김
'''
class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'content', 'reg_date']
'''

class Blog_api(GenericAPIView, mixins.ListModelMixin):
# ListModelMixin은 GeneicAPIView에 queryset과 serializer_class를 기반으로 하여 데이터 List를 만들어줌
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	
	# GET 요청에 대한 처리를 구현(api/blog/ 를 GET 으로 접근하면, 모든 Post 데이터를 얻도록)
	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)
		# ListModelMixin 클래스를 상속 받으면 list 라는 함수가 상속받아짐
		# get 메소드에서 이를 호출하는 것으로, 기본적으로 목록 조회 기능을 요청할 수 있음
	
'''
기본적으로 REST Framework는 GET / POST / PATCH / DELETE 등의 요청에 대한 기본 처리를 제공함

GenericAPIView 에서 각각 get / post / delete 등의 이름으로 정의가 되어 있음

GenericAPIView는 다른 Mixin 클래스와의 조합으로 쉽고 빠르게 구현하는 방법들을 제공하며, 
rest_framework.mixins 를 포함하고, ListModelMixins 라는 클래스를 다중 상속하여 해당 기능을 구현함
'''