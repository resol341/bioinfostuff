with open('genes.read_group_tracking') as fpkm_orig:
    with open('fpkm_table.txt', 'w') as fpkm_target:
        next(fpkm_orig)
        n = 0
        for line in fpkm_orig:
            n = n + 1
            fields = line.rstrip().rsplit('\t')
            fpkm_target.write(fields[0] + '\t' + fields[6] + '\t')
            if n % 12 == 0:
                fpkm_target.write('\n')
