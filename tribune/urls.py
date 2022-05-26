from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # path('index/',views.index, name ='index'),
    path('today/',views.tribune_of_day,name='tribuneToday'),
    path('archives/(\d{4}-\d{2}-\d{2})' ,views.past_days_news,name='pastNews'),
    path('search/',views.search_results, name='searchResults'),
    path('article/(\d+)',views.article,name = 'article')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    
    