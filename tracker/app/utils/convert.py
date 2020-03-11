from app.models import Location
import json

def locationsToKml(locations):
    '''

    :param locations: [Location object array]
    :return: [string] kml formated
    '''
    kmlOutput = "<?xml version='1.0' encoding='UTF-8'?>" \
                    "<kml xmlns='http://www.opengis.net/kml/2.2'>"
    check = True
    for location in locations:
        if(isinstance(location, Location)):
            name = str(location.id)
            description = ""
            coordinates = str(location.posArray)
            kmlOutput += "<Placemark>" \
                             "<name>"+name+"</name>" \
                             "<description>"+description+"</description>" \
                             "<Point>" \
                                "<coordinates>"+coordinates+"</coordinates>" \
                            "</Point>" \
                         "</Placemark>"
        else:
            check = False
    kmlOutput += "</kml>"
    if not(check):
        kmlOutput = "Error: Wrong type"
    return kmlOutput

def jsonToLocations(jsonPath):
    '''

    :param jsonPath: [string] path to json
    :return: [Location object array] array of Location models
    '''
    i = 0
    locations = []
    # Fetch data from jsonfile
    with open(jsonPath, 'r') as file:
        locationsDict = json.load(file)
    # Compile into Location model
    for tmp in locationsDict:
        tmpObj = Location.create(
            tmp['id'],
            tmp['lng'],
            tmp['lat'],
            tmp['origin'],
            tmp['confiance']
        )
        if (i == 0):
            tmpObj.set_start()
        if (i == len(locationsDict) - 1):
            tmpObj.set_end()
        locations.append(tmpObj)
        i += 1
    return locations
