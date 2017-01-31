# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from profiles.models import Profile
from django import forms
from django.http import JsonResponse
from .admin import Comment


def profile(request):
    profile = request.user.profile
    return render(request, 'profiles/profile.html', {'profile': profile})


def profile_detail_public(request, username):
    user = User.objects.get(username=username)
    profile = user.profile
    if request.user.is_authenticated:
        return render(request, 'profiles/profile.html', {'profile': profile})


def profile_detail_private(request):
    profile = request.user.profile
    if request.user.is_authenticated:
        return render(request, 'profiles/profile_detail.html', {'profile': profile,})


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
           'avatar', 'birthday', 'status', 'phone'
        )


def profile_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    form = ProfileEditForm(
        request.POST or None,
        request.FILES or None,
        instance=profile
    )

    if form.is_valid():
        profile_form = form.save(commit=False)
        profile_form.user = request.user
        profile_form.save()
        return redirect('/profiles/')
    return render(request, 'profiles/profile_edit.html', {'form': form})


def profiles_bookmark_list(request):
    return render(request, 'profiles/profiles_bookmark_list.html', locals())


def add_favorite(request):
    from place.models import Place
    place_id = request.GET['place_id']
    place = Place.objects.get(id=place_id)
    request.user.profile.favorites.add(place)
    return JsonResponse({'status': 'OK', 'message': u'Закладка добавлена!'})


def remove_favorite(request):
    from place.models import Place
    place_id = request.GET.get('place_id', None)
    place = Place.objects.get(id=place_id)
    request.user.profile.favorites.remove(place)
    return JsonResponse({'status': 'OK', 'message': u'Закладка Удалена!'})

def comment(request):
    comment = Comment.objects.all()
    return render(request, 'profiles/profile_detail_private.html')