class LegacyPrinter:
    def print_document_legacy(self, text):
        return f"Печать (старый формат): {text}"

class ModernPrinter:
    def print_document(self, content):
        return f"Печать (современный формат): {content}"

class PrinterAdapter:
    def __init__(self, legacy_printer):
        self.legacy_printer = legacy_printer

    def print_document(self, content):
        return self.legacy_printer.print_document_legacy(content)
