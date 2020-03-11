function init_map(height, mapId){
    /*
        Initialize a map.
       Params:
           height: value in px for height map. Width is 100% by default.
           mapId: div id for map
       Returns:
            map : a map object.
    */
    document.getElementById(mapId).style.height = height +'px';

    var map = L.map(mapId);
    L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 18,
      id: 'mapbox/streets-v11',
      tileSize: 512,
      zoomOffset: -1,
      accessToken: 'pk.eyJ1IjoiZ3VpbGxtbyIsImEiOiJjazdjbm1pdG4wbjNjM2Ztc21ocjU5OWF0In0.5wfY3OUFHYnVPNCqlKqafg'
    }).addTo(map);

    return map
}
function add_polyline(map, locations, color){
    /*
        Add a polyline path to a map.
        Params:
            map: See init_map()
            dataPoints: [
                [lat,lng],
            ]
    */
    locations = JSON.parse(JSON.stringify(locations))
    dataPoints = []
    for (index = 0; index < locations.length; ++index){
        dataPoints.push(JSON.parse(locations[index]["fields"]["posArray"]))
    }
    var polyline = L.polyline(dataPoints,{color: color}).addTo(map);
    map.fitBounds(polyline.getBounds());
}
function add_markers(map, locations){
    /*
        Add markers with confiance levels on path
        Params:
            map: See init_map()
            locations: [Location json]
    */
    // Init icons
      var lowIcon = L.icon({
        iconUrl: '/static/icons/circle_low.png',
        iconSize: [8, 8],
        iconAnchor: [4, 4],
        popupAnchor: [-3, -76],
      });
      var mediumIcon = L.icon({
        iconUrl: '/static/icons/circle_medium.png',
        iconSize: [8, 8],
        iconAnchor: [4, 4],
        popupAnchor: [-3, -76],
      });
      var highIcon = L.icon({
        iconUrl: '/static/icons/circle_high.png',
        iconSize: [8, 8],
        iconAnchor: [4, 4],
        popupAnchor: [-3, -76],
      });
      var endIcon = L.icon({
        iconUrl: '/static/icons/end.png',
        iconSize: [8, 8],
        iconAnchor: [4, 4],
        popupAnchor: [-3, -76],
      });
      var startIcon = L.icon({
        iconUrl: '/static/icons/start.png',
        iconSize: [8, 8],
        iconAnchor: [4, 4],
        popupAnchor: [-3, -76],
      });
      locations = JSON.parse(JSON.stringify(locations))
      for (index = 0; index < locations.length; ++index){
        var lat = locations[index]["fields"]["lat"]
        var lng = locations[index]["fields"]["lng"]
        var end = locations[index]["fields"]["end"]
        var start = locations[index]["fields"]["start"]
        var confiance = locations[index]["fields"]["confiance"]

        if(end){
            L.marker([lat,lng], {icon: endIcon, zIndexOffset: 1000}).addTo(map);
        }
        else if(start){
            L.marker([lat,lng], {icon: startIcon, zIndexOffset: 1000}).addTo(map);
        }
        else{
            if(confiance<50){
                L.marker([lat,lng], {icon: lowIcon}).addTo(map);
            }
            else if(confiance>75){
                L.marker([lat,lng], {icon: highIcon}).addTo(map);
            }
            else{
                L.marker([lat,lng], {icon: mediumIcon}).addTo(map);
            }
        }

      }
    }
