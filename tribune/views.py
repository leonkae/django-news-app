from django.http import HttpResponse,Http404
from django.shortcuts import render
import datetime as dt
from django.template import loader

def index(request):
    return render(request,('index.html'))

def tribune_of_day(request):
    date = dt.date.today()
    
 
    return render(request, 'all-news/today-news.html',{"date": date})

def convert_dates(dates):
    # gets the weekday number
    day_number = dt.date.weekday(dates)
    
    days =['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','saturday']
    day = days[day_number]
    return day

def past_days_news(request,past_date):
  
    try:
        date = dt.datedate.strptime(past_date,'%Y-%m-%d').date()
        
    except ValueError:
        raise Http404()  
        assert False 
    
    return render(request,'all-news/past-news.html',{"date": date})