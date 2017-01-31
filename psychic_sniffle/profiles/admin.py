from django.contrib import admin

# Register your models here.
from profiles.models import Profile
from place.widgets import AdvancedFileInput
from django_comments.models import Comment


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('avatar', 'slug', 'birthday', 'create_add', 'phone', 'first_name')
    prepopulated_fields = {"slug": ("first_name",)}
    model = Profile


admin.site.register(Profile, ProfileAdmin)

