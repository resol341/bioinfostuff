#import csv
#import numpy as np, scipy.stats as st
with open("median_data.txt") as median_data:
    with open ("pos_markers.txt", 'w') as pos_markers:
        markers = median_data.readline().rstrip().split("\t")
        lines = median_data.readlines()
        average_value = lines[-1].rstrip().split('\t')
        print(average_value)
        marker_average_dict = {}
        for i in range (1, len(markers)):
            marker_average_dict[markers[i]] = average_value[i]
        for line in lines[0:-1]:
            values = line.rstrip().split('\t')
            pos_markers.write(values[0] + '\t')
            marker_value_dict = {}
            for v in range (1, len(markers)):
                marker_value_dict[markers[v]] = values[v]
            for marker in markers[1:]:
                if float(marker_value_dict[marker]) >= float(marker_average_dict[marker]):
                    pos_markers.write(marker + ', ')
            pos_markers.write('\n')
