import os

def create_file():
    print("\n--- Create New File ---")
    at_current_dir = input("\nDo You Wanna Create New File In Current Directory? (y/n): ")

    if at_current_dir.lower() == "y":
        file_name = input("\nEnter File Name (with extension): ")
        
        if os.path.exists(file_name):
            print("\nFile Already Exists")
        else:
            with open(file_name, "w"):
                pass
            print("\nFile Created Successfully")
    else:
        dir_location = input("\nEnter Only Directory Location Where You Wanna Create New File: ")

        if os.path.isdir(dir_location):
            file_name = input("\nEnter New File Name With Extension: ")
            full_path = os.path.join(dir_location, file_name)

            with open(full_path, "w"):
                pass

            print("\nFile Created (File Path): " + full_path)
        else:
            print("\nDirectory Not Found, Please Enter Valid Directory Path")

def create_directory():
    print("\n--- Create New Directory ---")
    at_current_dir = input("\nDo You Wanna Create New Directory At Current Directory? (y/n): ")

    if at_current_dir.lower() == "y":
        dir_name = input("\nEnter New Directory Name: ")

        if os.path.exists(dir_name):
            print("\nSame Named Directory Already Exists")
        else:
            os.mkdir(dir_name)
            print("\nDirectory Created Successfully")
    else:
        root_location = input("\nEnter The Path Till Root Folder Where You Wanna Create A Directory: ")

        if os.path.exists(root_location):
            dir_name = input("\nEnter Directory Name: ")
            final_path = os.path.join(root_location, dir_name)

            if os.path.exists(final_path):
                print("\nSame Named Directory Already Exists")
            else:
                os.mkdir(final_path)
                print("\nDirectory Created Successfully (full path): " + final_path)
        else:
            print("\nPlease Enter Valid Path")

def remove_file():
    print("\n--- Remove File ---")
    at_current_dir = input("\nDo You Wanna Remove File From Current Directory? (y/n): ")

    if at_current_dir.lower() == "y":
        file_name = input("\nEnter File Name You Wanna Remove With Extension: ")

        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"\nFile {file_name} Removed Successfully")
        else:
            print("\nFile Not Found, Please Enter Valid File Name")
    else:
        full_path = input("\nEnter Full Path Of File (WITH EXTENSION): ")

        if os.path.exists(full_path):
            os.remove(full_path)
            print(f"\nFile {full_path} Removed Successfully")
        else:
            print("\nFile Not Found, Please Enter Valid Path")

def remove_dir():
    print("\n--- Remove Directory ---")
    at_current_dir = input("\nDo You Wanna Remove File From Current Directory? (y/n): ")

    if at_current_dir.lower() == "y":
        dir_name = input("\nEnter Directory Name : ")

        if os.path.exists(dir_name):
            os.rmdir(dir_name)
            print(f"\nDirectory {dir_name} Removed Successfully")
        else:
            print("\nDirectory Not Found , Please Enter Valid Path")

    else:
        full_path = input("\nEnter Full Directory Path : ")
        if os.path.exists(full_path):
            os.rmdir(full_path)
            print(f"\nDirectory {full_path} Removed Successfully")
        else:
            print("\nDirectory Not Found , Please Enter Valid Path")

print("\n\n-----------------------------------------")
print("|        File Management System         |")
print("-----------------------------------------")

while True:
    print("\n[ --- --- Main Menu --- --- ]")
    print("\n1 . Create New File")
    print("2 . Create New Directory")
    print("3 . Remove A File")
    print("4 . Remove Dirctory")    
    print("0 . Exit")

    choice = input("\n_ : ")

    if choice.isdigit():
        choice = int(choice)

        if choice == 1:
            create_file()
        elif choice == 2:
            create_directory()
        elif choice == 3:
            remove_file()
        elif choice == 4:
            remove_dir()
        elif choice == 0:
            print("\nSystem Exited .......")
            break
        else:
            print("\nInvalid Input, Please Enter a Valid Choice Number")
    else:
        print("\nInvalid Input, Please Enter a Valid Choice Number")
