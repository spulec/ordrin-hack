from django.views.generic.base import View

from braces.views import JSONResponseMixin
from ordrin.models import Sighting


class AjaxSightings(JSONResponseMixin, View):
    def get(self, request):
        min_id = request.GET.get('min_id')
        sightings = Sighting.objects.all().order_by('-id')
        if min_id:
            sightings = sightings.filter(id__gt=min_id)
            if sightings:
                sightings = [list(sightings)[-1]]
        else:
            sightings = sightings[20:40]
        sightings = [x.__dict__ for x in sightings]
        for sighting in sightings:
            sighting.pop('_state')
        return self.render_json_response(sightings)


ajax_sightings = AjaxSightings.as_view()