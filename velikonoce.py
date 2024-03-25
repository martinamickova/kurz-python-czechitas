velikonoce = {"Datum": "1. dubna 2024",
              "Symboly": ["vajíčko", "pomlázka", "beránek"],
              "Počasí": {"teplota": "20 °C",
                         "oblačnost": "jasno"},
            "Další slovník": {"key": "value"}}

print(velikonoce["Datum"])
print(velikonoce["Symboly"][1])
print(velikonoce["Počasí"]["teplota"])

velikonoce["Počasí"].update({"srážky": "žádné"})  # update přidá položku do slovníku
velikonoce["Symboly"].append("kuřátko")

print(velikonoce["Počasí"])
print(velikonoce["Symboly"])