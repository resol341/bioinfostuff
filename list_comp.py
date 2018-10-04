def compare_lists(list1, list2):
    overlap = []
    uniq_list1 = []
    non_rep_list1 = list(set(list1))
    non_rep_list2 = list(set(list2))
    uniq_list2 = non_rep_list2[:]
    for member in non_rep_list1:
        if member in non_rep_list2:
            uniq_list2.remove(member)
            overlap.append(member)
        else:
            uniq_list1.append(member)
    return non_rep_list1, non_rep_list2, overlap, uniq_list1, uniq_list2
def list_stat(list1, list2, overlap, uniq_list1, uniq_list2):
    with open ("list_stat.txt", 'w') as target_file:
        target_file.write(
        "list1 size:\t" + str(len(list1)) + '\n' +
        "list2 size:\t" + str(len(list2)) + '\n' +
        "number of item in common:\t" + str(len(overlap)) + '\n')
        target_file.write("overlap:\t" + '\n')
        for m in overlap:
            target_file.write(m)
        target_file.write("uniq in list1:\t" + str(len(uniq_list1)) + '\n')
        for uniq_1 in uniq_list1:
            target_file.write(uniq_1)
        target_file.write("uniq in list2:\t" + str(len(uniq_list2)) + '\n')
        for uniq_2 in uniq_list2:
            target_file.write(uniq_2)
with open("lista.txt") as pub_genes:
    pub_genelist = pub_genes.readlines()
with open("listb.txt") as re_genes:
    re_genelist = re_genes.readlines()
list_input = compare_lists(pub_genelist, re_genelist)
list_stat(list_input[0], list_input[1], list_input[2], list_input[3],list_input[4])