from pdb import Restart

from django.contrib import admin
from .models import *


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'username', 'role', 'joined_at')
    list_filter = ('joined_at', 'role')
    search_fields = ('full_name', 'username', 'role')
    date_hierarchy = 'joined_at'


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('name', 'user__full_name')
    date_hierarchy = 'created_at'


@admin.register(Versions)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'test', 'capacity', 'created_at')
    list_filter = ('created_at', 'test')
    search_fields = ('name', 'test__name')
    date_hierarchy = 'created_at'


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_version', 'variation', 'created_at')
    list_filter = ('created_at', 'test_version')
    search_fields = ('test_version__name', 'variation')
    date_hierarchy = 'created_at'
