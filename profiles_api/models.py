from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Gerenciador para a profile do usuario"""

    def create_user(self, email, name, password=None):
        """Criando um novo profile de usuário"""
        if not email:
            raise ValueError('User must have an email address')
        
        #normalizado os campos
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        #criptografando a senha
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    #criando um super usuário
    def create_superuser(self, email, name, password):
        """"Cria e sava um novo super usuário com o seguindes detalhes"""
        user = self.create_superuser(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Modelo de banco de dados para usuários no sistema"""

    #Criando o campo e-mail com o maximo de 255 caracteres e que seja unico
    email = models.EmailField(max_length=255, unique=True)
    #Campo que vai receber o nome de no maximo 255 caracteres
    name = models.CharField(max_length=255)
    #Verifica se o usuário esta ativo, ou seja, esta logado
    is_active = models.BooleanField(default=True)
    #Campo para saber se o usuario é um funcionario
    is_staff = models.BooleanField(default=False)

    #Criando o CLI para manipular o modelo
    objects = UserProfileManager()

    #Criando mais campos para o admin
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    #criando as funções para o django manipular o modelo
    def get_full_name(self):
        """Recuperando o nome todo do usuário"""
        return self.name
    
    def get_short_name(self):
        """Retornando o nome curto do usuário"""
        return self.name
    
    #Colocando o email do usuario como a string que representa esse modelo no admin
    def __str__(self):
        """Retorna o string representation do nosso usuário"""
        return self.email
