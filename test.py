import gpxpy
import gpxpy.gpx
import polyline

with open('Шумак 2022 подрез.gpx',"r", encoding="utf-8") as file:
    gpx = gpxpy.parse(file)

data = []

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            data.append((point.latitude, point.longitude))

with open('result.txt', 'w') as file:
    file.write(polyline.encode(data))
