from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from stars.models import Type, Star


# Create your views here.


class StarList(LoginRequiredMixin, View):
    def get(self, request):
        ty = Type.objects.all().count()
        st = Star.objects.all()

        ctx = {'type_count': ty, 'star_list': st}
        return render(request, 'stars/star_list.html', ctx)

class TypeView(LoginRequiredMixin, View):
    def get(self, request):
        ty = Type.objects.all()
        ctx = {'type_list': ty}
        return render(request, 'stars/type_list.html', ctx)


# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class TypeCreate(LoginRequiredMixin, CreateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars:all')


# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class TypeUpdate(LoginRequiredMixin, UpdateView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars:all')


class TypeDelete(LoginRequiredMixin, DeleteView):
    model = Type
    fields = '__all__'
    success_url = reverse_lazy('stars:all')


# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class StarCreate(LoginRequiredMixin, CreateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')


class StarUpdate(LoginRequiredMixin, UpdateView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')


class StarDelete(LoginRequiredMixin, DeleteView):
    model = Star
    fields = '__all__'
    success_url = reverse_lazy('stars:all')

# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createview