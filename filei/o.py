try:
    with open('test.txt',mode = 'r+') as my_file:
        print(my_file.read())
        my_file.seek(0)
        print(my_file.read())
except FileNotFoundError as err:
        print("file does not exist")
        raise err
