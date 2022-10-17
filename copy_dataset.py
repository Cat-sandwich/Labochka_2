import os
import csv
import shutil


def copy_dataset_to_new_dataset(path_dataset, path_txt_old, path_txt_new):

    name_folder = "new_dataset"

    if not os.path.isdir(name_folder):
        os.mkdir(name_folder)
    
    for i in range(1, len(path_txt_old)):
        print(path_dataset + str(path_txt_old[i]))
        print( name_folder + str(path_txt_new[i]))
        shutil.copyfile(path_dataset + str(path_txt_old[i]), name_folder + str(path_txt_new[i]))
    
    


def find_path_txt (path_dataset, delimiter):
    paths_txt = list()
    class_list = ('\good', '\\bad')

    for folder_name in class_list:
        count = len([f for f in os.listdir(path_dataset + folder_name) if os.path.join(path_dataset + folder_name, f)])

        for j in range (0, count):
            path_txt = folder_name + delimiter +  f'{(j): 05}' + '.txt'
            #print(f'{folder_name}: {(j): 05}')
            paths_txt.append(path_txt.replace(" ",""))
    
    return paths_txt


if __name__ == "__main__":

    print('Hallo')
    path_laba_2 = os.getcwd()
    path_dataset = os.path.abspath('dataset')
    print(path_dataset)
    path_txt_old = find_path_txt (path_dataset, '\\')
    path_txt_new = find_path_txt (path_dataset, '_')
    copy_dataset_to_new_dataset(path_dataset, path_txt_old, path_txt_new)
    print("Готово!")