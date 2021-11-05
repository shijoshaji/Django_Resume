from django.contrib import admin
from .models import (SocialMedia, Academics)

# Register your models here.
# admin.site.register(SocialMedia)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'updated_at')


@admin.register(Academics)
class AcademicsAdmin(admin.ModelAdmin):
    list_display = ('course', 'is_active', 'updated_at')
