"""Example Class for pytest testing"""


class Employee:
    """Model an employee"""

    def __init__(self, first_name: str, last_name: str, annual_salary: float) -> None:
        """inits the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount: float = 5000.0) -> None:
        """Give a raise to this employee"""
        self.annual_salary += raise_amount
