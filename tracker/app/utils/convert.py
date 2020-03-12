from app.models import Location
import json

def locationsToKml(locations):
    '''

    :param locations: [Location object array]
    :return: [dict] {
            "http": http status
            "data": kml formated data
        }
    '''
    kmlOutput = "<?xml version='1.0' encoding='UTF-8'?>\n" \
                    "<kml xmlns='http://www.opengis.net/kml/2.2'>\n"
    check = True
    error = {
        "1": "Expect Location model\n",
        "2": "Missing id\n",
        "3": "Missing coordinates\n"
    }
    errors = []
    http = 200
    i = 0
    for location in locations:
        if isinstance(location, Location):
            if location.id:
                errors.append(error['2'] + " in locations [" + str(i) + "]")

            if location.posArray:
                errors.append(error['3'] + " in locations [" + str(i) + "]")
            name = str(location.id)
            description = ""
            coordinates = str(location.posArray)
            kmlOutput += "  <Placemark>\n" \
                         "    <name>"+name+"</name>\n" \
                         "      <description>"+description+"</description>\n" \
                         "        <Point>\n" \
                         "          <coordinates>"+coordinates+"</coordinates>\n" \
                         "        </Point>\n" \
                         "  </Placemark>\n"
            i += 1
        else:
            check = False
            errors.append(error['1'] + " in locations [" + str(i) + "]")
    kmlOutput += "</kml>"
    if not check:
        http = 500
        kmlOutput = errors
    output = {
        "http": http,
        "data": kmlOutput
    }
    return output

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

def test(jsonPath):
    return locationsToKml(jsonToLocations(jsonPath))