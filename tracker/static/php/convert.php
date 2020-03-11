<?php
    function jsonToKml($jsonPath){
    /*
        :params: [string] path of json
        :return: [string] kml formated
    */
        $data = json_decode(file_get_contents($jsonPath));
        $kmlOutput = "<?xml version='1.0' encoding='UTF-8'?>".
                            "<kml xmlns='http://www.opengis.net/kml/2.2'>";
        foreach ($data as $location){
            $name = $location->id;
            $description = "";
            $coordinates = $location->lat.",".$location->lng;

            $kmlOutput .= "<Placemark>".
                             "<name>".$name."</name>".
                             "<description>".$description."</description>".
                             "<Point>".
                                "<coordinates>".$coordinates."</coordinates>".
                            "</Point>".
                         "</Placemark>";
        }

        $kmlOutput .= "</kml>";

        return $kmlOutput;
    }

    $jsonPath = "../json/traj1.json";
    var_dump(jsonToKml($jsonPath))
?>