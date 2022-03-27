from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from collections import defaultdict
from operator import itemgetter
from itertools import chain

'''
PDF SLICE ALGORITHM:
1. IF THE X VALUE IN THE DICTIONARY IS LESS THAN A CERTAIN VALUE,
    AND THE KEY OF IT IS A NUMBER WITH A DOT NEXT TO IT,
    MOVE UP A LITTLE AND SLICE IT!
2. CHECK OUT THE LINK => https://www.techtalk7.com/cropping-pages-of-a-pdf-file/
'''

import json
import numpy as np

class PDFSplitter(object):

    def __init__(self, json_f_dir, pdf_f_dir):
        self.json_f_dir = json_f_dir
        self.pdf_file = PdfFileReader(open(f"{pdf_f_dir}","rb"))
        self.page_size = (0, 0)
        self.base_coordinates = defaultdict(list)
        self.transformed_coordinates = defaultdict(list)
        self.page = self.pdf_file.getPage(0)

    def get_page_size(self):
        self.page_size = self.page.cropBox.getUpperRight()

        print(f'PAGE SIZE: {self.page_size}')

    def start_splitting(self):
        with open(f'{self.json_f_dir}', 'r') as f:
            print("Saving the coordinates...")
            coordinates = json.loads(f.read())
            f.close()
            
        for i in range(1, 10):
            print(f'Cleaning up the values for the key {i}...')
            # Convert the Python list to NumPy array for faster and more efficient performance
            all_x_and_y = np.array(coordinates[i])
            # Remove all items that have x-coordinates that exceed 80pt in the NumPy array
            self.base_coordinates[i] = all_x_and_y[np.logical_not(all_x_and_y[:, 0] > 80)].tolist()

        # Sort the list by the last element in the nested list; chain.from_iterable flattens the 2D list into 1D list
        print("Flattening the 2D list...")
        self.base_coordinates[i] = list(chain.from_iterable([[v1, v2] for v1, v2 in sorted(
            self.base_coordinates.values(), key=itemgetter(1, 2))]))

        # Write the updated coordinates that only contain question numbers on the JSON file
        with open(f'{self.json_f_dir}', 'w') as f:
            print("Rewriting the JSON file...")
            f.write(json.dumps(self.base_coordinates, indent=4))
            f.close()

        # for i in range(1, len(self.base_coordinates)):
            # Shift the y-coordinate up a little for cropping purposes
            # self.transformed_coordinates[i] = self.base_coordinates[i] + 





        # self.page.mediaBox.lowerRight = (lower_right_new_x_coordinate, lower_right_new_y_coordinate)
        # self.page.mediaBox.lowerLeft = (lower_left_new_x_coordinate, lower_left_new_y_coordinate)
        # self.page.mediaBox.upperRight = (upper_right_new_x_coordinate, upper_right_new_y_coordinate)
        # self.page.mediaBox.upperLeft = (upper_left_new_x_coordinate, upper_left_new_y_coordinate)
        

        
