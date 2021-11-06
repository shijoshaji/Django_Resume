from django.contrib import admin
from .models import (SocialMedia, Academics, Professional)

# Register your models here.
# admin.site.register(SocialMedia)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'updated_at')


@admin.register(Academics)
class AcademicsAdmin(admin.ModelAdmin):
    list_display = ('course', 'is_active', 'updated_at')


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ('company', 'is_active', 'updated_at')
