from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="9b1b5c60f90e4b229eced1f999e02310")


def get_news(search="coronavirus"):
    top_news = newsapi.get_top_headlines(
        q=search,
        sources="bbc-news,the-verge,the-times-of-india,google-news,abc-news,cnn,cnbc,fox-news",
    )
    news_dict = dict()
    # news = []
    # desc = []
    # img = []
    # url = []
    articles = top_news["articles"]
    for article in articles:
        if article["source"]["name"] in news_dict.keys():
            news_dict[article["source"]["name"]].append(article)
        else:
            news_dict[article["source"]["name"]] = [article]
    # for article in articles:
    #     news.append(article["title"])
    #     desc.append(article["description"])
    #     img.append(article["urlToImage"])
    #     url.append(article["url"])
    #
    # formatted_news = zip(news, desc, img, url)
    return news_dict
