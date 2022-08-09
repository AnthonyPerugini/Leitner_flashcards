import os
import json


def main():
    # load an already existing dataset
    path = '/home/spicy/fun/repos/Leitner_flashcards/pickled_stuff'
    data = read_from_file(path)

    
    # option to create a new dataset from another file?




def read_from_file(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            dataset = pickle.load(f)

        return dataset

    else:
        print(f'failed to load path {path}')
        return None


def write_to_file(path):











if __name__=='__main__':
    main()
