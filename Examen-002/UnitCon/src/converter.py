"""
Módulo de conversión de unidades.
Soporta conversiones de temperatura, longitud y peso.
"""


class UnitConverter:
    """Clase para realizar conversiones entre diferentes unidades."""

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convierte Celsius a Fahrenheit."""
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Convierte Fahrenheit a Celsius."""
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def meters_to_feet(meters: float) -> float:
        """Convierte metros a pies."""
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet: float) -> float:
        """Convierte pies a metros."""
        return feet / 3.28084

    @staticmethod
    def kilograms_to_pounds(kg: float) -> float:
        """Convierte kilogramos a libras."""
        return kg * 2.20462

    @staticmethod
    def pounds_to_kilograms(pounds: float) -> float:
        """Convierte libras a kilogramos."""
        return pounds / 2.20462


def main():  # pragma: no cover
    """Función principal para ejecutar el convertidor de manera interactiva."""
    converter = UnitConverter()
    print("=== Convertidor de Unidades ===")
    print("\n1. Temperatura (Celsius ↔ Fahrenheit)")
    print("2. Longitud (Metros ↔ Pies)")
    print("3. Peso (Kilogramos ↔ Libras)")
    try:
        opcion = input("\nSeleccione una opción (1-3): ")
        valor = float(input("Ingrese el valor a convertir: "))
        if opcion == "1":
            print(f"\n{valor}°C = {converter.celsius_to_fahrenheit(valor):.2f}°F")
            print(f"{valor}°F = {converter.fahrenheit_to_celsius(valor):.2f}°C")
        elif opcion == "2":
            print(f"\n{valor}m = {converter.meters_to_feet(valor):.2f}ft")
            print(f"{valor}ft = {converter.feet_to_meters(valor):.2f}m")
        elif opcion == "3":
            print(f"\n{valor}kg = {converter.kilograms_to_pounds(valor):.2f}lb")
            print(f"{valor}lb = {converter.pounds_to_kilograms(valor):.2f}kg")
        else:
            print("Opción no válida")
    except ValueError:
        print("Error: Ingrese un número válido")


if __name__ == "__main__":
    main()
