import time
import requests

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from ordrin.models import Sighting

API_KEY = 'K5FoDxQC4qs3C0fO4UaCNCbv1TRZYjOvujslQ8tT'


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = "http://www.foodspotting.com/api/v1/sightings.json"
        try:
            last_id = Sighting.objects.all().order_by('-id')[0].id
        except IndexError:
            last_id = 0
        while True:
            res = requests.get(url, params={'api_key': API_KEY})
            sightings = res.json['data']['sightings']
            for sighting in sightings:
                review = sighting['current_review']
                item = sighting['item']
                place = sighting['place']
                new, created = Sighting.objects.get_or_create(
                        id=sighting['id'],
                        thumb_280=review['thumb_280'],
                        item_name=item['name'],
                        place_name=place['name'],
                        lat=sighting['latitude'],
                        lng=sighting['longitude']
                )
                if created:
                    print 'Added', sighting['id']
            time.sleep(5)
