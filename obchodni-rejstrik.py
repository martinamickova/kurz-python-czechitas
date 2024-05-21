import requests
import json

ico = input("Zadej IČO požadované firmy: ")
path = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + ico
response = requests.get(path)
firma = response.json()

print(firma['obchodniJmeno'])
print(firma['sidlo']['textovaAdresa'])
