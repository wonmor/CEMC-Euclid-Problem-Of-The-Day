from pdfminer.layout import LAParams, LTTextBox, LTText, LTChar, LTAnno
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

import json

# Tutorial used: https://stackoverflow.com/questions/22898145/how-to-extract-text-and-text-coordinates-from-a-pdf-file
# Another tutorial: https://stackoverflow.com/questions/59182694/pdfminer-extraction-for-single-words-lttext-lttextbox


class PDFParser(object):
    def __init__(self, json_file, fp):
        print("__INIT__ RUNNING")
        self.json_file = json_file
        self.fp = open(f'{fp}', 'rb')
        self.locations = {}

    def get_coordinates(self):
        manager = PDFResourceManager()
        laparams = LAParams()
        dev = PDFPageAggregator(manager, laparams=laparams)
        interpreter = PDFPageInterpreter(manager, dev)
        pages = PDFPage.get_pages(self.fp)
        for page in pages:  # Code stops here... Attribute Error: Str has no 'seek' attribute
            interpreter.process_page(page)
            layout = dev.get_result()
            x, y, text = -1, -1, ''
            for textbox in layout:
                if isinstance(textbox, LTText):
                    for line in textbox:
                        for char in line:
                            # If the char is a line-break or an empty space, the word is complete
                            if isinstance(char, LTAnno) or char.get_text() == ' ':
                                if x != -1:
                                    print('PDF PARSING IN PROGRESS: At %r is text: %s' % (
                                        (x, y), text))
                                    self.locations[f'{text}'] = (x, y)
                                x, y, text = -1, -1, ''
                            elif isinstance(char, LTChar):
                                text += char.get_text()
                                if x == -1:
                                    x, y, = char.bbox[0], char.bbox[3]
            # If the last symbol in the PDF was neither an empty space nor a LTAnno, print the word here
            if x != -1:
                print('PDF PARSING IN PROGRESS: At %r is text: %s' %
                      ((x, y), text))
                self.locations[f'{text}'] = (x, y)

        with open(f'{self.json_file}', 'w') as f:
            print('JSON file successfully opened!')
            f.write(json.dumps(self.locations, indent=4, sort_keys=True))
            print('JSON file successfully written!')
            f.close()

        self.fp.close()
