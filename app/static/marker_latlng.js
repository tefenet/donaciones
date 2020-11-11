var mymap = L.map('mapid').setView([-34.9217246, -57.95694], 12);
var field_lat = document.getElementById('gl_lat');
var field_lng = document.getElementById('gl_long');

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoidWN1cmFqIiwiYSI6ImNraGM4b2pjZzA0NDkycnQzZHNnNmpkbXEifQ.9fI2AiJMz05Uq16hWfQL9w', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
}).addTo(mymap);

var searchControl = L.esri.Geocoding.geosearch().addTo(mymap);


var marker;
mymap.on('click', function (e) {
    if (results) {
        results.clearLayers();
    }
    if (marker) { // check
        mymap.removeLayer(marker); // remove
    }
    marker = new L.marker(e.latlng).addTo(mymap);
    update_coordenadas(e.latlng);
});

var results = L.layerGroup().addTo(mymap);
searchControl.on('results', function (data) {
    if (marker) { // check
        mymap.removeLayer(marker); // remove
    }
    results.clearLayers();
    for (var i = data.results.length - 1; i >= 0; i--) {
        var marker_latlong = data.results[i].latlng;
        results.addLayer(L.marker(marker_latlong));
    }
    update_coordenadas(marker_latlong);
});

function update_coordenadas(latlng) {
    console.log(latlng.lat);
    console.log(latlng.lng);
    field_lat.value = latlng.lat;
    field_lng.value = latlng.lng;

}
