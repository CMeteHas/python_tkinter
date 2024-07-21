import tkinter as tk
import random as rd



form=tk.Tk()
form.title("Mete'nin Denemeleri-6")

liste=[]
for i in range(5):
    while len(liste)!=5:
        a=rd.randint(1,50)
        if a not in liste:
            liste.append(a)
def göster():
    label1.config(text=liste,bg="green")
def saydamlaştır():
    form.wm_attributes("-alpha",0.1)
def döndür():
    form.wm_attributes("-alpha",1.0)
def MaxYap():
    form.state("zoomed")
def MinYap():
    form.state("iconic")


label1=tk.Label(form,fg="yellow",bg="yellow",font="Times 20 bold")
label1.pack()


göster=tk.Button(form, text="GÖSTER",fg="purple",bg="pink",font="Times 20 bold",command=göster)
göster.pack()
saydamlaştır=tk.Button(form, text="SAYDAMLAŞTIR",fg="purple",bg="pink",font="Times 20 bold",command=saydamlaştır)
saydamlaştır.pack()
döndür=tk.Button(form, text="DÖNDÜR",fg="purple",bg="pink",font="Times 20 bold",command=döndür)
döndür.pack()
MaxYap=tk.Button(form, text="MAXYAP",fg="purple",bg="pink",font="Times 20 bold",command=MaxYap)
MaxYap.pack()
MinYap=tk.Button(form, text="MİNYAP",fg="purple",bg="pink",font="Times 20 bold",command=MinYap)
MinYap.pack()


form.mainloop()