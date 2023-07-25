from django.db import models

# Create your models here.

CATEGORY = (('Home', 'ホーム'), ('welcome', 'ようこそ'))

class Home(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY   
    )

    #データベースのタイトルを表示する関数
    def __str__(self):
        return self.title
