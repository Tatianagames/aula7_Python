#Calcular o IMC

import tkinter as tk


def imc():

    altura = float(entry_altura.get())
    peso = float(entry_peso.get())
    result = peso / altura ** 2 
    result_label['text'] = f'O seu IMC é: {result}'

janela = tk.Tk()
janela.title("IMC")
janela.geometry('200x400')


label_altura = tk.Label(janela, text="Altura:")
entry_altura = tk.Entry(janela)

label_peso = tk.Label(janela, text="Peso:")
entry_peso = tk.Entry(janela)



result_label = tk.Label(janela, text='')


btn = tk.Button(janela, text="Calcular IMC", font= 'arial', fg='blue', width=15, command=imc )



label_altura.pack()
entry_altura.pack()
label_peso.pack()
entry_peso.pack()

btn.pack()

result_label.pack()

janela.mainloop()





