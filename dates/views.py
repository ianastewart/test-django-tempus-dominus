from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
from .models import DateTest
from .forms import *


# Create your views here.

class DateCreateView(CreateView):
    model = DateTest
    form_class = DateForm
    template_name = 'dates/date_form.html'
    success_url = '/'

    def form_invalid(self, form):
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        return super().post(request, args, kwargs)


class DateUpdateView(UpdateView):
    model = DateTest
    template_name = 'dates/date_form.html'
    form_class = DateForm
    success_url = '/'
    pass


class DateListView(ListView):
    model = DateTest
    template_name = 'dates/date_list.html'
    context_object_name = 'dates'
    pass