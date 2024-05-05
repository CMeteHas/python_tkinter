import tkinter as tk
form=tk.Tk()
form.title("Mete'nin Denemeleri-5")
def topla():
    print(3132+5698)
def çarp():
    print(3132*5698)

dugme=tk.Button(form,text="Topla",fg="white",bg="red",command=topla)
dugme.pack()
dugme2=tk.Button(form,text="Çarp",fg="green",bg="pink",command=çarp)
dugme2.pack()



form.mainloop()