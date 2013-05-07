from django.db import models


# Create your models here.

class Video(models.Model):
	name = models.CharField(max_length=250)
	startDate = models.DateTimeField("Start date")
	average = models.FloatField(null=True)

	def __unicode__(self):
		return self.name

class Load(models.Model):
	video = models.ForeignKey(Video)
	dataDate = models.DateTimeField("Heure du chargement de la donnee")
	speed = models.FloatField()