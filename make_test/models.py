import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Users(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'Oddiy foydalanuvchi'),
    )
    full_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='F.I.Sh')
    username = models.CharField(max_length=100, null=True, blank=True, verbose_name='Username')
    phone = models.CharField(max_length=100, null=True, blank=True, verbose_name='Telefon raqam')
    telegram_id = models.BigIntegerField(null=True, blank=True, unique=True, verbose_name="Telegram ID")
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='user', null=True, blank=True,
                            verbose_name='Foydalanuvchi roli')
    joined_at = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now(),
                                     verbose_name="Qo'shilgan vaqti")

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'
        db_table = 'users'

    def __str__(self):
        return self.full_name


class Test(models.Model):
    name = models.CharField(max_length=221, null=True, blank=True, verbose_name="Nomi")
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Test egasi")
    file = models.FileField(upload_to='tests/', null=True, blank=True, verbose_name="Test Excel fayli")
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True,
                                      verbose_name="Yaratilgan vaqti")

    class Meta:
        db_table = 'Contest'
        verbose_name = 'Test'
        verbose_name_plural = "Testlar"

    def __str__(self):
        return self.name


class Versions(models.Model):
    name = models.CharField(max_length=221, null=True, blank=True, verbose_name="Nomi")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Test")
    tests_file = models.FileField(upload_to="versions/", null=True, blank=True, verbose_name="Tuzilgan testlar fayli")
    answers_file = models.FileField(upload_to='answers/', null=True, blank=True, verbose_name="Test javoblari")
    capacity = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(1000)
    ], verbose_name="Variantlar miqdori")
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True,
                                      verbose_name="Yaratilgan vaqti")

    class Meta:
        db_table = 'Version'
        verbose_name = "Version"
        verbose_name_plural = "Test versiyasi"

    def __str__(self):
        return self.name


class Results(models.Model):
    test_version = models.ForeignKey(Versions, on_delete=models.SET_NULL, null=True, blank=True,
                                     verbose_name="Test versiyasi nomi")
    variation = models.CharField(max_length=221, null=True, blank=True, verbose_name="Variant")
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True,
                                      verbose_name="Tekshirilgan vaqti")

    class Meta:
        db_table = 'Results'
        verbose_name = "Result"
        verbose_name_plural = "Natijalar"

    def __str__(self):
        return f"{self.test_version} {self.variation}"
