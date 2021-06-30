from django.db import models

class User(models.Model):
    user_email = models.EmailField(max_length=128, unique=True, verbose_name="유저 이메일", default = '')
    user_id = models.CharField(max_length=32, unique=True, verbose_name='유저 아이디', default = '')
    user_pw = models.CharField(max_length=128, verbose_name='유저 비밀번호', default = '')
    user_name = models.CharField(max_length=16, verbose_name='유저 이름', default = '')
    user_birth = models.DateField(verbose_name='유저 생일', default = '')

    def __str__(self):
        return self.user_id

    class Meta:
        db_table='user'
        verbose_name='유저'
        verbose_name_plural='유저'