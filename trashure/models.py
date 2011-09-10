from django.db import models
import math
from django.db.models.fields.files import ImageField

THE_ERA_CHOICES = (		# where to put this?
	('CH', 'Childhood'),
	('HS', 'High School'),
	('CL', 'College'),
	('AD', 'Adult'),
	('UN', 'unknown'),
)

class JunkPollItem(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	photo = ImageField(upload_to='../media', height_field=None, width_field=None)
	memory = models.TextField()
	year = models.CharField(max_length=4)
	era = models.CharField(max_length=2, choices=THE_ERA_CHOICES)
	pub_date = models.DateTimeField('date published', auto_now=True)
	treasure_counter = models.IntegerField(default=0)
	trash_counter = models.IntegerField(default=0)
	rating_score = models.IntegerField(default=0)
	controversy_score = models.IntegerField(default=0)
	def __unicode__(self):
		return self.name
	def save(self, *args, **kwargs):
		self.rating_score = self.treasure_counter - self.trash_counter
		self.controversy_score = ( self.treasure_counter + self.trash_counter )/(math.fabs(self.rating_score)+1)
		super(JunkPollItem, self).save(*args, **kwargs) # see overriding model methods docs
	
