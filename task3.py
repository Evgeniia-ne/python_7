class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


employee = Position('Иван', 'Сидоров', 'Повар', 10000, 20000)
print(employee.get_full_name())
print(employee.position)
print(employee.get_total_income())