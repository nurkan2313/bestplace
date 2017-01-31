# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django_comments.models import Comment
from place.models import Place # Внимание !!!
from django_comments.models import Comment
import sendgrid







class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'Пользователь')
    avatar = models.ImageField(u'Фотография пользователя', upload_to='upload/avatar_pic/', blank=True, null=True)
    first_name = models.CharField(u'Имя', max_length=255)
    last_name = models.CharField(u'Фамилия', max_length=255)
    birthday = models.DateField(u'День рождения', blank=True, null=True)
    status = models.CharField(u'Статус', max_length=255, blank=True, null=True)
    phone = models.CharField(u'Мобильный телефон', max_length=30, blank=True, null=True)
    slug = models.SlugField(unique=True)
    create_add = models.DateTimeField(u'Профиль был создан: ', auto_now_add=True)
    favorites = models.ManyToManyField(Place) # Внимание !!!


    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


    def __unicode__(self):
        return self.user.username


@receiver(post_save, sender=User, dispatch_uid="create_profile")
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=Comment, dispatch_uid="comment_mail_send")
def comment_mail_send(sender, instance, created, **kwargs):
#    print dir(instance)
        

    if instance.is_public == True:
        sg = sendgrid.SendGridClient('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')
        message = sendgrid.Mail(to=instance.user_email, subject='Comment is published', html=instance.name+', Your comment is published', text='Body', from_email='mi@besmart.kz')
        status, msg = sg.send(message)

    else:
        sg = sendgrid.SendGridClient('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')
        message = sendgrid.Mail(to=instance.user_email, subject='Your comment is on moderation', html=instance.name+', Your last comment is succesfully saved. Please, wait for moderation.', text='Body', from_email='mi@besmart.kz')
        status, msg = sg.send(message)

