import os
import shutil

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

            if os.path.exists(full_path):
                print("\nFile Already Exists")
            else:
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
    at_current_dir = input("\nDo You Wanna Remove Directory From Current Directory? (y/n): ")

    if at_current_dir.lower() == "y":
        dir_name = input("\nEnter Directory Name : ")

        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"\nDirectory {dir_name} Removed Successfully")
        else:
            print("\nDirectory Not Found , Please Enter Valid Path")

    else:
        full_path = input("\nEnter Full Directory Path : ")
        if os.path.exists(full_path):
            shutil.rmtree(full_path)
            print(f"\nDirectory {full_path} Removed Successfully")
        else:
            print("\nDirectory Not Found , Please Enter Valid Path")

def copy_file():
    print("\n--- Copy File ---")
    source_loc = input("\nEnter Source Location Of File (full path ) : ")

    if os.path.exists(source_loc):
        destination_loc = input("\nEnter Destination Location To Paste The File ( full path ): ")

        if os.path.exists(destination_loc):
            want_to_copy = input("\nDo You Wanna Cut The File ? (y / n) : ")

            if want_to_copy.lower() == "y":
                destination_path = os.path.join(destination_loc, os.path.basename(source_loc))
                print(f"\nFile Successfully Cutted And Pasted To {shutil.move(source_loc, destination_path)}")
            else:
                print(f"\nFile Successfully Copied To {shutil.copyfile(source_loc, destination_loc)}")
        else:
            print("\nPlease Enter Valid Destination Path")
    else:
        print("\nPlease Enter Valid Source File Path")

def copy_dir():
    print("\n-- Copy Directory ---")
    source_loc = input("\nEnter Source Location Of Directory (full path ) : ")

    if os.path.exists(source_loc):
        destination_loc = input("\nEnter Destination Location To Paste The Directory ( full path ) : ")

        if os.path.exists(destination_loc):
            want_to_copy = input("\nDo You Wanna Cut The Directory ? (y / n) : ")

            if want_to_copy.lower() == "y":
                destination_path = os.path.join(destination_loc, os.path.basename(source_loc))
                print(f"\nDirectory Successfully Cutted And Pasted To {shutil.move(source_loc, destination_path)}")
            else:
                print(f"\nDirectory Successfully Pasted To {shutil.copytree(source_loc, destination_loc)}")

def list_dir_items():
    print("\n--- List Directory Items ---")
    at_current_dir = input("\nDo You Wanna List Current Directory Items? (y/n): ")

    if at_current_dir.lower() == "y":
        dir_path = "."
    else:
        dir_path = input("\nEnter Directory Full Path: ")

    try:
        all_items = os.listdir(dir_path)
        print("Directory Items:")
        for index, item in enumerate(all_items, 1):
            print(f"{index} . {item}")
        print()
    except FileNotFoundError:
        print("\nDirectory Not Found, Please Enter Valid Directory Path")

def rename_file():
    print("\n--- Rename File ---")
    old_name = input("\nEnter the current name of the file (with extension): ")

    if os.path.exists(old_name):
        new_name = input("Enter the new name for the file (with extension): ")

        try:
            os.rename(old_name, new_name)
            print(f"File '{old_name}' successfully renamed to '{new_name}'")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("\nFile Not Found, Please Enter Valid File Name")

def rename_dir():
    print("\n--- Rename Directory ---")
    old_name = input("\nEnter the current name of the directory: ")

    if os.path.exists(old_name):
        new_name = input("Enter the new name for the directory: ")

        try:
            os.rename(old_name, new_name)
            print(f"Directory '{old_name}' successfully renamed to '{new_name}'")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("\nDirectory Not Found, Please Enter Valid Directory Name")

print("\n\n-----------------------------------------")
print("|        File Management System         |")
print("-----------------------------------------")

while True:
    print("\n[ --- --- Main Menu --- --- ]")
    print("\n1 . Create New File")
    print("2 . Create New Directory")
    print("3 . Remove A File")
    print("4 . Remove Directory")
    print("5 . Copy File")
    print("6 . Copy Directory")
    print("7 . List Directory Items")
    print("8 . Rename File")
    print("9 . Rename Directory")
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
        elif choice == 5:
            copy_file()
        elif choice == 6:
            copy_dir()
        elif choice == 7:
            list_dir_items()
        elif choice == 8:
            rename_file()
        elif choice == 9:
            rename_dir()
        elif choice == 0:
            print("\nSystem Exited .......")
            break
        else:
            print("\nInvalid Input, Please Enter a Valid Choice Number")
    else:
        print("\nInvalid Input, Please Enter a Valid Choice Number")
