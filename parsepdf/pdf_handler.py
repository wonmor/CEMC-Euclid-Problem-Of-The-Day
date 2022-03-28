import pdf_parser
import pdf_splitter

from enum import Enum


class Command(Enum):
    QUESTIONS = 0
    SOLUTIONS = 1

# PDF COORDINATE SYSTEM: https://www.pdfscripting.com/public/PDF-Page-Coordinates.cfm


state_dict = {
    'QUESTIONS': Command.QUESTIONS,
    'SOLUTIONS': Command.SOLUTIONS,
    'PARSE': pdf_parser.PDFParser,
    'SPLIT': pdf_splitter.PDFSplitter
}


class PDFHandler(object):

    def __init__(self, target):
        # When class is instantiated, immediately start parsing the target file...
        self.target = target
        self.manpulate_pdf(self.target, 'PARSE')

    def split_pdf(self):
        self.manipulate_pdf(self.target, 'SPLIT')

    @staticmethod
    def manipulate_pdf(target, operation):
        print('PDF parsing sesquence started!')

        # Define which file to execute
        command = state_dict[target]

        # Define which function to execute
        func = state_dict[operation]

        match command:
            case Command.QUESTIONS:
                m_pdf = func(
                    'parsepdf/questions_coordinates.json', 'parsepdf/EuclidCombinedContest.pdf')
                m_pdf.get_coordinates()

            case Command.SOLUTIONS:
                m_pdf = func(
                    'parsepdf/answers_coordinates.json', 'parsepdf/EuclidCombinedSolutions.pdf')
                m_pdf.get_coordinates()


# Parse and split both the questions and the solutions sheets
questions_sheet = PDFHandler('QUESTIONS')
questions_sheet.split_pdf()

solutions_sheet = PDFHandler('SOLUTIONS')
solutions_sheet.split_pdf()
