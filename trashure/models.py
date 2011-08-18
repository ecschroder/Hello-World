from django.db import models
from django.db.models.fields.files import ImageField

THE_ERA_CHOICES = (		# where to put this?
	('CH', 'Childhood'),
	('HS', 'High School'),
	('CL', 'College'),
	('AD', 'Adult'),
	('UN', 'unknown'),
)

TRASH_OR_TREASURE_CHOICES = (
	('Y', 'Treasure'),
	('N', 'Trash'),
)

class JunkPollItem(models.Model):
	the_name = models.CharField(max_length=200)
	the_description = models.TextField()
	the_photo = ImageField(upload_to='../media', height_field=None, width_field=None)
	the_memory = models.TextField()
	the_year = models.CharField(max_length=4)
	the_era = models.CharField(max_length=2, choices=THE_ERA_CHOICES)
	the_pub_date = models.DateTimeField('date published')
	# could add a votes manager here
	def __unicode__(self):
		return self.the_name
	
	
class TrashChoice(models.Model):
	poll = models.ForeignKey(JunkPollItem)
	choice = models.CharField(max_length=1, choices=TRASH_OR_TREASURE_CHOICES)
	votes = models.IntegerField()
	def __unicode__(self):
		return self.choice
	
	
	
