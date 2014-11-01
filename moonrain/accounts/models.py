from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from ..projects.models import Project


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Необходимо ввести электронный адрес')

        user = self.model(
            email=UserManager.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email,
                                password=password,
                                username=username)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    '''
    Пользователь
    '''
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=255,
        unique=True,
        db_index=True,
    )

    username = models.CharField(
        verbose_name='Имя пользователя',
        blank=False,
        max_length=255,
        unique=True,
    )

    avatar = models.ImageField(
        verbose_name='Аватар',
        upload_to='images/%Y/%m',
        blank=True,
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=255,
        blank=True,
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=255,
        blank=True,
    )

    department = models.CharField(
        verbose_name='Подразделение',
        max_length=255,
        blank=True,
    )

    is_admin = models.BooleanField(
        verbose_name='Является администратором?',
        default=False,
    )

    projects = models.ManyToManyField(Project, verbose_name='Проекты',
                                      blank=True,
                                      help_text='Проекты, в которых участвует пользователь',)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_full_name(self):
        return '%s %s' % (self.last_name,
                          self.first_name,)

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Meta:
    verbose_name = ('Пользователь')
    verbose_name_plural = ('Пользователи')