def read_patients_list(patients_list):
    """read file containig list of patients, one per line."""
    with open(patients_list) as selectpatients:
        lines = selectpatients.readlines()
        select_patients = []
        for line in lines:
            select_patients.append(line.rstrip())
        return select_patients
def enumerate_patients(expression_file, select_patients):
    """generate list containing the numbers of patients of interest in the expression file."""
    with open(expression_file) as expression:
        first_line = expression.readline().rstrip()
        patients = first_line.split('\t')
        patients_enumerate = [i for i,x in enumerate(patients) if x in select_patients]
        patients_enumerate = [0] + patients_enumerate
    return patients_enumerate
patients_list = input("Please enter full file name of the patient list file: ")
select_patients = read_patients_list(patients_list)
expression_file = input("Please enter full filename of the expression file: ")
id_patients_of_interest = enumerate_patients(expression_file, select_patients)
new_file = input("Please enter name for file output: ")
with open(new_file, 'w') as new_list:
    with open(expression_file) as expression:
        lines = expression.readlines()
        for line in lines:
            fields = line.rstrip().split('\t')
            for column in id_patients_of_interest:
                new_list.write(fields[column] + '\t')
            new_list.write('\n')