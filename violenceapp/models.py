from django.db import models

class State(models.Model):
    state_name = models.CharField(max_length=255)
    state_slug = models.SlugField()
    def  __unicode__(self):
        return self.state_name

class Tags(models.Model):
    tag = models.CharField(max_length=255)
    tag_slug = models.SlugField()
    def __unicode__(self):
        return self.tag
    def get_absolute_url(self):
        return "/tag/%s" % self.tag_slug
    
class Report(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    state = models.ForeignKey(State)
    report_date = models.DateField()
    description = models.TextField()
    tags = models.ManyToManyField(Tags, blank=True, null=True)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/reports/%i" % self.id
