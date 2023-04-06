# Principiul responsabilității unice
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.salary = 0
        
    def calculate_salary(self):
        if self.position == "Manager":
            self.salary = 5000
        elif self.position == "Developer":
            self.salary = 3000
        elif self.position == "Tester":
            self.salary = 2000
        else:
            self.salary = 1000
            
# Principiul deschis-închis
class EmployeeBonus:
    def calculate_bonus(self, employee):
        if isinstance(employee, Manager):
            return employee.salary * 0.2
        elif isinstance(employee, Developer):
            return employee.salary * 0.1
        elif isinstance(employee, Tester):
            return employee.salary * 0.05
        else:
            return 0

class Manager(Employee):
    pass

class Developer(Employee):
    pass

class Tester(Employee):
    pass

# Principiul substituției lui Liskov și principiul segregării interfețelor
class EmployeeRepository:
    def save_employee(self, employee):
        pass
    
    def delete_employee(self, employee):
        pass
    
    def find_employee_by_id(self, employee_id):
        pass
    
    def find_employees_by_position(self, position):
        pass

class BonusCalculator:
    def __init__(self, employee_repository):
        self.employee_repository = employee_repository
        
    def calculate_total_bonus(self):
        employees = self.employee_repository.find_employees_by_position("Manager")
        total_bonus = 0
        bonus_calculator = EmployeeBonus()
        for employee in employees:
            total_bonus += bonus_calculator.calculate_bonus(employee)
        return total_bonus

# Principiul inversiunii dependențelor
employee_repository = EmployeeRepository()
bonus_calculator = BonusCalculator(employee_repository)
total_bonus = bonus_calculator.calculate_total_bonus()
print(f"Total bonus for managers: {total_bonus}")

# În acest exemplu, clasa Employee respectă principiul responsabilității unice, deoarece are o singură responsabilitate: de a calcula salariul unui angajat. Clasele Manager, Developer și Tester extind clasa Employee și nu adaugă funcționalități suplimentare, respectând astfel principiul substituției lui Liskov și principiul segregării interfețelor.

# Clasa EmployeeBonus respectă principiul deschis-închis, deoarece poate fi extinsă cu ușurință pentru a calcula bonusuri pentru noi tipuri de angajați, fără a modifica codul existent.

# Clasa EmployeeRepository respectă principiul inversiunii dependențelor, deoarece clasa BonusCalculator depinde de interfața EmployeeRepository, iar nu de clasa specifică. Aceasta face ca BonusCalculator să poată fi integrat cu ușurință în alte sisteme care implementează aceeași interfață.

# În final, clasa BonusCalculator utilizează clasa EmployeeBonus pentru a calcula bonusurile angajaților, respectând astfel principiul substituției lui Liskov și principiul segregării interfețelor.