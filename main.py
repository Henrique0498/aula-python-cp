import json
import requests
import os

with open('./files/base_tdspy.json') as file:
    jsonFile = json.load(file)


def clear_url(value):
    return value.replace(".com", "").replace(".br", "").replace(".org", "")


def format_list(enumerated_url):
    index, url = enumerated_url
    url_sem_com = clear_url(url)
    return f"{index + 1} - {url_sem_com}"


loopingMain = True
looping = True
insertRm = None
optionSelect = None
restartSystem = True

while loopingMain:
    while looping and restartSystem:
        insertRm = input('\nDigite apenas os números de seu RM: ')

        if insertRm in jsonFile:
            looping = False
        else:
            print("Por favor, digite um RM valido.")

    looping = True
    urls = jsonFile[insertRm]
    resultArray = list(map(format_list, enumerate(urls)))
    result_string = "\n".join(resultArray)

    while looping:
        try:
            print("\nEssas são suas opções:")
            print(result_string)
            optionSelect = int(input("Escolha uma delas usando o número na frente delas: ")) - 1

            if optionSelect >= 0 and optionSelect <= len(urls):
                looping = False
            else:
                print("Por favor, escolha uma opção válida.")
        except Exception as e:
            print("Por favor, digite um valor válido.")
            print(f'Descrição do erro:\n{str(e)}')

    print("\nPegando seus dados na nuvem...")
    response = requests.get(f"https://www.{urls[optionSelect]}")
    print("Salvando os dados...")
    file_html = response.content
    looping = True

    if not os.path.exists("files"):
        os.mkdir("files")

    with open(f'./files/{clear_url(urls[optionSelect])}.html', 'w') as file_site:
        file_site.write(str(file_html))
    print(f'Dados salvos em "./files/{clear_url(urls[optionSelect])}.html."\n')

    while looping:
        print("Deseja recomeçar o processo?")
        finallyProject = input("Digite 's' para Sim e 'n' para Não: ")

        if finallyProject.lower() == "s":
            loopingFromRestart = True

            while loopingFromRestart:
                print("\nVocê deseja colocar um novo RM?")
                restartInput = input("Digite 's' para Sim e 'n' para Não: ")

                if restartInput.lower() == "n":
                    loopingFromRestart = False
                    restartSystem = False
                elif restartInput.lower() == "s":
                    restartSystem = True
                    loopingFromRestart = False
                else:
                    print("Desculpe, não conseguir te entender.")

            looping = False
            loopingMain = True
        elif finallyProject.lower() == "n":
            loopingMain = False
            looping = False
            print("\nObrigado por usar o nosso sistema.\nVolte sempre!")
        else:
            print("Desculpe, não conseguir te entender.\n")

    looping = True
