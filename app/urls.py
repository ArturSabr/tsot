from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('events/list', EventsListView.as_view(), name='programs'),
    path('employees/list', EmployeeListView.as_view(), name='projects'),
    path('events/<int:pk>', DetailEvent.as_view(), name='program_detail'),
    path('employees/<int:pk>', DetailEmployee.as_view(), name='project_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
