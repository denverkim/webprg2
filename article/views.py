from django.shortcuts import render
from django.views import generic
from article.models import Article


def index(request):
    return render(request, 'index.html')
#    return HttpResponse('<h1>My first app</h1>')

def about(request):
    return render(request, 'about.html')

# def articles(request):
#     return render(request, 'articles.html')

class ArticleListView(generic.ListView):
    model = Article

class ArticleDetailView(generic.DetailView):
    model = Article