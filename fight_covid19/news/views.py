from django.shortcuts import render 
from newsapi import NewsApiClient 
   
def index(request): 
      
    newsapi = NewsApiClient(api_key ='9b1b5c60f90e4b229eced1f999e02310') 
    top = newsapi.get_top_headlines(q='coronavirus',
                                          sources='bbc-news,the-verge,the-times-of-india'
                                        ) 
  
    l = top['articles'] 
    desc =[] 
    news =[] 
    img =[]
    url=[] 
  
    for i in range(len(l)): 
        f = l[i] 
        news.append(f['title']) 
        desc.append(f['description']) 
        img.append(f['urlToImage'])
        url.append(f['url']) 
    mylist = zip(news, desc, img, url) 
  
    return render(request, 'news/news.html', context ={"mylist":mylist})