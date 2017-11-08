from django.db import models
import datetime
from django.utils import timezone

class Article( models.Model ):
	article_title = models.CharField(max_length = 100, default="A Non Creative Article")
	article_text = models.CharField(max_length = 10000)
	article_date = models.DateField('date published')
	article_upvote = models.IntegerField(default=0)
	article_downvote = models.IntegerField(default=0)

	def __str__(self):
		return self.article_title + " [ " + str(self.article_date) + " ]"

	def was_published_recently(self):
		return self.article_date >= timezone.now() - datetime.timedelta(days = 1)

class Media( models.Model ):
	media_id = models.ForeignKey( Article, on_delete=models.CASCADE )
	media =  models.BinaryField()
	media_type = models.CharField(max_length=20, default="Undefined")

	def __str__(self):
		return "Media_id: " + repr(self.media_id) + " Media_Type: " + self.media_type