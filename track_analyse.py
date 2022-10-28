import gpxpy
import gpxpy.gpx
import math
import csv

with open("300км.gpx", "r", encoding="utf-8") as file:
    gpx = gpxpy.parse(file)
data = []
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            data.append([float(point.latitude), float(point.longitude), float(point.elevation)])


def get_track_distance(data):
    result = 0
    for i in range(len(data) - 1):
        x_diff = round(abs(data[i][0] - data[i + 1][0]) * 111200, 2)
        y_diff = round(abs(data[i][1] - data[i + 1][1]) * 111200, 2)
        z_diff = round(abs(data[i][2] - data[i + 1][2]), 2)
        # print(f'{x_diff}, {y_diff}, {z_diff}')
        result += math.sqrt(pow(x_diff, 2) + pow(y_diff, 2) + pow(z_diff, 2))
    return round(result, 2)


# with open('result.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
#     for row in data:
#         writer.writerow(row)





print(get_track_distance(data))
