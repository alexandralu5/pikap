import unittest

class BDDStyleTests(unittest.TestCase):

    def test_document_factory_creation_flow(self):
        from factory_pattern import DocumentFactory

        pdf_document = DocumentFactory.create_document('pdf')

        from factory_pattern import PDFDocument
        self.assertIsInstance(pdf_document, PDFDocument)
        self.assertEqual(pdf_document.open(), "Открыт PDF документ")
        self.assertEqual(pdf_document.save(), "PDF документ сохранен")

        word_document = DocumentFactory.create_document('word')

        from factory_pattern import WordDocument
        self.assertIsInstance(word_document, WordDocument)
        self.assertEqual(word_document.open(), "Открыт Word документ")
        self.assertEqual(word_document.save(), "Word документ сохранен")

    def test_adapter_pattern_flow(self):
        from adaptar_pattern import LegacyPrinter, PrinterAdapter

        legacy_printer = LegacyPrinter()
        adapter = PrinterAdapter(legacy_printer)

        result = adapter.print_document("Тестовый документ")

        expected = "Печать (старый формат): Тестовый документ"
        self.assertEqual(result, expected)

    def test_observer_pattern_flow(self):
        from observer_pattern import NewsAgency, NewsSubscriber

        agency = NewsAgency()
        subscriber1 = NewsSubscriber("Иван")
        subscriber2 = NewsSubscriber("Мария")

        agency.attach(subscriber1)
        agency.attach(subscriber2)
        agency.publish_news("Важная новость!")

        self.assertEqual(len(subscriber1.received_news), 1)
        self.assertEqual(len(subscriber2.received_news), 1)

        agency.detach(subscriber1)
        agency.publish_news("Вторая новость")

        self.assertEqual(len(subscriber1.received_news), 1)
        self.assertEqual(len(subscriber2.received_news), 2)

if __name__ == '__main__':
    unittest.main()
