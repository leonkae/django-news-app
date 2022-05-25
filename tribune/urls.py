from django.urls import path
from . import views

urlpatterns = [
    # path('index/',views.index, name ='index'),
    path('today/',views.tribune_of_day,name='tribuneToday'),
    path('archives/(\d{4}-\d{2}-\d{2})' ,views.past_days_news,name='pastNews')
]