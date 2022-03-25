import pdf_parser

from enum import Enum

class Command(Enum):
    QUESTIONS = 0
    SOLUTIONS = 1

def parse_pdf(command):
    print('PDF parsing sesquence started!')

    match command:
        case Command.QUESTIONS:
            print("Parsing the questions!")
            m_pdf = pdf_parser.PDFParser('questions_coordinates', 'parsepdf/EuclidCombinedContest.pdf')
            m_pdf.get_coordinates()

        case Command.SOLUTIONS:
            m_pdf = pdf_parser.PDFParser('answers_coordinates', 'parsepdf/EuclidCombinedSolutions.pdf')
            m_pdf.get_coordinates()

parse_pdf(Command.QUESTIONS)