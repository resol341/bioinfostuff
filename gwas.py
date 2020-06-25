with open('cad.add.160614.website.txt') as gwas:
    firstline = gwas.readline()
    lines = gwas.readlines()
    with open('gwas_PTEN.txt', 'w') as gwas_pten:
        gwas_pten.write(firstline)
        for line in lines:
            fields = line.split('\t')
            if int(fields[1]) == 10 and int(fields[2]) >= 89623195 and int(fields[2]) <= 89728532:
                gwas_pten.write(line)
