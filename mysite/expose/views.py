from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Article, Media
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

#Displays the 10 latest article titles.
class HomeView(generic.ListView):

	context_object_name = 'recentArticles'
	template_name = "expose/home.html"

	def get_queryset(self):
		"""Get the query set of the 10 latest published articles for the home page."""
		return( Article.objects.order_by('-article_date')[:10] )

#Displays a specific articles detail.
def article(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	return(render(request, 'expose/article.html', { 'article': article }))

#Displays a specific articles detail.
def archive(request):
	return(render(request, 'expose/archive.html', {'archive': ""}))

#Displays archive of articles.
def archive_year(request):
	archive_year = request.GET['year']
	articleList = Article.objects.filter(article_date__year=archive_year)
	return(render(request, 'expose/archive_year.html', {'articleList': articleList,}))

#Displays archive of certain month in user specified year and specified month.
def archive_month(request):
	archive_month = request.GET['month']
	archive_year = request.GET['year']

	articleList = Article.objects.filter(article_date__year=archive_year, article_date__month=archive_month)
	return(render(request, 'expose/archive_month.html', {'articleList': articleList,}))