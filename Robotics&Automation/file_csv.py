filename = input("filename: ")
file_type = input("file_type: ")

try_counter = 0
while try_counter < 3:
    try:
        file_handler = open(f'{filename}.{file_type}', 'r')
        for line in file_handler:
            print(line)

        file_handler.close()
    except AttributeError:
        print("Some error occurred\nEnterthe correct filename")
    except FileNotFoundError:
        print("Some error occurred\nEnterthe correct filename")
    else:
        print(file_handler.read())
    finally:
        file_handler.close()