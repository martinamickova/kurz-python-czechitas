import requests
import json


ico = input("Zadej IČO požadované firmy: ")
path_ico = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + ico
response_ico = requests.get(path_ico)
firma_ico = response_ico.json()

print(firma_ico['obchodniJmeno'])
print(firma_ico['sidlo']['textovaAdresa'])


name = input("Zadej název hledané firmy: ")
path_name = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
headers = {"accept": "application/json",
    "Content-Type": "application/json"}
data = f'{{"obchodniJmeno": "{name}"}}'
response_name = requests.post(path_name, headers=headers, data=data)
firmy_name = response_name.json()

print(f"Nalezeno subjektů: {firmy_name['pocetCelkem']}")
for i in firmy_name['ekonomickeSubjekty']:
    print(i['obchodniJmeno'], i['ico'])