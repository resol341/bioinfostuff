with open("GPL13912_old_annotations.txt") as gene_annotation:
    lines = gene_annotation.readlines()
    gene_annotation_dict = {}
    for line in lines:
        gene = line.rstrip().split('\t')
        try:
            gene_annotation_dict[gene[0]] = gene[1]
        except IndexError:
            pass
with open("geo2r.txt") as gene_expression:
    first_line = gene_expression.readline()
    lines = gene_expression.readlines()
    with open("myupgenes_name.txt", 'w') as target_file:
        target_file.write(first_line)
        for line in lines:
            expression = line.rstrip().split("\t")
            if expression[0] in gene_annotation_dict.keys():
                target_file.write(gene_annotation_dict[expression[0]] + "\t" + line)