'''
CODE WRITTEN BY DEVELOPER JOHN SEONG IN 2022
'''

import itertools
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from collections import defaultdict

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
        self.page_count = self.pdf_file.numPages
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

            # Remove all items that have x-coordinates that exceed 76pt or is lower than 68pt in the NumPy array
            self.base_coordinates[i] = all_x_and_y[np.logical_and((
                all_x_and_y[:, 0] < 74), (all_x_and_y[:, 0] > 70))].flatten().tolist()

        print(self.base_coordinates)

        for i in range(1, 11):
            page_num = self.base_coordinates[i][2]
            self.page = self.pdf_file.getPage(page_num)

            print(f'Crop at page {page_num}')
            print(f'self.page_count: {self.page_count}')

            # First question on the page; when the y-coordinate of previous question is smaller than the current one meaning that the current question is starting from a new page...
            if self.base_coordinates[i][1] > 350:
                self.page.cropBox.upperLeft = (0, self.base_coordinates[i][1] + 25)
                print((0, self.base_coordinates[i][1] + 25))
                self.page.cropBox.lowerRight = (self.page_size[0], self.base_coordinates[i + 1][1] + 12.5)

            # Last question on the page...
            elif (page_num == self.page_count - 1 and self.base_coordinates[i][1] < 400) or self.base_coordinates[i][1] < 400:
                self.page.cropBox.upperLeft = (0, self.base_coordinates[i][1] + 25)
                self.page.cropBox.lowerRight = (self.page_size[0], self.page_size[1])
            
            else:
                self.page.cropBox.upperLeft = (0, self.base_coordinates[i - 1][1] + 25)
                self.page.cropBox.lowerRight = (self.page_size[0], self.base_coordinates[i + 1][1] - 25)

            self.output.addPage(self.page)
        
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