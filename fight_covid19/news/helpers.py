from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="9b1b5c60f90e4b229eced1f999e02310")


def get_news(search="coronavirus"):
    top_news = newsapi.get_top_headlines(
        q=search, language='en',country='in'
    )
    news_dict = dict()
    
    articles = top_news["articles"]
    
    for article in articles:
        if article["source"]["name"] in news_dict.keys():
            news_dict[article["source"]["name"]].append(article)
        else:
            news_dict[article["source"]["name"]] = [article]
    
    return news_dict
