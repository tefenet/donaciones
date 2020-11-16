var mymap = L.map('mapid').setView([-34.9217246, -57.95694], 12);
var field_lat = document.getElementById('gl_lat');
var field_lng = document.getElementById('gl_long');
let field_select = document.getElementById('city_id')

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoidWN1cmFqIiwiYSI6ImNraGM4b2pjZzA0NDkycnQzZHNnNmpkbXEifQ.9fI2AiJMz05Uq16hWfQL9w', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
}).addTo(mymap);

var searchControl = new L.esri.Geocoding.geosearch().addTo(mymap);


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

var results = new  L.layerGroup().addTo(mymap);
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
    field_lat.value = latlng.lat;
    field_lng.value = latlng.lng;    
    L.esri.Geocoding.reverseGeocode()
        .latlng([latlng.lat, latlng.lng])
        .run(function (error, result, response) {
            if (!error && response)                
                console.log(result.address.City)
            // acá se guardaría el nombre de la ciudad seleccionada en el atributo city_id de center
            // callback is called with error, result, and raw response
            // result.latlng contains the coordinates of the located address
            // result.address contains information about the match
        });
}

//este diccionario hay que completar con coordenadas de municipios
geo_locations={"Almirante Brown":{"lat":-34.829578,"lng":-58.370357}}

function getAjaxx(name) {
    return $.get({
      url: 'https://apis.datos.gob.ar/georef/api/municipios?formato=json&provincia=buenos+aires&nombre='+ encodeURIComponent(name)
    })
  }
  function setCentroide(jsonResponse) {
    let centroide = jsonResponse.municipios[0].centroide
    
    field_lat.value = centroide.lat;
    field_lng.value = centroide.lon;
    if (marker) { // check
        mymap.removeLayer(marker); // remove
    }
    marker = L.marker([centroide.lat, centroide.lon]).addTo(mymap);
    mymap.setView([centroide.lat, centroide.lon], 10);
  }


field_select.onchange=(ev)=>{    
    nombre=field_select.selectedOptions[0].text
    getAjaxx(nombre).done(setCentroide)    
    console.log(nombre)
}
