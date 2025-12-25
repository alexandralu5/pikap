import unittest
from unittest.mock import Mock, patch, MagicMock

class TestWithMockObjects(unittest.TestCase):

    def test_observer_with_mocks(self):
        mock_observer1 = Mock()
        mock_observer2 = Mock()

        from observer_pattern import NewsAgency
        agency = NewsAgency()

        agency.attach(mock_observer1)
        agency.attach(mock_observer2)

        test_news = "Тестовая новость"
        agency.publish_news(test_news)

        expected_message = f"Новая новость: {test_news}"
        mock_observer1.update.assert_called_once_with(expected_message)
        mock_observer2.update.assert_called_once_with(expected_message)

    def test_adapter_with_mock(self):
        mock_legacy_printer = Mock()
        mock_legacy_printer.print_document_legacy.return_value = "Mocked print result"

        from adaptar_pattern import PrinterAdapter
        adapter = PrinterAdapter(mock_legacy_printer)

        result = adapter.print_document("Test content")

        mock_legacy_printer.print_document_legacy.assert_called_once_with("Test content")
        self.assertEqual(result, "Mocked print result")

    def test_factory_with_patch(self):
        with patch('factory_pattern.PDFDocument') as MockPDFDocument:
            mock_instance = Mock()
            mock_instance.open.return_value = "Mocked open"
            mock_instance.save.return_value = "Mocked save"
            MockPDFDocument.return_value = mock_instance

            from factory_pattern import DocumentFactory
            document = DocumentFactory.create_document('pdf')

            MockPDFDocument.assert_called_once()

            self.assertEqual(document.open(), "Mocked open")
            self.assertEqual(document.save(), "Mocked save")

    def test_news_agency_integration_with_mocks(self):
        from observer_pattern import NewsAgency, NewsSubscriber

        agency = NewsAgency()

        real_subscriber = NewsSubscriber("Реальный подписчик")
        mock_subscriber = Mock()

        agency.attach(real_subscriber)
        agency.attach(mock_subscriber)

        agency.publish_news("Интеграционная новость")

        self.assertEqual(len(real_subscriber.received_news), 1)

        mock_subscriber.update.assert_called_once()

if __name__ == '__main__':
    unittest.main()
