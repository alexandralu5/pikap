import unittest
from factory_pattern import DocumentFactory, PDFDocument, WordDocument

class TestFactoryPattern(unittest.TestCase):

    def test_pdf_document_creation(self):
        document = DocumentFactory.create_document('pdf')
        self.assertIsInstance(document, PDFDocument)

    def test_word_document_creation(self):
        document = DocumentFactory.create_document('word')
        self.assertIsInstance(document, WordDocument)

    def test_invalid_document_type(self):
        with self.assertRaises(ValueError):
            DocumentFactory.create_document('excel')

    def test_pdf_document_methods(self):
        document = PDFDocument()
        self.assertEqual(document.open(), "Открыт PDF документ")
        self.assertEqual(document.save(), "PDF документ сохранен")

    def test_word_document_methods(self):
        document = WordDocument()
        self.assertEqual(document.open(), "Открыт Word документ")
        self.assertEqual(document.save(), "Word документ сохранен")

if __name__ == '__main__':
    unittest.main()
