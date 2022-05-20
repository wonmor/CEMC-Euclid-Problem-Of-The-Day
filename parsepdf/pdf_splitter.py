'''
CODE WRITTEN BY DEVELOPER JOHN SEONG IN 2022
'''

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

output_dict = {
    'parsepdf/questions_coordinates.json': 'parsepdf/pdf-files-parsed/questions.pdf',
    'parsepdf/answers_coordinates.json': 'parsepdf/pdf-files-parsed/solutions.pdf'
}

class PDFSplitter(object):

    def __init__(self, json_f_dir, pdf_f_dir):
        print("split class running!")

        self.json_f_dir = json_f_dir
        self.pdf_file = PdfFileReader(open(f"{pdf_f_dir}", "rb"))
        self.page_size = (0, 0)
        self.base_coordinates = defaultdict(list)
        self.transformed_coordinates = defaultdict(list)
        self.all_sizes_base_coordinates = []
        self.number_of_tests = 0
        self.page = self.pdf_file.getPage(0)
        self.output = PdfFileWriter()

        # Start splitting...
        self.get_page_size()
        self.start_splitting()

    def get_page_size(self):
        self.page_size = list(self.page.cropBox.getUpperRight())

        print(f'PAGE SIZE: {self.page_size}')

    def start_splitting(self):
        print("split function running!")

        with open(f'{self.json_f_dir}', 'r') as f:
            print("Saving the coordinates...")
            coordinates = json.loads(f.read())

            f.close()
            print(f'Coordinates list: {coordinates}')

        for i in range(1, 11):
            print(f'Cleaning up the values for the key {i}...')
            print(f"Current dict: {coordinates[f'{i}.']}")

            # Convert the Python list to NumPy array for faster and more efficient performance
            all_x_and_y = np.array(coordinates[f'{i}.'])

            # Remove all items that have x-coordinates that exceed 80pt in the NumPy array
            self.base_coordinates[i] = all_x_and_y[np.logical_not(
                all_x_and_y[:, 0] > 80)].tolist()

            # Sort the list by the last element in the nested list
            self.base_coordinates[i].sort(key=lambda x: x[1])
            
            print(f'BASE COORDINATES: {self.base_coordinates}')
            print(f'INDIVIDUAL SIZE OF BASE COORDINATES: {len(self.base_coordinates[i])}')

            self.all_sizes_base_coordinates.append(len(self.base_coordinates[i]))

            for j in range(len(self.base_coordinates[i]) - 1):
                page = self.pdf_file.getPage(j + 1)

                # i => Question Num. | j => Year of Test Index | 1 => y-coordinate of the question num.
                if i >= 2:
                    page.cropBox.upperLeft = (0, self.base_coordinates[i - 1][j][1] + 25)
                    print(f'Cropping upperLeft: {(0, self.base_coordinates[i - 1][j][1] + 25)}')
                else:
                    page.cropBox.upperLeft = (0, self.base_coordinates[i][j][1] - 25)
                    print(f'Exception: Cropping upperLeft: {(0, self.base_coordinates[i][j][1] + 25)}')

                print(self.page_size[1])
                
                try:
                    page.cropBox.lowerRight = (self.page_size[1], self.base_coordinates[i][j][1] - 25)
                    print(f'Cropping lowerRight: {(self.page_size[1], self.base_coordinates[i][j][1] - 25)}')
                except IndexError:
                    print('OOPS! BREAKING FROM THE NESTED LOOP...')
                    break

                self.output.addPage(page)
        
        # Get the most commonly appearing integer in the list as there might have been some miscalculations in the number of tests in the PDF file...
        self.all_sizes_base_coordinates = np.array(self.all_sizes_base_coordinates)

        counts = np.bincount(self.all_sizes_base_coordinates)

        self.number_of_tests = np.argmax(counts)

        print(f"NUMBER OF TESTS: {self.number_of_tests}")
        
        # Write the updated coordinates that only contain question numbers on the JSON file
        with open(f'{self.json_f_dir}', 'w') as f:
            print("Rewriting the JSON file...")
            f.write(json.dumps(self.base_coordinates, indent=4))
            
            print("Rewriting process completed!")
            f.close()

        outputStream = open(output_dict[f'{self.json_f_dir}'], 'wb')

        print("Writing the splitted PDF files...")

        self.output.write(outputStream)

        print("Splitted PDF files saved!")

        outputStream.close()

        # for i in range(1, len(self.base_coordinates)):
            # Shift the y-coordinate up a little for cropping purposes
            # self.trandsformed_coordinates[i] = self.base_coordinates[i] +

        # self.page.mediaBox.lowerRight = (lower_right_new_x_coordinate, lower_right_new_y_coordinate)
        # self.page.mediaBox.lowerLeft = (lower_left_new_x_coordinate, lower_left_new_y_coordinate)
        # self.page.mediaBox.upperRight = (upper_right_new_x_coordinate, upper_right_new_y_coordinate)
        # self.page.mediaBox.upperLeft = (upper_left_new_x_coordinate, upper_left_new_y_coordinate)
