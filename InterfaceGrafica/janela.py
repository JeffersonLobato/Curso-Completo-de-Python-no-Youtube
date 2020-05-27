from tkinter import *


class Janela:
    def __init__(self, raiz):

        self.img = PhotoImage(file="logo_python.png")
        self.fr1 = Frame(raiz, bg="#ffffff", highlightbackground="red", highlightthickness=3)
        self.fr1.pack()

        self.lb1 = Label(self.fr1, text="Olá mundo!", background="#ffffff", font=("Times", 30, "bold", "italic"))
        self.lb1.pack(side=LEFT)


        self.fr2 = Frame(raiz, bg="#ffffff")
        self.fr2.pack()

        self.bt1 = Button(self.fr2, text="CLIQUE AQUI", background="blue", font=("Times", 30, "bold", "italic"), command=self.muda_label)
        self.bt1["relief"] = RAISED
        self.bt1["border"] = 5
        self.bt1.bind("<Return>", self.muda_label2)
        self.bt1.pack(side=LEFT)


    def muda_label(self):
        self.lb1["text"] = "Deu certo!"
        self.lb_img = Label(raiz, image=self.img)
        self.lb_img.pack()

    def muda_label2(self, event):
        self.lb1["text"] = "Deu certo!"
        self.lb_img = Label(raiz, image=self.img)
        self.lb_img.pack()

raiz = Tk()
Janela(raiz)
raiz.geometry("600x400+600+200")
raiz.title("Aula 50")
raiz.iconbitmap("logo_python.ico")
raiz["bg"] = "#ffffff"

raiz.mainloop()