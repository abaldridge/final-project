from django.db import models

class FoodRelated(models.Model):
    person = models.ManyToManyField(Person)
    slug_name = models.CharField(max_length=300)
    def  __unicode__(self):
        return self.slug_name
    class Meta:
        ordering = ('idk',)

class SocialMediaMassacres(models.Model):

class Florida(models.Model):

class Crimes
    
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    state_name = models.CharField(max_length=50)
    name_slug = models.SlugField()
    age = models.IntegerField()
    class Meta:
        verbose_name = "Person"
    def __unicode__(self):
        return (self.first_name, self.last_name, self.state_name, self.age)



#code below just attempting to figure this out#
class Incident(models.Model):
    crime_date = models.DateField()
    
class State(models.Model):
    state_name = models.CharField(max_length=50)
    name_slug = 

class Story
    headline = 
    blurb = 

class Incident(models.Model):
    first_name

#old code to look at#

class Florida(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    county = models.ForeignKey(County)
    site_id = models.CharField(max_length=3)
    def __unicode__(self):
        return self.name
    def get_absolute_url (self):
        return "reports/%s/

class Report(models.Model):
    lake = models.ForeignKey(Lake)
    date = models.DateField()
    alert = models.BooleanField()
    toxin = models.FloatField()
    ecoli = models.IntegerField()
    def __unicode__(self):
        return "%s on %s" (self.lake.name, self.date)
    
