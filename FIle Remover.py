import os
import shutil
import time


def main():
    # initializing the count
    deleted_folders_count = 0
    deleted_files_count = 0

    # Path Name!
    print("Instructions: Please change all \ backSlashes to Forwardslashes /","\n","Warning! This app deletes the entered path permanently if the folder or file is older than 30days so use with care!")
    path = input("Enter the path from which folders&files are to be deleted:")

    # Deletion Time
    days = 30

    # Days to seconds
    seconds = time.time() - (days * 24 * 60 * 60)

    # Is the file there in the path?
    if os.path.exists(path):

        # iterating over every file or folder in the path.
        for root_folder, folders, files in os.walk(path):

            # comparing the age of file or folder
            if seconds >= get_file_or_folder_age(root_folder):
                # removing the folder
                remove_folder(root_folder)
                # incrementing the count
                deleted_folders_count += 1

                # breaking after removing folder
                break
            else:
                # checking folder from the root_folder
                for folder in folders:

                    # folder path
                    folder_path = os.path.join(root_folder, folder)

                    # compairing with days
                    if seconds >= get_file_or_folder_age(folder_path):

                        # calling removefolder function
                        remove_folder(folder_path)
                        # incrementing count
                        deleted_folders_count += 1

                for file in files:

                    # folder path
                    file_path = os.path.join(root_folder, file)

                    # compairing with days
                    if seconds >= get_file_or_folder_age(file_path):

                        # calling removefile function
                        remove_file(file_path)
                        # incrementing count
                        deleted_files_count += 1
        else: 

            #compairing with days
            if seconds >= get_file_or_folder_age(path):

                #calling the file
                remove_file(path)
                deleted_files_count += 1
    else:

        #fileORfolder Not FOund
        print (path,' is not a path in your computer ')
        deleted_files_count += 1

    print("Total Folders deleted: ",deleted_folders_count)
    print("Total Files deleted: ",deleted_files_count)


#Defining the functions called above
def remove_folder(path):

    #removing the folder
    if not shutil.rmtree(path):
        #success
        print(path," is removed successfully")
    
    else:
        #failure 
        print("Unable to delete the ",path)

def remove_file(path):
    #removing file
    if not os.remove(path):
        
        #success
        print(path," is removed successfully")
    else:
        #failure
        print("Unable to delete the ",path)

def get_file_or_folder_age(path):
    #getting creationtime of folder
    #time will be in seconds
    ctime = os.stat(path).st_ctime

    #returning the time
    return ctime

if __name__ == '__main__':
    main() 
#Copyright (c) 2022 Abhinav Anand
        
