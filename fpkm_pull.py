def pathway_input():
    """Accept pathway input and store in a list"""
    pathways = []
    while True:
        message = "Please enter the pathways of interest, enter q when done: "
        pathway = input(message)
        if pathway == 'q':
            break
        else:
            pathways.append(pathway)
    return pathways
def get_genelist_kegg(pathway):
    import urllib.request
    genelist = []
    url = "http://rest.kegg.jp/get/" + pathway
    with urllib.request.urlopen(url) as kegg_pathway:
        lines = kegg_pathway.readlines()
        for line in lines:
            fields = line.split()
            if fields[0].decode('utf8') == 'GENE':
                genelist.append(fields[2].decode('utf8').rstrip(';'))
            else:
                try:
                    int(fields[0])
                    genelist.append(fields[1].decode('utf8').rstrip(';'))
                except ValueError:
                    pass
    return genelist
def get_genelist_file(filename):
    with open(filename) as genelist_file:
        genelist = [line.rstrip() for line in genelist_file]
        non_redundant_genelist = list(set(genelist))
    return non_redundant_genelist
def fpkm_filter_keyword(candidates):
    with open("FPKM_minus14171619_rearrange.txt") as fpkm_minus_full:
        firstline = fpkm_minus_full.readline().rstrip()
        lines = fpkm_minus_full.readlines()
    filename = input("Please type a name for the generated FPKM table: ")
    with open(filename, 'w') as fpkm_minus_select:
        fpkm_minus_select.write(firstline + '\n')
        for line in lines:
            line_split = line.split('\t')
            for candidate in candidates:
                if candidate == line_split[0]:
                    fpkm_minus_select.write(line)