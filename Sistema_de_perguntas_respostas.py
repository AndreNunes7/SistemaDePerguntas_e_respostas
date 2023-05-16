# Sistema de perguntas e respostas

pergunta01 = [
        {
            "pergunta": "Quanto é 2 + 2 ?: ",
            "Opçoes": [4, 6, 9, 8],
            "respostas": 4,
        },

        {   
            "pergunta": "Quanto é 3 x 3 ?: ",
            "Opçoes": [5, 3, 9, 10],
            "respostas": 9
        },
        {
            "pergunta": "Quantas letras tem a palavra 'Feijão' ?",
            "Opçoes": [6, 5, 7, 6],
            "respostas": 6
        }
 
]

qtd_de_acertos = 0   
for pergunta in pergunta01:
    print('pergunta:',pergunta["pergunta"])
    print()
    
    for indice, opcao in enumerate(pergunta["Opçoes"]):
        print(f"{indice})" ,opcao)
    print()
    
    opcoes = pergunta["Opçoes"]
    

    rsp = input("Escolha uma opção: ")
     
    acertou = False
    rsp_int = None 
    qtd_opcoes = len(opcoes)

    if rsp.isdigit():
        rsp_int = int(rsp)

    if rsp_int is not None:
        if rsp_int >= 0 and rsp_int < qtd_opcoes:
            if opcoes[rsp_int] == pergunta["respostas"]:
                acertou = True
                
    if acertou:
        qtd_de_acertos += 1
        print("Você acertou ✅")
        
    else:
        print("Você errou! ❌")

    print()
print(f"Você acertou {qtd_de_acertos} de {len(pergunta)} perguntas")
