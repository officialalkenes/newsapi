from django.shortcuts import render

from newsapi import NewsApiClient

# Create your views here.
def dashboard(request):
    news_api = NewsApiClient(api_key= "3ed6a68e1aea44a48338570b00b9f2c1")
    head_lines = news_api.get_top_headlines(sources = "bbc-news")
    articles = head_lines["articles"]
    des = []
    image = []
    news = []

    for content in range(len(articles)):
        article = articles[content]
        des.append(article["description"])
        news.append(article["title"])
        image.append(article["urlToImage"])

    my_list = zip(news, des, image)

    context = {
        "my_list": my_list
    }

    return render(request, "dashboard.html", context)