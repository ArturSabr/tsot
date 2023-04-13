from django.shortcuts import render
from .models import *

from django.views.generic import ListView, DetailView, CreateView


# def home(request):
#     return render(request,'index1.html',{})

class Home(ListView):
    model = EmployeeModel
    queryset = EmployeeModel.objects.all()
    context_object_name = 'employees'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = EventModel.objects.order_by('-date')[:3]
        return context

class EventsListView(ListView):
    model = EventModel
    queryset = EventModel.objects.all()
    context_object_name = 'events'
    template_name = 'events.html'

class DetailEvent(DetailView):
    model = EventModel
    context_object_name = 'events'
    template_name = 'detail_events.html'

class EmployeeListView(ListView):
    model = EmployeeModel
    queryset = EmployeeModel.objects.all()
    context_object_name = 'events'
    template_name = 'detail_employees.html'

class DetailEmployee(DetailView):
    model = EmployeeModel
    context_object_name = 'employee'
    template_name = 'detail_employees.html'
