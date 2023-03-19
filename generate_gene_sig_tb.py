#!/usr/bin/env python3
# This script is for generating suitable input for CellAssign using a table
# with a cell type and correponding gene in each line
f = open("/Users/lusiz/Downloads/tables2_cleanup_v2.txt", "r")
# first create a dict where the keys correspond to cell types while the list contained has marker genes
gene_list = []
marker_dict = {}
for x in f:
    line_list = x.split("\t")
    gene_list.append(line_list[1].rstrip())
    if line_list[0] in marker_dict.keys():
        marker_dict[line_list[0]].append(line_list[1].rstrip())
    else:
        marker_dict[line_list[0]] = [line_list[1].rstrip()]
gene_list_uniq = list(set(gene_list))
f.close()
target_file = open("/Users/lusiz/Downloads/heart_cellstype.csv", "w")
first_line = 'Gene,' + ','.join(marker_dict.keys()) + '\n'
target_file.write(first_line)
for gene in gene_list_uniq:
    line_list = []
    for cell in marker_dict.keys():
        if gene in marker_dict[cell]:
            line_list.append('1')
        else:
            line_list.append('0')
    line = gene + ',' + ','.join(line_list) + '\n'
    target_file.write(line)
target_file.close()
