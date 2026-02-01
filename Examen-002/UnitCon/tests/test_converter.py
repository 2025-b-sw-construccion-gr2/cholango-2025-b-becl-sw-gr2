"""
Tests unitarios para el módulo converter.
"""

from src.converter import UnitConverter


class TestTemperatureConversion:
    """Tests para conversiones de temperatura."""

    def test_celsius_to_fahrenheit(self):
        """Test conversión Celsius a Fahrenheit."""
        assert UnitConverter.celsius_to_fahrenheit(0) == 32
        assert UnitConverter.celsius_to_fahrenheit(100) == 212
        assert round(UnitConverter.celsius_to_fahrenheit(37), 2) == 98.60

    def test_fahrenheit_to_celsius(self):
        """Test conversión Fahrenheit a Celsius."""
        assert UnitConverter.fahrenheit_to_celsius(32) == 0
        assert UnitConverter.fahrenheit_to_celsius(212) == 100
        assert round(UnitConverter.fahrenheit_to_celsius(98.6), 2) == 37.0


class TestLengthConversion:
    """Tests para conversiones de longitud."""

    def test_meters_to_feet(self):
        """Test conversión metros a pies."""
        assert round(UnitConverter.meters_to_feet(1), 2) == 3.28
        assert round(UnitConverter.meters_to_feet(10), 2) == 32.81

    def test_feet_to_meters(self):
        """Test conversión pies a metros."""
        assert round(UnitConverter.feet_to_meters(3.28084), 2) == 1.0
        assert round(UnitConverter.feet_to_meters(32.8084), 2) == 10.0


class TestWeightConversion:
    """Tests para conversiones de peso."""

    def test_kilograms_to_pounds(self):
        """Test conversión kilogramos a libras."""
        assert round(UnitConverter.kilograms_to_pounds(1), 2) == 2.20
        assert round(UnitConverter.kilograms_to_pounds(10), 2) == 22.05

    def test_pounds_to_kilograms(self):
        """Test conversión libras a kilogramos."""
        assert round(UnitConverter.pounds_to_kilograms(2.20462), 2) == 1.0
        assert round(UnitConverter.pounds_to_kilograms(22.0462), 2) == 10.0


class TestEdgeCases:
    """Tests para casos especiales."""

    def test_zero_values(self):
        """Test con valores cero."""
        assert UnitConverter.meters_to_feet(0) == 0
        assert UnitConverter.kilograms_to_pounds(0) == 0

    def test_negative_values(self):
        """Test con valores negativos."""
        assert UnitConverter.celsius_to_fahrenheit(-40) == -40
        assert round(UnitConverter.meters_to_feet(-5), 2) == -16.40
