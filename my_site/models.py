from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Skill(models.Model):
    class Meta:
      verbose_name_plural = 'Skills'
      verbose_name = 'Skill'

      name = models.CharField(max_length=20, blank=True, null=True)
      score = models.IntegerField(default=20, blank=True, null=True)
      image = models.FileField(blank=True, null=True, upload_to="skills")
      is_key_skill = models.BooleanField(default=False)

      def __str__(self):
         return self.name
 