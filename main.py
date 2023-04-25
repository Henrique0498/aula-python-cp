import json
import requests

with open('./files/base_tdspy.json') as file:
    jsonFile = json.load(file)


def remove_com(enumerated_url):
    index, url = enumerated_url
    url_sem_com = url.replace(".com", "")
    return f"{index + 1} - {url_sem_com}"


isValid = False
insertRm = None
optionSelect = None


while not isValid:
    insertRm = input('Digite apenas os números de seu RM: ')

    if insertRm in jsonFile:
        isValid = True
    else:
        print("\nPor favor, digite um RM valido.\n")


isValid = False
urls = jsonFile[insertRm]
resultArray = list(map(remove_com, enumerate(urls)))
result_string = "\n".join(resultArray)


while not isValid:
    print("\nEssas são suas opções:")
    print(result_string)
    optionSelect = int(input("Escolha uma delas usando o número na frente delas: ")) - 1

    if optionSelect >= 0 and optionSelect <= len(urls):
        isValid = True
    else:
        print("\nPor favor, escolha uma opção válida.")


print("\nPegando seus dados na nuvem...")
response = requests.get(f"https://www.{urls[optionSelect]}")
print("Ok, tudo certo, dados pegos com sucesso!\nSalvando os dados...")
file_html = response.content


with open('./files/site.html', 'w') as file_site:
    file_site.write(str(file_html))
print("Dados salvos!")
