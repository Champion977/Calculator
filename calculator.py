def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Nie można dzielić przez 0"
    return x / y

def main():
    print("Prosty kalkulator")
    print("Dostępne operacje: +  -  *  /")

    try:
        x = float(input("Podaj pierwszą liczbę: "))
        op = input("Wybierz operację: ")
        y = float(input("Podaj drugą liczbę: "))

        if op == '+':
            print("Wynik:", add(x, y))
        elif op == '-':
            print("Wynik:", subtract(x, y))
        elif op == '*':
            print("Wynik:", multiply(x, y))
        elif op == '/':
            print("Wynik:", divide(x, y))
        else:
            print("Nieznana operacja.")
    except ValueError:
        print("Błąd: wprowadź liczby.")

if __name__ == "__main__":
    main()
