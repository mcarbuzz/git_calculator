from Nedyalku import addition, subtraction, multiplication, division
from Erokhin import modulo, power, sine, cosine
from Frolov import square_root, floor_value, ceil_value, memory_add, memory_clear

def main():
    while True:
        print("\n=== Калькулятор ===")
        print("1: Сложение (+)")
        print("2: Вычитание (-)")
        print("3: Умножение (*)")
        print("4: Деление (/)")
        print("5: Остаток от деления (%)")
        print("6: Возведение в степень (^)")
        print("7: Синус (sin)")
        print("8: Косинус (cos)")
        print("9: Квадратный корень (√)")
        print("10: Округление вниз (floor)")
        print("11: Округление вверх (ceil)")
        print("12: Добавить в память (m+)")
        print("13: Очистить память (mc)")
        print("0: Выход")
        
        choice = input("Выберите операцию: ")
        
        if choice == "0":
            print("Выход из программы.")
            break
        
        if choice in ["1", "2", "3", "4", "5", "6"]:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            if choice == "1":
                print("Результат:", addition(a, b))
            elif choice == "2":
                print("Результат:", subtraction(a, b))
            elif choice == "3":
                print("Результат:", multiplication(a, b))
            elif choice == "4":
                print("Результат:", division(a, b))
            elif choice == "5":
                print("Результат:", modulo(a, b))
            elif choice == "6":
                print("Результат:", power(a, b))
        elif choice in ["7", "8", "9", "10", "11"]:
            a = float(input("Введите число: "))
            if choice == "7":
                print("Результат:", sine(a))
            elif choice == "8":
                print("Результат:", cosine(a))
            elif choice == "9":
                print("Результат:", square_root(a))
            elif choice == "10":
                print("Результат:", floor_value(a))
            elif choice == "11":
                print("Результат:", ceil_value(a))
        elif choice == "12":
            value = float(input("Введите число для добавления в память: "))
            memory_add(value)
            print("Текущее значение памяти:", memory_add(value))
        elif choice == "13":
            memory_clear()
            print("Память очищена.")
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

