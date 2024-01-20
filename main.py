import os

print("\n\n-----------------------------------------")
print("|        File Management System         |")
print("-----------------------------------------")

while True:

    print("\n[ --- --- Main Menu --- --- ]")

    print("\n1 . Create New File")
    print("2 . Create New Directory")
    print("0 . Exit")

    choice = input("\n_ : ")

    at_current_dir = ""

    if choice.isdigit():

        choice = int(choice)

        if choice == 1:

            print("\n--- Create New File ---")

            at_current_dir = input("\nDo You Wanna Create New File In Current Directory ? (y , n) : ")

            if at_current_dir.lower() == "y":

                file_name = input("\nEnter File Name ( with extension ) : ")
                
                if os.path.exists(file_name):

                    print("\nFile Already Exists")

                else:

                    file = open(file_name,"w")
                    print("\nFile Created Successfully")
                    file.close()
            else:

                dir_location = input("\nEnter Only Directory Location Where You Wanna Create New File : ")

                if os.path.isdir(dir_location):

                    file_name = input("\nEnter New File Name With Extension : ")

                    full_path = os.path.join(dir_location,file_name)

                    file = open(full_path,"w")

                    print("\nFile Created ( File Path ) : " + full_path)

                    file.close()

                else:

                    print("\nirectory Not Found , Please Enter Valid Directory Path")

        elif choice == 2:

            print("\n--- Create New Directory ---")

            at_current_dir = input("\nDo You Wanna Create New Directory At Current Directory ? (y / n) : ")

            if at_current_dir.lower() == "y":

                dir_name = input("\nEnter New Directory Name : ")

                if os.path.exists(dir_name):

                    print("\nSame Named Directory Already Exists ")

                else:

                    os.mkdir(dir_name)

                    print("\nDirectory Created Successfully")

            else:

                root_location = input("\nEnter The Path Till Root Folder Where You Wanna Create A Directory : ")

                if os.path.exists(root_location):

                    dir_name = input("\nEnter Directory Name : ")

                    final_path = os.path.join(root_location,dir_name)

                    if os.path.exists(final_path): 

                        print("\nSame Named Directory Already Exists")

                    else:

                        os.mkdir(final_path)

                        print("\nDirectory Created Successfully ( full path ) " + final_path)

                else:

                    print("\nPlease Enter Valid Path")

            
        elif choice == 0:

            print("\nSystem Exited .......")
            break
        
        else:

            print("\nInvalid Input , Please Enter Valid Choice Number")

    else:

        print("\nInvalid Input , Please Enter Valind Choice Number")
