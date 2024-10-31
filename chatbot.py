def saldacao(nome):
    import random
    frases = ["Ola meu nome e "+nome+". como vai?", "Ola", "Tudo bem com vc?"]
    print(frases[random,randint(0,2])

def recebeTexto():
    texto ="Cliente: " + input("Cliente: ")
    palavraProibida = ["boco","mane","filho da mae"]
    for p in palavraProibida:
        if p in texto:
            print("nao vem nao! me respeite!")
            return recebeTexto()
        return texto

def buscaResposta(nome, texto):
    while True:
        viu = != "":
            if texto,replace("Cliente: ","") == "Tchau":
                print(nome+ ": volte sempre!")
                return "fim"
                elif viu.strip() -- texto.strip():
                    proximalinha - conhecimento.readline()
                    if "chatbot: " in priximalinha
            else:
                print("me desculpe, nao sei o que falar")
                conhecimento.write("\n" + texto)
                resposta_user + input(" o que esperava?\n")
                conhecimento.write("\n" +"Chatbot: "+resposta_user)
                return "Hum..."





def exibeResposta(resposta, nome):
    print(resposta.replace("Chatbot",nome))
    if resposta == "fim"
    return "continua"
