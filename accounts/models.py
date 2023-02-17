from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    # 일반 user 생성, username 이 userID를 의미함
    def create_user(self, email, username, name, password=None):
        # if not email:
        #     raise ValueError("Users must have an email address.")
        
        # if not name:
        #     raise ValueError("Users must have an name.")

        if not username:
            raise ValueError("Users must have an userID.")

        user = self.model(
            # email = self.normalize_email(email),           
            # name = name,
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    # 관리자 User 생성
    def create_superuser(self, email, username, name, password):
        user = self.create_user(
            # email = self.normalize_email(email),
            username = username,
            # name = name,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(blank=False, unique=True)
    name = models.CharField(max_length=10, blank=False)
    birth_day = models.DateField(null=True, blank=True)
    birth_time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    class Meta:
      ordering = ['created_at']

    def __str__(self):
      return f'{self.nick_name}'

    object = MyAccountManager()  # 헬퍼 클래스 사용
 
    USERNAME_FIELD = 'username'  # 로그인 ID로 사용할 필드
    # REQUIRED_FIELDS = ['password'] # 필수 작성 필드
 
    def __str__(self):
        return self.username
 
    def has_perm(self, perm, obj=None):
        return self.is_admin
 
    def has_module_perms(self, app_lable):
        return True
 


