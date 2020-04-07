from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response

from fight_covid19.news.helpers import get_news


class NewsViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        news_dict = cache.get("news", default=None)
        if not news_dict:
            news_dict = get_news()
        return Response(news_dict)
