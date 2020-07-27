with open('CARDIoGRAM_GWAS_RESULTS.txt') as gwas:
    firstline = gwas.readline()
    lines = gwas.readlines()
    with open('CARDIoGRAM_q23.31.txt', 'w') as gwas_q2331, open('CARDIoGRAM_q23.2.txt', 'w') as gwas_q232:
        gwas_q232.write(firstline)
        gwas_q2331.write(firstline)
        for line in lines:
            fields = line.split('\t')
            ChrPos = fields[1].split(':')
            if ChrPos[0] == 'chr10' and int(ChrPos[1]) >= 89600001 and int(ChrPos[1]) <= 89718512:
                gwas_q2331.write(line)
            elif ChrPos[0] == 'chr10' and int(ChrPos[1]) <= 89600000 and int(ChrPos[1]) >= 87900001:
                gwas_q232.write(line)
