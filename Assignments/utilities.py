def read_numbers_from_file(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Convert the line to an integer and add it to the list
                number = int(line.strip())
                numbers.append(number)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except ValueError:
        print("One or more lines in the file do not contain valid integers.")
    return numbers


def read_pi(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Convert the line to an integer and add it to the list
                line = line.split()
                for number in line:
                    number = int(number.strip())
                    numbers.append(number)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except ValueError:
        print("One or more lines in the file do not contain valid integers.")
    return numbers
