from django.db import models


class Sighting(models.Model):
    id = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=200)
    place_name = models.CharField(max_length=200)
    thumb_280 = models.URLField()
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    review_id = models.IntegerField()

    def __unicode__(self):
        return u"{}:{}".format(self.item_name, self.place_name)
