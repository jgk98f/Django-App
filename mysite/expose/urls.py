from django.conf.urls import url
from . import views

app_name='expose'

urlpatterns = [ url(r'^$', views.HomeView.as_view(), name='HomeView'),
	url(r'^article/(?P<article_id>[0-9]+)/$', views.article, name='article'),
	url(r'^archive/$' ,views.archive, name='archive'),
	url(r'^archive/by/year/$' ,views.archive_year, name='archive_year'),
	url(r'^archive/by/month/$', views.archive_month, name='archive_month'),
	url(r'^author/article/$', views.author_article, name='author_article'),
	url(r'^author/article/submit/$', views.submit_article, name='submit_article')
]