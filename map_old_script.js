var data = JSON.parse("{{ data|escapejs }}");
var map = L.map("map");
var coordinates = L.Polyline.fromEncoded(data).getLatLngs();

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 18,
  attribution:
    '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

track = L.polyline(coordinates, {
  color: "#FF0000",
  weight: 3,
  opacity: 1.0,
  lineJoin: "round",
}).addTo(map);

map.fitBounds(track.getBounds());

var trackStart = [coordinates[0].lat,coordinates[0].lng]
var trackFinish = [coordinates[coordinates.length - 1].lat,coordinates[coordinates.length - 1].lng]

L.marker(trackStart).addTo(map);
L.marker(trackFinish).addTo(map);


//-----------------------------------------------------------------------------------------------



var distance = document.getElementById('route_distance');
  var elev_gain = document.getElementById('route_elev_gain');
  var map = L.map("map");

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 18,
    attribution:
      '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  var url = '{{ route.track.url }}'; // URL to your GPX file
  new L.GPX(url, {
    gpx_options: {
      joinTrackSegments: false
    },
    polyline_options: {
      color: '#FF0000',
      opacity: 1.0,
      weight: 3,
      lineCap: 'round'
    },
    async: true,
    marker_options: {
      startIconUrl: '{% static 'libs/leaflet-gpx/images/pin-icon-start.png' %}',
      endIconUrl: '{% static 'libs/leaflet-gpx/images/pin-icon-end.png' %}',
      shadowUrl: '{% static 'libs/leaflet-gpx/images/pin-shadow.png' %}'
    }
  }).on('loaded', function(e) {
    map.fitBounds(e.target.getBounds());
    distance.innerText = (e.target.get_distance() / 1000).toFixed(1) + ' км';
    elev_gain.innerText = (e.target.get_elevation_gain()).toFixed(1) + ' м';
  }).addTo(map);