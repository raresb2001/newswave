from django.shortcuts import render
import requests



def show_news(request):
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=7cd4f3a74a624a2498c0325a95af58d8'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'articles': articles,
    }

    return render(request, 'news/show_news.html', context)