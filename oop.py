class Employee:

    # Atributi same klase i to su atrbuti koji su isti za sve instance, 
    # mada mozemo ih menjati i za odredjenu instancu ako je to potrebno
    # njima pristupamo sa Employee. mada mozemo i sa self ako je to potrebno
    raise_amount = 1.04
    num_of_emps = 0

    # Konstruktor, tu su nam atrubuti instance i to su 
    # atributi koji su razliciti za svaku instancu
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        # svaki put kad se kreira nova instanca ove klase 
        # poziva se __init__ metoda, zato ovde uvecavamo broj radnika
        # i to bas za atribut klase zato ide Employee
        Employee.num_of_emps += 1
    
    # to ce biti atribut koji je tako napisan da ako 
    # promenimo first ili last, da se automatski promeni i email
    @property
    def email(self):
        return self.first + "." + self.last + "@company.com"

    @property
    def fullname(self):
        return self.first + " " + self.last
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleting name!")
        self.first = None
        self.last = None

    # Metoda tj. funkcija koja je vezana za ovu klasu 
    # i ona obavezno prima self kao 1. argument
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Metode sa __..__ su specijalne metode(special method), a
    # imamo i claasmethods(umesto self, tj instance kao prvi argumnet automatski primaju klasu(cls)) 
    # i staticmethods(ne sadrze ni self ni cls) -> npr jel neki dan radni ili neradni
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    
    # za gledanje podataka moze se koristiti i __dict__
    # -> npr print(emp_1.__dict__)
    def __str__(self):
        return "{} {} - {}".format(self.first, self.last, self.email)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string):
        first, last, pay = string.split('-')
        return cls(first, last, pay)


class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def print_emps(self):
        for emp in self.employees:
            print("--> " + emp.fullname)

    def add_emps(self, emp):
        self.employees.append(emp)
    

emp_str_1 = "Isidora-Colic-59000"
emp_1 = Employee.from_string(emp_str_1)

print(emp_1)

dev_1 = Developer("Luka", "Ikodinovic", 60000, 'Java')
dev_2 = Developer("Milica", "Simic", 70000, 'C++')

mgr_1 = Manager('Ivana', 'Rodic', 50000, [dev_2])

mgr_1.add_emps(dev_1)

mgr_1.print_emps()

# Imamo jos i isinstance(instance, class) i issubclass(class, subclass) 
# za proveru jel nesto instanca klase, kao i jel nesto podklsa klase 

# Zakomentarisati veci deo koda -> oznaci + (ctrl + k + c)
# Otkomentarisati veci deo koda -> oznaci + (ctrl + k + u)