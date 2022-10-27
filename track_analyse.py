import gpxpy
import gpxpy.gpx
import math

with open("izubr.gpx", "r", encoding="utf-8") as file:
    gpx = gpxpy.parse(file)
data = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            data.append([float(point.latitude), float(point.longitude), float(point.elevation)])


# print(f'{data[0][0]-data[1][0]};{data[0][1]-data[1][1]};{data[0][2]-data[1][2]}')


def get_track_distance(data):
    result = 0
    for i in range(len(data) - 1):
        x_diff = abs(data[i][0] - data[i+1][0]) * 111200
        y_diff = abs(data[i][1] - data[i+1][1]) * 111200
        z_diff = abs(data[i][2] - data[i+1][2])
        if x_diff < 6 and y_diff < 6 and z_diff < 6:
            x_diff = 0
            y_diff = 0
            z_diff = 0
        else:
            result += math.sqrt(x_diff * x_diff + y_diff * y_diff + z_diff * z_diff)
    return round(result, 2)


print(get_track_distance(data))
