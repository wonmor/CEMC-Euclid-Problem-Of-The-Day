'''
CODE WRITTEN BY DEVELOPER JOHN SEONG IN 2022
'''

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
        PDFHandler.manipulate_pdf(self.target, 'PARSE')

    @staticmethod
    def manipulate_pdf(target, operation):
        # Define which file to execute
        command = state_dict[target]

        # Define which function to execute
        func = state_dict[operation]

        match command:
            case Command.QUESTIONS:
                m_pdf = func(
                    'parsepdf/questions_coordinates.json', 'parsepdf/EuclidCombinedContest.pdf')

            case Command.SOLUTIONS:
                m_pdf = func(
                    'parsepdf/answers_coordinates.json', 'parsepdf/EuclidCombinedSolutions.pdf')


# Parse and split both the questions and the solutions sheets

print("PARSING AND SPLITTING QUESTIONS.PDF!")

questions_sheet = PDFHandler('QUESTIONS')
questions_sheet.manipulate_pdf('QUESTIONS', 'SPLIT')

# print("PARSING AND SPLITTING SOLUTIONS.PDF!")
# solutions_sheet = PDFHandler('SOLUTIONS')
# solutions_sheet.manipulate_pdf('SOLUTIONS', 'SPLIT')
