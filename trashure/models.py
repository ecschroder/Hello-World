import math

from django.db import models
from django.db.models.fields.files import ImageField
from django.utils.translation import ugettext_lazy as _ # i18n on static text

# long choice names are easier to analyze
THE_ERA_CHOICES = (	
	('Childhood', _('Childhood')),
	('High_School', _('High School')),
	('College', _('College')),
	('Adult', _('Adult')),
	('unknown', _('unknown')),
)

class JunkPollItem(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	photo = ImageField(upload_to='../media', height_field=None, width_field=None)
	memory = models.TextField()
	year = models.CharField(max_length=4)
	era = models.CharField(_("era"), max_length=20, choices=THE_ERA_CHOICES)
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
	
