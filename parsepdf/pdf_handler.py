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
            m_pdf = pdf_parser.PDFParser('parsepdf/questions_coordinates.json', 'parsepdf/EuclidCombinedContest.pdf')
            m_pdf.get_coordinates()

        case Command.SOLUTIONS:
            m_pdf = pdf_parser.PDFParser('parsepdf/answers_coordinates.json', 'parsepdf/EuclidCombinedSolutions.pdf')
            m_pdf.get_coordinates()

# Parse the questions and solutions file
parse_pdf(Command.QUESTIONS)
parse_pdf(Command.SOLUTIONS)