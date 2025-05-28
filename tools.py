# Importei varios modulos 
import random as r # Para gerar as senhas
import string as s # Para criar variaveis com todas as letras ou numeros 
import tkinter as tk # a interface

# Funcao main
def main():
    global warnLabel,senhaLabel,caracteresEntry, aba # Variaveis globais

    # ai aqui eu crio os botoes textos e a aba
    aba = tk.Tk()
    aba.title = "Gerador De Senhas"

    # Botoes
    gerarSenhaButton = tk.Button(aba, text="Gerar Senha!", command=criarSenha)
    copiarSenhaButton = tk.Button(aba, text="Copiar Senha!", command=copiarSenha)
    verificarSenhaButton = tk.Button(aba, text="Verificar Senha!", command=verificarSenha)

    # Labels/Textos
    senhaLabel = tk.Label(aba, text="(Senha)")
    warnLabel = tk.Label(aba, text="(Warn)")

    # Entry/Caixa De Entrada
    caracteresEntry = tk.Entry(aba)

    # aqui faz eles aparecer pq antes so criamos
    gerarSenhaButton.pack(side="bottom")
    copiarSenhaButton.pack(side="bottom")
    verificarSenhaButton.pack(side="bottom")
    caracteresEntry.pack(side="bottom")
    senhaLabel.pack(side="top")
    warnLabel.pack(side="top")

    # aqui eu deixo a aba sempre ativa
    aba.mainloop()

# Funcao criarSenha
def criarSenha():
    global senha,simbolos,caracteres # Variaveis globais

    senha = "" # senha vazia para eu usar dps

    # aqui eu crio as variaveis para pegar letras digitos tudo que a senha vai ter
    letras = s.ascii_letters
    numeros = s.digits
    simbolos = "!@#$%&*"

    # junto tudo em uma variavel
    tudo = letras + numeros + simbolos

    # pego o numero de caracteres que a pessoa digitou
    caracteres = caracteresEntry.get()

    # tento 
    try:
        caracteres = int(caracteres) # se a pessoa digitou numero entao virar int
        
        for i in range(caracteres): # loop for que executa quantas vezes a pessoa digitou
            senha += r.choice(tudo) # escolhe 1 letra todas vez q executado

        senhaLabel.config(text=f"{senha}") # mostra a senha na senhaLabel

    except: # se a pessoa digitou letra ou outra coisa
        warnLabel.config(text="Digite Um Número Válido") # mostro um aviso

# Funcao verificarSenha
def verificarSenha():
    pontos = 0 # pontos para verificar se a senha e forte ou nao

    caracteresVerificado = len(caracteres) # pego o numero de caracteres que a pessoa digitou

    # se a senha tiver mais de 10 caracteres aumento 1 ponto
    if caracteresVerificado > 10:
        pontos += 1
    
    # se a senha tiver letra minuscula aumento 1 ponto
    if any(s.islower() for s in senha):
        pontos += 1

    # se a senha tiver letra maiuscula aumento 1 ponto
    if any(s.isupper() for s in senha):
        pontos += 1

    # se a senha tiver numeros aumento 1 ponto
    if any(s.isdigit() for s in senha):
        pontos += 1

    # se a senha tiver simbolos aumento 1 ponto
    if any(s in simbolos for s in senha):
        pontos += 1

    # se a senha tiver menos de 3 pontos ela e fraca
    if pontos < 3:
        warnLabel.config(text="Senha Fraca, Crie Uma Mais Forte")

    # se a senha tiver 3 pontos ela e media
    elif pontos == 3:
        warnLabel.config(text="Senha Média, Crie Uma Mais Forte")

    # se a senha tiver mais de 3 pontos ela e forte
    elif pontos > 3:
        warnLabel.config(text="Senha Forte!")

    return pontos # retorna a quantidade de pontos

# Funcao copiarSenha
def copiarSenha():

    # tento
    try:
        if not senha: # se a senha estiver vazia ou nao existir
            warnLabel.config(text="Gere uma senha primeiro!")
    
        else: # senao estiver vazia
            aba.clipboard_clear() # limpa a area
            aba.clipboard_append(senha) # coloca a senha
            warnLabel.config(text="Senha Copiada Para A Área De Transferência!") # aviso
    except Exception as e: # se der erro
        warnLabel.config(text=f"Erro ao copiar: {e}") # aviso


