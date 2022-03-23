from pdfminer.layout import LAParams, LTText, LTChar, LTAnno
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

# Tutorial used: https://stackoverflow.com/questions/22898145/how-to-extract-text-and-text-coordinates-from-a-pdf-file
# Another tutorial: https://stackoverflow.com/questions/59182694/pdfminer-extraction-for-single-words-lttext-lttextbox

class ManipulatePDF():
    def __init__(self, fp, pages):
        self.fp = fp
        self.pages = pages
        self.locations = []

        self.manager = PDFResourceManager()
        self.laparams = LAParams()

    def get_coordinates(self):
        dev = PDFPageAggregator(self.manager, laparams=self.laparams)
        interpreter = PDFPageInterpreter(self.manager, dev)

        for page in self.pages:
            print('--- Processing ---')
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
                                    print('At %r is text: %s' % ((x, y), text))
                                    x, y, text = -1, -1, ''     
                            elif isinstance(char, LTChar):
                                text += char.get_text()
                                if x == -1:
                                    x, y, = char.bbox[0], char.bbox[3]    
            # If the last symbol in the PDF was neither an empty space nor a LTAnno, print the word here
            if x != -1:
                self.locations.append([x, y, text])

 
def get_questions():
    # Read the question sheet
    global quest_locations

    fp = open('EuclidCombinedContest.pdf', 'rb')
    pages = PDFPage.get_pages(fp)

    questions = ManipulatePDF(fp, pages)
    questions.get_coordinates()

    quest_locations = questions.locations

    print("quest_locations: " + quest_locations)


def get_answers():
    # Read the answer sheet
    global solute_locations

    fp = open('EuclidCombinedSolutions.pdf', 'rb')
    pages = PDFPage.get_pages(fp)

    solutions = ManipulatePDF(fp, pages)
    solutions.get_coordinates()

    solute_locations = solutions.locations
