class Employee:
    def __init__(self):
        self.name = ''
        self.ID_num = 0
        self.department = ''
        self.job_title = ''

person_1 = Employee()
person_1.name = 'Susan Meryers'
person_1.ID_num = 47899
person_1.department = 'Accounting'
person_1.job_title = 'Vice President'

person_2 = Employee()
person_2.name = 'Mark Jones'
person_2.ID_num = 39119
person_2.department = 'IT'
person_2.job_title = 'Programmer'

person_3 = Employee()
person_3.name = 'Joy Rogers'
person_3.ID_num = 81774
person_3.department = 'Manufacturing'
person_3.job_title = 'Engineer'

Employee_list = [person_1, person_2, person_3]

for person in Employee_list:
    print('Name:', person.name,'  ', 'ID Number:', person.ID_num, '  ', 'Department:', person.department, '  ', 'Job Title:', person.job_title)

