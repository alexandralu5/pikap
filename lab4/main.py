from factory_pattern import DocumentFactory
from adaptar_pattern import LegacyPrinter, PrinterAdapter, ModernPrinter
from observer_pattern import NewsAgency, NewsSubscriber

def demonstrate_factory_pattern():
    print("=== ФАБРИЧНЫЙ МЕТОД  ===")

    pdf_doc = DocumentFactory.create_document('pdf')
    word_doc = DocumentFactory.create_document('word')

    print(f"PDF документ: {pdf_doc.open()} -> {pdf_doc.save()}")
    print(f"Word документ: {word_doc.open()} -> {word_doc.save()}")

    try:
        DocumentFactory.create_document('excel')
    except ValueError as e:
        print(f"Ошибка: {e}")

def demonstrate_adapter_pattern():
    print("\n=== АДАПТЕР ===")

    legacy_printer = LegacyPrinter()
    modern_printer = ModernPrinter()
    adapter = PrinterAdapter(legacy_printer)

    print("Современный принтер:", modern_printer.print_document("Документ 1"))
    print("Адаптер для старого принтера:", adapter.print_document("Документ 2"))
    print("Старый принтер напрямую:", legacy_printer.print_document_legacy("Документ 3"))

def demonstrate_observer_pattern():
    print("\n=== НАБЛЮДАТЕЛЬ  ===")

    agency = NewsAgency()

    subscribers = [
        NewsSubscriber("Иван Иванов"),
        NewsSubscriber("Мария Петрова"),
        NewsSubscriber("Алексей Сидоров")
    ]

    for subscriber in subscribers[:2]:
        agency.attach(subscriber)
        print(f"{subscriber.name} подписался на новости")

    print("\n--- Публикация первой новости ---")
    agency.publish_news("Python 3.12 выпущен!")

    agency.attach(subscribers[2])
    print(f"\n{subscribers[2].name} подписался на новости")

    print("\n--- Публикация второй новости ---")
    agency.publish_news("Новый фреймворк для тестирования")

    agency.detach(subscribers[1])
    print(f"\n{subscribers[1].name} отписался от новостей")

    print("\n--- Публикация третьей новости ---")
    agency.publish_news("Итоги конференции PyCon")

    print("\n--- Статистика полученных новостей ---")
    for subscriber in subscribers:
        print(f"{subscriber.name}: {len(subscriber.received_news)} новостей")

if __name__ == "__main__":
    demonstrate_factory_pattern()
    demonstrate_adapter_pattern()
    demonstrate_observer_pattern()
