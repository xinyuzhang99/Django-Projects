from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from gadgets.models import Brand, Gadget


# Create your views here.


class GadgetList(LoginRequiredMixin, View):
    def get(self, request):
        br = Brand.objects.all().count()
        ga = Gadget.objects.all()

        ctx = {'brand_count': br, 'gadget_list': ga}
        return render(request, 'gadgets/gadget_list.html', ctx)

class BrandView(LoginRequiredMixin, View):
    def get(self, request):
        br = Brand.objects.all()
        ctx = {'brand_list': br}
        return render(request, 'gadgets/brand_list.html', ctx)


# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class BrandCreate(LoginRequiredMixin, CreateView):
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class BrandUpdate(LoginRequiredMixin, UpdateView):
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


class BrandDelete(LoginRequiredMixin, DeleteView):
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class GadgetCreate(LoginRequiredMixin, CreateView):
    model = Gadget
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


class GadgetUpdate(LoginRequiredMixin, UpdateView):
    model = Gadget
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')


class GadgetDelete(LoginRequiredMixin, DeleteView):
    model = Gadget
    fields = '__all__'
    success_url = reverse_lazy('gadgets:all')

# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.

# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createview