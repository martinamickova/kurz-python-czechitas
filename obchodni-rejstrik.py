import requests
import json


while True:
    ico_yes_or_no = input("Znáte IČO hledané firmy? (ano/ne) ").strip().lower()  # Určení, podle čeho chceme firmu vyhledávat
    # Část 1 - hledání podle IČO
    if ico_yes_or_no == "ano":
        ico = input("Zadejte požadované IČO: ")
        path_ico = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + ico
        response_ico = requests.get(path_ico)
        company_ico = response_ico.json()
        print(company_ico['obchodniJmeno'])
        print(company_ico['sidlo']['textovaAdresa'])
        break
    # Část 2 - hledání podle názvu
    elif ico_yes_or_no == "ne":
        name = input("Zadejte název hledané firmy: ")
        path_name = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
        headers = {"accept": "application/json",
            "Content-Type": "application/json"}
        data_name = f'{{"obchodniJmeno": "{name}"}}'
        data_name = data_name.encode("utf-8")
        response_name = requests.post(path_name, headers=headers, data=data_name)
        company_name = response_name.json()

        print(f"Nalezeno subjektů: {company_name['pocetCelkem']}")
        for i in company_name['ekonomickeSubjekty']:
            print(i['obchodniJmeno'] + ', ' + i['ico'])
        break
    else:
        print("Zadejte odpověď ve formátu ano/ne.")