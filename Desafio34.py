sal = float(input('Enter Employee Salary: '))
if sal > 1250.00:
    t = sal + (sal * 10 / 100)
    print("The Employee get 10% raise.\nThe Employee's new Salary is: $ {:.2f}".format(t))
else:
    f = sal + (sal * 15 / 100)
    print("The Employee get 15% raise.\nThe Employee's new Salary is: $ {:.2f}".format(f))