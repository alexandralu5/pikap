from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

def main():
    N = 11
    print("\n"+"Демонстрация работы с геометрическими фигурами:")
    print("=" * 50 + "\n")

    rectangle = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")

    print(rectangle)
    print(circle)
    print(square)

    print("\n" + "=" * 50)
    print("Демонстрация работы внешнего пакета:")

    try:
        import requests
        response = requests.get('https://httpbin.org/json')
        print(f"Статус код HTTP запроса: {response.status_code}")
        print("Внешний пакет requests работает корректно!")
    except ImportError:
        print("Пакет requests не установлен. Установите его командой: pip install requests")
    except Exception as e:
        print(f"Ошибка при использовании внешнего пакета: {e}")

if __name__ == "__main__":
    main()
