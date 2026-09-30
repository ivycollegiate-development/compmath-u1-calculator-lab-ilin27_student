"""Calculator with Guardrails — Lab Starter.

This calculator WORKS but has NO GUARDRAILS.
Your job: make it survive bad input and division by zero.
"""

MENU = """
Choose an operation:
  1) add (+)
  2) subtract (-)
  3) multiply (*)
  4) divide (/)
  5) Fahrenheit -> Celsius
  6) Celsius -> Fahrenheit
  7) Celsius -> Kelvin
  8) km -> miles
  9) miles -> km
  10) kg -> lbs
  11) lbs -> kg
  q) quit
"""

KM_PER_MILE = 1.609344
KG_PER_LB = 0.45359237
MAX_VALUE = 1e15
ABSOLUTE_ZERO_C = -273.15


def is_too_big(n):
    return abs(n) > MAX_VALUE


def is_below_absolute_zero(celsius_value):
    return celsius_value < ABSOLUTE_ZERO_C


def get_number(prompt):
    """Ask the user for a number."""
    while True:
        raw = input(prompt)
        try:
            value = float(raw)
        except ValueError:
            print(f"'{raw}' is not a number. Try again.")
            continue
        if is_too_big(value):
            print("absurdly large — refusing to compute. Try again.")
            continue
        return value


def divide(a, b):
    """Return a / b."""
    if b == 0:
        print("Cannot divide by zero.")
        return None
    return a / b


def c_to_f(c):
    return c * 9 / 5 + 32


def f_to_c(f):
    return (f - 32) * 5 / 9


def c_to_k(c):
    return c + 273.15


def km_to_miles(km):
    return km / KM_PER_MILE


def miles_to_km(miles):
    return miles * KM_PER_MILE


def kg_to_lbs(kg):
    return kg / KG_PER_LB


def lbs_to_kg(lbs):
    return lbs * KG_PER_LB


def main():
    print("=== Calculator v0 (no guardrails) ===")
    while True:
        print(MENU)
        choice = input("> ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"):
            print("Please pick 1-11, or q.")
            continue

        a = get_number("First number: ")

        # 溫度轉換處理 (5, 6, 7)
        if choice in ("5", "6", "7"):
            celsius = f_to_c(a) if choice == "5" else a
            if is_below_absolute_zero(celsius):
                print(f"{celsius:.2f} C is below absolute zero -- refusing.")
                continue
            if choice == "5":
                result = celsius
            elif choice == "6":
                result = c_to_f(a)
            else:
                result = c_to_k(a)
            print(f"Result: {result}")
            continue

        # 距離與重量轉換處理 (8, 9, 10, 11)
        if choice in ("8", "9", "10", "11"):
            if choice == "8":
                result = km_to_miles(a)
            elif choice == "9":
                result = miles_to_km(a)
            elif choice == "10":
                result = kg_to_lbs(a)
            else:
                result = lbs_to_kg(a)
            print(f"Result: {result}")
            continue

        # 雙數運算 (1, 2, 3, 4)
        b = get_number("Second number: ")

        if choice == "1":
            result = a + b
        elif choice == "2":
            result = a - b
        elif choice == "3":
            result = a * b
        elif choice == "4":
            result = divide(a, b)

        if result is not None:
            print(f"Result: {result}")


if __name__ == "__main__":
    main()