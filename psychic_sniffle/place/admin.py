from django.contrib import admin
from django.db import models
from place.models import Place, PlaceTag, Feedback, Category, PlacePicture, DetailMap
from place.widgets import AdvancedFileInput
from place.forms import PlaceAdminForm



class PlacePictureStackable(admin.StackedInline):
    model = PlacePicture
    extra = 0
    formfield_overrides = {models.ImageField: {'widget': AdvancedFileInput}}


class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlacePictureStackable, ]
    list_display = ('place_picture', 'name', 'slug', 'is_published', 'created')
    list_filter = ('category', 'tags', )
    search_fields = ('name', 'slug', )
    readonly_fields = ('created', )
    prepopulated_fields = {"slug": ("name",)}
    model = Place
    formfield_overrides = {models.ImageField: {'widget': AdvancedFileInput}}
    form = PlaceAdminForm


admin.site.register(DetailMap)
admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceTag)
admin.site.register(Feedback)
admin.site.register(PlacePicture)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}

admin.site.register(Category, CategoryAdmin)
