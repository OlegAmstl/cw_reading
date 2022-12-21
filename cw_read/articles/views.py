from django.shortcuts import render, redirect

from .models import Article
from .forms import CreateArticle


def all_articles(request):
    articles = Article.objects.all()
    template = 'articles/all_articles.html'
    context = {
        'articles': articles,
    }
    return render(request, template, context=context)


def create_article(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            form.save()
            return redirect('articles:all_articles')

    form = CreateArticle
    template = 'articles/create_article.html'
    context = {
        'form': form,
    }
    return render(request, template, context=context)
