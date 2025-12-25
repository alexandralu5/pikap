import unittest
from observer_pattern import NewsAgency, NewsSubscriber

class TestObserverPattern(unittest.TestCase):

    def test_attach_detach(self):
        agency = NewsAgency()
        subscriber = NewsSubscriber("Тест")

        agency.attach(subscriber)
        self.assertIn(subscriber, agency._observers)

        agency.detach(subscriber)
        self.assertNotIn(subscriber, agency._observers)

    def test_notification(self):
        agency = NewsAgency()
        subscriber1 = NewsSubscriber("Подписчик 1")
        subscriber2 = NewsSubscriber("Подписчик 2")

        agency.attach(subscriber1)
        agency.attach(subscriber2)

        agency.publish_news("Тестовая новость")

        self.assertEqual(len(subscriber1.received_news), 1)
        self.assertEqual(len(subscriber2.received_news), 1)
        self.assertIn("Тестовая новость", subscriber1.received_news[0])

    def test_subscriber_update(self):
        subscriber = NewsSubscriber("Тест")
        result = subscriber.update("Сообщение")
        self.assertEqual(result, "Тест получил: Сообщение")

if __name__ == '__main__':
    unittest.main()
