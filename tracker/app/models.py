from django.db import models


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    lng = models.FloatField()
    lat = models.FloatField()
    origin = models.IntegerField()
    confiance = models.FloatField()
    end = models.BooleanField()
    start = models.BooleanField()
    posArray = models.FloatField()

    @classmethod
    def create(cls, id, lng, lat, origin, confiance):
        '''
        :param id: [Integer] primary key
        :param lng: [Float] determines longitude
        :param lat: [Float] determines latitude
        :param origin: [Integer] determines id path
        :param confiance: [Float] confiance value
        end: [Boolean] determine the end of path
        start: [Boolean] determine the start of path
        posArray: [Float array] formated latitude, longitude
        :return: self
        '''
        location = cls(
            id=id,
            lng=lng,
            lat=lat,
            origin=origin,
            confiance=confiance,
            end=False,
            posArray=[lat, lng]
        )
        return location

    def set_start(self):
        self.start = True

    def set_end(self):
        self.end = True
