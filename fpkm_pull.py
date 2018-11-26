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
    message = "Please type the full file name of the input FPKM file: "
    input_fpkm = input(message)
    with open(input_fpkm) as fpkm_input:
        firstline = fpkm_input.readline().rstrip()
        lines = fpkm_input.readlines()
    filename = input("Please type a name for the generated FPKM table: ")
    with open(filename, 'w') as fpkm_output:
        fpkm_output.write(firstline + '\n')
        for line in lines:
            line_split = line.split('\t')
            for candidate in candidates:
                if candidate == line_split[0]:
                    fpkm_output.write(line)
greeting_message = "Please select 1 for kegg pathway input or 2 for gene list file input: "
selection = input(greeting_message)
if selection == "1":
    pathway_list = pathway_input()
    genelist = []
    for pathway in pathway_list:
        genelist = genelist + get_genelist_kegg(pathway)
        #print(genelist)
        fpkm_filter_keyword(genelist)
elif selection == "2":
    genelist_file_message = "Please enter name of the file that contains the genelist: "
    genelist_file = input(genelist_file_message)
    genelist = get_genelist_file(genelist_file)
    fpkm_filter_keyword(genelist)
else:
    print("Invalid input, please try again")
