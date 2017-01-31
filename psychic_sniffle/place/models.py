# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField



class PlaceTag(models.Model):
    name = models.CharField(u'Название', max_length=255)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(u'Название', max_length=255)
    slug = models.SlugField(u'Slug', max_length=70)

    class Meta:
        verbose_name = u'категорию'
        verbose_name_plural = u'Категории'

    def __unicode__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(u'Название ', max_length=30)
    slug = models.SlugField(u'Slug', unique=True)
    category = models.ForeignKey(Category, verbose_name=u'Категория', blank=True, null=True)
    created = models.DateTimeField(u'Дата регистрации: ', auto_now_add=True)
    modified = models.DateTimeField(u'Дата изменения: ', auto_now=True)
    main_foto = models.ImageField(u'Фотография заведения', upload_to='media/')
    tags = models.ManyToManyField(PlaceTag, related_name="place" )
    work_time = models.CharField(u'График работы', max_length=100)
    adress = models.CharField(u'Адрес', max_length=100)
    short_description = models.TextField(u'Краткое описание')
    description = models.TextField(u'Полное описание')
    is_published = models.BooleanField(u'Опубликовано', default=False)

    class Meta:
        verbose_name = u'заведение'
        verbose_name_plural = u'заведения'

    def __unicode__(self):
        return self.name

    def place_picture(self):
        return u'<img src="%s"  width="100"/>' % (self.main_foto.url)
    place_picture.short_description = u'Картинка'
    place_picture.allow_tags = True

def content_file_name(instance, filename):
    return 'uploads/{0}/{1}'.format(instance.place.slug, filename)

class PlacePicture(models.Model):
    place = models.ForeignKey(Place, related_name='pictures')
    picture = models.ImageField(u'Изображение', upload_to=content_file_name)
    
    class Meta:
        verbose_name = u'изображение'
        verbose_name_plural = u'Галерея'

    def __unicode__(self):
        return self.place.name


class Feedback(models.Model):
    comment = models.TextField(u'Коментарий')
    author = models.ForeignKey(User)
    created = models.DateTimeField(u'Дата публикации', auto_now_add=True)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return self.author.get_full_name()


class DetailMap(models.Model):
    map_name = models.CharField(max_length=100)
    position = GeopositionField()

    class Meta:
        verbose_name = u'карта'
        verbose_name_plural = u'карты'