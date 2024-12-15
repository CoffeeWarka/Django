from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def func_temp(request):
    return render(request, 'second_task/def_view.html')


class class_temp(TemplateView):
    template_name = 'second_task/class_view.html'