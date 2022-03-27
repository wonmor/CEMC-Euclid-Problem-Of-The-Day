import pdf_parser
import pdf_splitter

from enum import Enum


class Command(Enum):
    QUESTIONS = 0
    SOLUTIONS = 1

# PDF COORDINATE SYSTEM: https://www.pdfscripting.com/public/PDF-Page-Coordinates.cfm


class PDFHandler(object):

    def __init__(self, command):
        # Parse the questions and the solutions file
        self.parse_pdf(command)
        self.split_pdf(command)

    def parse_pdf(self, command):
        print('PDF parsing sesquence started!')

        # Supports string parameters as well
        command = Command.QUESTIONS if command == 'QUESTIONS' else Command.SOLUTIONS if command == 'SOLUTIONS' else None

        match command:
            case Command.QUESTIONS:
                print("Parsing the questions!")
                m_pdf = pdf_parser.PDFParser(
                    'parsepdf/questions_coordinates.json', 'parsepdf/EuclidCombinedContest.pdf')
                m_pdf.get_coordinates()

            case Command.SOLUTIONS:
                m_pdf = pdf_parser.PDFParser(
                    'parsepdf/answers_coordinates.json', 'parsepdf/EuclidCombinedSolutions.pdf')
                m_pdf.get_coordinates()

    def split_pdf(self, command):
        print('PDF splitting sequence started!')

        # Supports string parameters as well
        command = Command.QUESTIONS if command == 'QUESTIONS' else Command.SOLUTIONS if command == 'SOLUTIONS' else None

        match command:
            case Command.QUESTIONS:
                m_pdf = pdf_splitter.PDFSplitter(
                    'parsepdf/questions_coordinates.json', 'parsepdf/EuclidCombinedContest.pdf')
                m_pdf.start_splitting()

            case Command.SOLUTIONS:
                m_pdf = pdf_splitter.PDFSplitter(
                    'parsepdf/answers_coordinates.json', 'parsepdf/EuclidCombinedSolutions.pdf')
                m_pdf.start_splitting()

# Parse and split both the questions and the solutions sheets
questions_sheet = PDFHandler('QUESTIONS')
solutions_sheet = PDFHandler('SOLUTIONS')