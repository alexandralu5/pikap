class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Browser:
    def __init__(self, id, name, memory_usage, computer_id):
        self.id = id
        self.name = name
        self.memory_usage = memory_usage
        self.computer_id = computer_id

class BrowserComputer:
    def __init__(self, browser_id, computer_id):
        self.browser_id = browser_id
        self.computer_id = computer_id

computers = [
    Computer(1, "Игровой компьютер"),
    Computer(2, "Рабочий компьютер"),
    Computer(3, "Серверный отдел"),
    Computer(4, "Ноутбук отдела разработки"),
    Computer(5, "Компьютер отдела тестирования")
]

browsers = [
    Browser(1, "Chrome", 512, 1),
    Browser(2, "Firefox", 256, 2),
    Browser(3, "Edge", 300, 3),
    Browser(4, "Opera", 200, 4),
    Browser(5, "Safari", 350, 5),
    Browser(6, "Chrome", 500, 2),
    Browser(7, "Firefox", 280, 1),
    Browser(8, "Edge", 320, 4)
]

browser_computers = [
    BrowserComputer(1, 1), BrowserComputer(1, 2),
    BrowserComputer(2, 2), BrowserComputer(2, 4),
    BrowserComputer(3, 3), BrowserComputer(4, 4),
    BrowserComputer(5, 5), BrowserComputer(6, 1),
    BrowserComputer(6, 2), BrowserComputer(7, 2),
    BrowserComputer(7, 5), BrowserComputer(8, 3),
    BrowserComputer(8, 4)
]

def get_computer_browsers_one_to_many():
    return [(comp, [br for br in browsers if br.computer_id == comp.id])
            for comp in computers]

def get_browser_computers_many_to_many():
    result = []
    for br in browsers:
        computer_ids = [bc.computer_id for bc in browser_computers if bc.browser_id == br.id]
        comps = [comp for comp in computers if comp.id in computer_ids]
        result.append((br, comps))
    return result

def variant_a():
    print("=== ВАРИАНТ A ===")
    print("Предметная область: Браузер-Компьютер\n")

    print("1. Список связанных компьютеров и браузеров:")
    computer_browsers = sorted(get_computer_browsers_one_to_many(), key=lambda x: x[0].name)
    for comp, browsers_list in computer_browsers:
        browser_names = [br.name for br in browsers_list]
        print(f"{comp.name}: {browser_names}")

    print("\n2. Компьютеры с суммарным использованием памяти браузеров:")
    comp_totals = [(comp, sum(br.memory_usage for br in browsers_list))
                   for comp, browsers_list in get_computer_browsers_one_to_many()]

    for comp, total in sorted(comp_totals, key=lambda x: x[1], reverse=True):
        print(f"{comp.name}: {total} МБ")

    print("\n3. Компьютеры с 'отдел' в названии и их браузеры:")
    for comp, browsers_list in get_computer_browsers_one_to_many():
        if "отдел" in comp.name.lower():
            browser_names = [br.name for br in browsers_list]
            print(f"{comp.name}: {browser_names}")

if __name__ == "__main__":
    variant_a()
