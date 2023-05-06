def get_employee_details():
    name = input('What is the employee name?: ')
    age = input('What is the employee age?: ')
    title = input('What is the employee job title?: ')

    # Create an employee dictionary
    employee_dict = {}
    employee_dict['first_name'] = name
    employee_dict['age'] = int(age)
    employee_dict['title'] = title

    return employee_dict
