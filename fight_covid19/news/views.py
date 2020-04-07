from django.shortcuts import render
from newsapi import NewsApiClient
from django.core.cache import cache
from fight_covid19.news.helpers import get_news


def index(request):
    news_dict = cache.get("news", default=None)
    if not news_dict:
        news_dict = get_news()
    return render(request, "news/news.html", context={"news_dict": news_dict})
