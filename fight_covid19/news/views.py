from django.shortcuts import render
from newsapi import NewsApiClient
from django.core.cache import cache
from fight_covid19.news.helpers import get_news


def index(request):
    news_list = cache.get("news", default=None)
    if not news_list:
        news_list = get_news()
    return render(request, "news/news.html", context={"mylist": news_list})
