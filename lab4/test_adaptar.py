import unittest
from adaptar_pattern import LegacyPrinter, ModernPrinter, PrinterAdapter

class TestAdapterPattern(unittest.TestCase):

    def test_modern_printer(self):
        printer = ModernPrinter()
        result = printer.print_document("Тест")
        self.assertEqual(result, "Печать (современный формат): Тест")

    def test_legacy_printer(self):
        printer = LegacyPrinter()
        result = printer.print_document_legacy("Тест")
        self.assertEqual(result, "Печать (старый формат): Тест")

    def test_adapter(self):
        legacy_printer = LegacyPrinter()
        adapter = PrinterAdapter(legacy_printer)
        result = adapter.print_document("Тест")
        self.assertEqual(result, "Печать (старый формат): Тест")

if __name__ == '__main__':
    unittest.main()
