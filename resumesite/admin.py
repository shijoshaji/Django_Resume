from django.contrib import admin
from .models import SocialMedia

# Register your models here.
# admin.site.register(SocialMedia)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
