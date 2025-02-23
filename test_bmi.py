import pytest
from bmi_program import calculate_bmi

def test_calculate_bmi():
    assert calculate_bmi(150, 5, 7) == (23.5, "Normal weight")
    assert calculate_bmi(100, 5, 7) == (15.7, "Underweight")
    assert calculate_bmi(180, 5, 7) == (28.2, "Overweight")
    assert calculate_bmi(220, 5, 7) == (34.5, "Obese")

def test_calculate_bmi_invalid_height():
    with pytest.raises(ZeroDivisionError):
        calculate_bmi(150, 0, 0)
