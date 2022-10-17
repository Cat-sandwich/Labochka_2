import os
import csv
import shutil
import random


    
def add_to_csv_and_to_dataset_random_number (path_dataset, paths_txt):
    
    name_folder = "dataset_random_number"

    if not os.path.isdir(name_folder):
            os.mkdir(name_folder)

    path_dataset_random_number = os.path.abspath(name_folder)
    

    with open('dataset_random_number.csv','w+', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Absolute path", "Relative path", "Class"])

        for i in range (1, len(paths_txt)):
            class_txt = str(paths_txt[i]).split('\\')
            
            list_random_number = list(range(1, 10000))
            random.shuffle(list_random_number) 
            
            writer.writerow([f'{ (path_dataset_random_number) }\{ ( str(list_random_number[i]) ) }.txt', f'..\\dataset_random_number\{(str(list_random_number[i])).replace(" ","")}', f'{class_txt[1]}'])
            shutil.copyfile(path_dataset + str(paths_txt[i]),path_dataset_random_number  + '\\'+ str(list_random_number[i]) + '.txt')
              

# '\\good_0000.txt'

def find_path_txt (path_dataset):
    paths_txt = list()
    class_list = ('\good', '\\bad')

    for folder_name in class_list:
        count = len([f for f in os.listdir(path_dataset + folder_name) if os.path.join(path_dataset + folder_name, f)])

        for j in range (0, count):
            path_txt = folder_name +   f'\\{(j): 05}' + '.txt'
            #print(f'{folder_name}: {(j): 05}')
            paths_txt.append(path_txt.replace(" ",""))
    
    return paths_txt


if __name__ == "__main__":

    print('Hallo')
    path_laba_2 = os.getcwd()
    path_dataset = os.path.abspath('dataset')
    print(path_dataset)
    paths_txt = find_path_txt (path_dataset)
    add_to_csv_and_to_dataset_random_number (path_dataset, paths_txt)
    
    print("Готово!")