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
            res = requests.get(url, params={'api_key': API_KEY, 'sort': 'latest'})
            sightings = res.json['data']['sightings']
            for sighting in sightings:
                review = sighting['current_review']

                image_url = review['thumb_280']
                "http://s3.amazonaws.com/foodspotting-ec2/reviews/2526351/thumb_275.jpg?1349541252"
                "http://dtlddqohdq03s.cloudfront.net/"
                image_url = image_url.replace("s3.amazonaws.com/foodspotting-ec2/",
                        "dtlddqohdq03s.cloudfront.net/")
                item = sighting['item']
                place = sighting['place']
                try:
                    new, created = Sighting.objects.get_or_create(
                            id=sighting['id'],
                            thumb_280=image_url,
                            item_name=item['name'][:200],
                            place_name=place['name'][:200],
                            lat=sighting['latitude'],
                            lng=sighting['longitude'],
                            review_id=review['id']
                    )
                except IntegrityError:
                    pass
                if created:
                    print 'Added', sighting['id']
            time.sleep(5)
            print 'Done!'