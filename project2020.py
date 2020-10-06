from reading_from_user import read_nonempty_alphabetical_string, read_nonempty_string, read_range_integer


def display_title(section):
    print(f"\nModule Record System - {section}")
    print("-" * 30)


def menu():
    display_title("Please Choose")
    print("1. Record Attendance\n"
          "2. Generate Statistics\n"
          "3. Exit")
    choice = read_range_integer(">> ", 1, 3)

    return choice


def login():
    while True:
        with open("login_details.txt") as login_details:
            username = login_details.readline().rstrip()
            password = login_details.readline().rstrip()

            display_title("Login")
            entered_username = read_nonempty_alphabetical_string("Username >> ")
            entered_password = read_nonempty_string("Password >> ")

            if entered_username == username and entered_password == password:
                print(f"Welcome, {username}")
                break
            else:
                print("Please enter a valid username & password.")
    return username


def get_modules():
    module_codes = []
    module_names = []
    with open("modules.txt", "r") as modules:
        for module in modules:
            line = module.rstrip().split(",")
            line[1] = line[1].strip()
            module_codes.append(line[0])
            module_names.append(line[1])
    return module_codes, module_names


def choose_module(module_names, module_codes):
    display_title("Choose a Module")
    for i, module in enumerate(module_names):
        print(f"{i + 1}. {module_codes[i]} - {module}")
    choice = read_range_integer(">> ", 1, len(module_codes))
    choice = module_codes[choice - 1]
    return choice


def get_class_attendance(module_code):
    names_list = []
    present_list = []
    absent_list = []
    excuse_list = []
    with open(f"{module_code}.txt") as module:
        for line in module:
            line = line.rstrip().split(",")
            names_list.append(line[0].strip())
            present_list.append(int(line[1].strip()))
            absent_list.append(int(line[2].strip()))
            excuse_list.append(int(line[3].strip()))
    return names_list, present_list, absent_list, excuse_list


def take_class_attendance(module_code, names_list, present_list, absent_list, excuse_list):
    display_title(module_code)
    number_of_students = len(names_list)
    print(f"There are {number_of_students} students enrolled")
    for i, student in enumerate(names_list):
        print(f"Student {i + 1}: {student}")
        print("1. Present\n2. Absent\n3. Excuse")
        choice = read_range_integer(">> ", 1, 3)
        if choice == 1:
            present_list[i] = present_list[i] + 1
        elif choice == 2:
            absent_list[i] = absent_list[i] + 1
        else:
            excuse_list[i] = excuse_list[i] + 1

    update_class_attendance(module_code, names_list, present_list, absent_list, excuse_list)


def update_class_attendance(module_code, names_list, present_list, absent_list, excuse_list):
    with open(f"{module_code}.txt", "w") as module_file:
        for i, name in enumerate(names_list):
            module_file.write(name + ", " + str(present_list[i]) + ", " + str(absent_list[i]) + ", " +
                              str(excuse_list[i]) + "\n")
    print(f"{module_code}.txt successfully updated.")


def generate_and_save_stats(module_code, names_list, present_list, absent_list, excuse_list):
    no_of_students = len(names_list)
    no_of_classes = calculate_total_days()
    total_attendance, average_attendance = calculate_attendance_rate(present_list)
    low_attenders = calculate_low_attenders(names_list, no_of_classes)
    print(f"Module: {module_code}")
    print(f"Number of Students: {no_of_students}")
    print(f"Number of Classes: {no_of_classes}")
    print(f"Lowest Attender(s): {low_attenders}")


def calculate_total_days(present_list, absent_list, excuse_list):
    no_of_classes = present_list[0] + absent_list[0] + excuse_list[0]
    return no_of_classes


def calculate_attendance_rate(present_list, absent_list, excuse_list, no_of_classes):
    total_attendance = sum(present_list)
    average_attendance = total_attendance / no_of_classes
    return total_attendance, average_attendance


def calculate_low_attenders(names_list, no_of_classes):
    70_percent_in_days = int(no_of_classes * 0.7)
    for i, student in names_list:






def main():
    name = login()
    module_codes, module_names = get_modules()

    while True:
        menu_choice = menu()
        if menu_choice == 1:
            module_choice = choose_module(module_names, module_codes)
            names_list, present_list, absent_list, excuse_list = get_class_attendance(module_choice)
            take_class_attendance(module_choice, names_list, present_list, absent_list, excuse_list)
        elif menu_choice == 2:
            module_choice = choose_module(module_names, module_codes)
            names_list, present_list, absent_list, excuse_list = get_class_attendance(module_choice)
        else:
            break


main()


