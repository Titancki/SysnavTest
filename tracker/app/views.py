from django.http import HttpResponse, Http404
from django.template import loader
from django.core import serializers
from django.conf import settings
from app.utils.convert import locationsToKml, jsonToLocations
import os
def index(request):
    jsonFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/json/')
    if request.method == 'GET' and 'jsonPath' in request.GET:
        jsonPath = os.path.join(jsonFolder,request.GET['jsonPath'])
    else:
        jsonPath = os.path.join(jsonFolder,'traj1.json')

    locations = jsonToLocations(jsonPath)
    locations = serializers.serialize("json", locations)

    template = loader.get_template('app/index.html')
    context = {
        'locations': locations,
    }
    return HttpResponse(template.render(context, request))

def convertKml(request):

    template = loader.get_template('app/convertKml.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def downloadKml(request):
    jsonFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/json/')
    if request.method == 'GET' and 'jsonPath' in request.GET:
        jsonPath = os.path.join(jsonFolder,request.GET['jsonPath'])
    else:
        jsonPath = os.path.join(jsonFolder,'traj1.json')

    locations = jsonToLocations(jsonPath)

    if locationsToKml(locations)["http"] == 200:
        kmlContent = locationsToKml(locations)["data"]
    else:
        raise 500
    pathDownload = os.path.join(jsonFolder,"../kml/kmlfile.kml")
    f = open(pathDownload, "w")
    f.write(kmlContent)
    f.close()
    file_path = os.path.join(settings.MEDIA_ROOT, pathDownload)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
    template = loader.get_template('app/convertKml.html')
    context = {

    }
    return HttpResponse(template.render(context, request))