from django.contrib import admin
from library.models import *


# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
