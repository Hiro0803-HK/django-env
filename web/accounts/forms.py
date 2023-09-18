from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#サインアップに使用するフォームのクラスを作成。データベースはUserを使用
class SignupForm(UserCreationForm):
  
  class Meta:
    model = User
    fields = ('username',)