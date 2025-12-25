from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def save(self):
        pass

class PDFDocument(Document):
    def open(self):
        return "Открыт PDF документ"

    def save(self):
        return "PDF документ сохранен"

class WordDocument(Document):
    def open(self):
        return "Открыт Word документ"

    def save(self):
        return "Word документ сохранен"

class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == 'pdf':
            return PDFDocument()
        elif doc_type == 'word':
            return WordDocument()
        else:
            raise ValueError(f"Неизвестный тип документа: {doc_type}")
