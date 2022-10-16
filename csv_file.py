import csv
import os.path

def add_to_csv (file_name, path):
    print("hey")
    with open('dataset.csv','w+', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Absolute path", "Relative path", "Class"])

        number = sum(os.path.isfile(os.path.join(path, f)) for f in os.listdir(path)) + 1
        print(number)

        
def find_path_txt (path_dataset):
    paths_txt = list()
    class_list = ('\good', '\\bad')

    for folder_name in class_list:
        count = len([f for f in os.listdir(path_dataset + folder_name) if os.path.join(path_dataset + folder_name, f)])

        for j in range (0, count):
            path_txt = folder_name + f'\\{(j): 05}' + '.txt'
            print(f'{folder_name}: {(j): 05}')
            paths_txt.append(path_txt[len(path_dataset):])
    
    return paths_txt










if __name__ == "__main__":
    print('Hallo')
    path_dataset = os.path.abspath('dataset')
    print(path_dataset)
    
    paths_txt = find_path_txt(path_dataset)