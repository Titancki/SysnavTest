from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from app.utils.convert import locationsToKml, jsonToLocations

def index(request):
    if request.method == 'GET' and 'jsonPath' in request.GET:
        jsonPath = 'static/json/' + request.GET['jsonPath']
    else:
        jsonPath = 'static/json/traj1.json'

    locations = jsonToLocations(jsonPath)
    locations = serializers.serialize("json", locations)

    template = loader.get_template('app/index.html')
    context = {
        'locations': locations,
    }
    return HttpResponse(template.render(context, request))

def convertKml(request):
    locations = jsonToLocations('static/json/traj1.json')
    kml = locationsToKml(locations)

    template = loader.get_template('app/convertKml.html')
    context = {
        'kml': kml,
    }
    return HttpResponse(template.render(context, request))
