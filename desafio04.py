import requests

def menu():
    escolha = str(input('Deseja verificar mais algum site?: ')).lower()
    if escolha == 's':
        main()
    elif escolha == 'n':
        print('Encerra')
        return
    else:
        print('opção invalida')
        menu()

def main():
    print('Insira o site para verificar: (separado por virgula) = ')
    urls = str(input()).lower().split(',')
    for url in urls:
        url = url.strip()
        if "." not in url:
            print(url, "url invalid")
        else:
            if "http" not in url:
                url = f"http://{url}"
            try:
                requisicao = requests.get(url)
                if requisicao.status_code == 200:
                    print(url, 'site Online')
                else:
                    print(url, 'Site offline')
            except:
                print(url, ' Erro')
            menu()
main()
