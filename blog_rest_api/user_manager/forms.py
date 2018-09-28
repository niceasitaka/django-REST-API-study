from django import forms

class LoginForm(forms.Form):
	id = forms.CharField(label='ID', max_length=12)
	# widget 증 forms.PasswordInput 은 패스워드 입력 시 문자가 보이지 않도록 처리
	password = forms.CharField(label='PASSWORD', max_length=12, widget=forms.PasswordInput)
	
class JoinForm(forms.Form):
	#  ID는 최소 4자 이상, 12사 이하 / 비밀번호는 최소 6자 이상 12자 이하
	id = forms.CharField(label='ID', min_length=4, max_length=12, required=True)
	password = forms.CharField(label='PASSWORD', min_length=6, max_length=12, required=True, 
								widget=forms.PasswordInput)
	password_check = forms.CharField(label='PASSWORD(input again)', min_length=6, 
										max_length=12, required=True, widget=forms.PasswordInput)