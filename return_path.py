from genericpath import isdir
import os


def get_path_dataset ( folder_name, id, class_name ):
   
    return os.path.abspath(f'{(folder_name)}' + f'\\{class_name}' + f'\\{id:04}.txt' )

def get_path_dataset_new ( folder_name, id, class_name ):
   
    return os.path.abspath(f'{(folder_name)}' + f'{class_name}' + f'\\{id:04}.txt' )

def get_path_dataset_new ( folder_name, id, class_name = None):
   
    return os.path.abspath(f'{(folder_name)}' + f'\\{id:04}.txt' )



if __name__ == "__main__":

    class_name = ['good', 'bad']

    path_laba_2 = os.getcwd()
    contend = os.listdir(path_laba_2)
    for folder_name in contend:
        if os.path.isdir(folder_name) and folder_name.find('.', 0, 1) :
            print(folder_name)
