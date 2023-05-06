import json
from input_module import get_employee_details


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            employee_list = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        employee_list = []
    return employee_list


def write_json_to_file(json_obj, output_file):
    with open(output_file, 'w') as f:
        json.dump(json_obj, f, indent=4)


def main():
    file_path = './employees.json'
    employee_list = read_json_file(file_path)

    while True:
        employee_dict = get_employee_details()
        employee_list.append(employee_dict)

        print('\n')
        choice = input(
            "Do you want to enter details for another employee? (Y/N): ")
        if choice.lower() == 'n':
            break

    write_json_to_file(employee_list, file_path)


if __name__ == '__main__':
    main()
