class Employee:
    def __init__(self):
        self.name = ''
        self.ID = 0
        self.dept = ''
        self.title = ''


emp1 = Employee()
emp1.name = 'Susan Meyers'
emp1.ID = 47899
emp1.dept = 'Accounting'
emp1.title = 'Vice President'

emp2 = Employee()
emp2.name = 'Mark Jones'
emp2.ID = 39119
emp2.dept = 'IT'
emp2.title = 'Programmer'

emp3 = Employee()
emp3.name = 'Joy Rogers'
emp3.ID = 81774
emp3.dept = 'Manufacturing'
emp3.title = 'Engineer'

employees = [emp1, emp2, emp3]

for x in employees:
    print('Name:', x.name)
    print('ID Number:', x.ID)
    print('Department:', x.dept)
    print('Job Title:', x.title)
    print()

