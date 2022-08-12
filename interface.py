import tkinter as tk
from tkinter import ttk
from config import listar_nome_paises, mostrar_moedas, mostrar_populacao, requisicao, parsing, URL_ALL, URL_NAME

texto_da_resposta = requisicao(URL_ALL)
if texto_da_resposta:
    lista_de_paises = parsing(texto_da_resposta)
    if lista_de_paises:
        paises = listar_nome_paises(lista_de_paises)

janela = tk.Tk()

janela.title('API de países')

module_name = tk.Label(text='API | Consulta dados de países', background='orange', foreground='black', width=10, height=2, borderwidth=2, relief='solid', font="-weight bold -size 10")
module_name.grid(row=0, columnspan=3, sticky="NWE", padx=10, pady=10)

type_title = tk.Label(text='Selecione o país:')
type_title.grid(row=1, column=0, sticky="NW", padx=10, pady=10)
type_selection = ttk.Combobox(janela, value=paises, height=10, width=48)
type_selection.grid(row=1, column=1, sticky="NW", padx=10, pady=10)

type_moedas = tk.Label(text='Dados do país:')
type_moedas.grid(row=2, column=0, sticky="NW", padx=10, pady=10)

footer = tk.Label(text="Desenvolvido por: Renato Maldonado", background='blue', foreground='white')
footer.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

def capturar_dados():
    try:
        dados = tk.Label(text='padrão', width=55, height=3, background='black', foreground='white')
        dados.grid(row=2, column=1, columnspan=2, sticky="NW", padx=10, pady=10)
        moeda = mostrar_moedas(type_selection.get())
        populacao = mostrar_populacao(type_selection.get())
        dados = tk.Label(text='padrão', width=55, height=3, background='black', foreground='white')
        dados.grid(row=2, column=1, columnspan=2, sticky="NW", padx=10, pady=10)
        dados["text"] = f'Moeda: {moeda[0]} \n Code: {moeda[1]} \n População: {populacao}'
    except:
        dados = tk.Label(text='Dados não encontrados na api', width=55, height=3, background='red', foreground='white')
        dados.grid(row=2, column=1, columnspan=2, sticky="NW", padx=10, pady=10)

button = tk.Button(text='Enviar', command=capturar_dados)
button.grid(row=1, column=2, sticky="NE", padx=10, pady=10)

janela.mainloop()