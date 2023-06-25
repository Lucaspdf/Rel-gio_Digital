import tkinter as tk
import datetime

class TelaPrincipal:
    def __init__(self, master):
        self.nossaTela = master
        self.iblRelogio = tk.Label(self.nossaTela, font=('Calibri', 26), fg='Purple')
        self.iblRelogio.pack(pady=30, padx=30)
        self.alteracao()

    def alteracao(self):
        now = datetime.datetime.now()
        self.iblRelogio['text'] = now.strftime('%H:%M:%S')
        self.nossaTela.after(1000, self.alteracao)

janelaRaiz = tk.Tk()
TelaPrincipal(janelaRaiz)
janelaRaiz.mainloop()
