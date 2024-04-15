from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float
    
    def __str__(self):
        return f"{self.name}: {self.price} Kč"

@dataclass    
class Pizza(Item):
    ingredients: dict

    def __str__(self):
        return super().__str__() + f", ingredience: {self.ingredients}"

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        self.price += price_per_ingredient
        self.ingredients[ingredient] = quantity 
        return self

@dataclass
class Drink(Item):
    volume: int

    def __str__(self):
        return super().__str__() + f"({self.volume} ml)"


@dataclass
class Order:
    customer_name: str
    delivery_adress: str
    items: list
    status: str = "Nová"

    def __str__(self):
        polozky = []
        for i in self.items:
            polozky.append(str(i.name))
        return f"Objednávka na jméno {self.customer_name} (doručení na adresu: {self.delivery_adress}): {polozky}. Stav objednávky: {self.status}"

    def mark_delivered(self):
        self.status = "Doručeno"

@dataclass
class DeliveryPerson:
    name: str
    phone_number: str
    available: bool = True
    current_order: Item = None

    def __str__(self):
        if self.available == True:
            return f"Doručovatel {self.name} (tel. č. {self.phone_number}) je dostupný."
        else:
            return f"Doručovatel {self.name} (tel. č. {self.phone_number}) je momentálně nedostupný a doručuje objednávku pro {self.current_order.customer_name}."
        

    def complete_delivery(self):
        self.current_order.mark_delivered()
        self.current_order = None
        self.available = True

    def assign_order(self, order):
        if self.available == True:
            self.current_order = order
            self.available = False
        else:
            return "Doručovatel je nedostupný."
        


# Vytvoření instance pizzy a manipulace s ní
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
hawai = Pizza("Hawai", 230, {"rajčata": 150, "sýr": 100, "šunka": 100, "ananas": 100})
# margarita.add_extra("olivy", 50, 10)

# Vytvoření instance nápoje
cola = Drink("Cola", 45, 500)
fanta = Drink("Fanta", 45, 500)
dzus = Drink("džus", 30, 330)

# # Vytvoření a výpis objednávky
order_novak = Order("Jan Novák", "Pražská 123", [margarita, cola])
order_dvorakova = Order("Anna Dvořáková", "Brněnská 45", [hawai, fanta])
order_hrochova = Order("Eva Hrochová", "Jihlavská 67", [hawai, dzus])
# order_novak.mark_delivered()
# print(objednavka_novak)

# # Vytvoření řidiče a přiřazení objednávky
delivery_novotny = DeliveryPerson("Petr Novotný", "777 888 999")
delivery_sova = DeliveryPerson("Karel Sova", "123 456 789")
print(delivery_novotny, delivery_sova)
delivery_novotny.assign_order(order_novak)
delivery_sova.assign_order(order_dvorakova)
delivery_novotny.assign_order(order_hrochova)
# print(delivery_novotny)

# # Dodání objednávky
delivery_novotny.complete_delivery()

delivery_novotny.assign_order(order_hrochova)
delivery_novotny.complete_delivery()

# # Kontrola stavu objednávky po doručení
print(order_novak)
print(order_dvorakova)
print(order_hrochova)
print(delivery_novotny, delivery_sova)
# print(margarita)
# print(cola)