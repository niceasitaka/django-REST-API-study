from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'content', 'reg_date']

'''
Serializer는 queryset과 모델 인스턴스와 같은 복잡한 데이터를 
JSON, XML 또는 다른 콘텐츠 유형으로 쉽게 변환 가능
ModelForm 클래스와 유사하게 동작함
'''