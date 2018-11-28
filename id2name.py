with open("index.txt") as index:
    dict = {}
    for line in index:
        fields = line.rstrip().rsplit('\t')
        dict[fields[0]] = fields[1]
with open("fpkm_table.txt") as orig_fpkm:
    with open ("fpkm_table_name.txt", 'w') as target_fpkm:
        next (orig_fpkm)
        for line in orig_fpkm:
            fields = line.rstrip().rsplit('\t')
            print(dict[fields[0]])
            target_fpkm.write(dict[fields[0]] + "\t" + line)
