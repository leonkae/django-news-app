# from curses.ascii import HT
# from email import message
from django.http import HttpResponse,Http404
from django.shortcuts import redirect, render
import datetime as dt
# from django.template import loader
from .models import Article

def index(request):
    return render(request,('index.html'))

def news_of_day(request):
    date = dt.date.today()
    news =Article.todays_news()
    
 
    return render(request, 'all-news/today-news.html',{"date": date, "news":news})

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
    if date == dt.date.today():
        return redirect (news_today) 
    news = Article.days_news(date) 
    
    return render(request,'all-news/past-news.html',{"date": date, "news": news})

def news_today(request):
    # news= Article.objects.all()
    date = dt.date.today()
    news = Article.todays_news()
    return render(request,'all-news/today-news.html',{"news":news})
  
                
def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"
        
        return render (request, 'all-news/search.html',{"message":message, "articles": searched_articles})
    
    else:
        message = "You have not searched for any term"
        return render(request, 'all-news/search.html',{"message":message})             

def article(request,article_id):
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:   
        raise Http404()
    return render(request, 'all-news/article.html',{"article":article})             