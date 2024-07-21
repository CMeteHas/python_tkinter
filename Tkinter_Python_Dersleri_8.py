import tkinter as tk
form=tk.Tk()
form.wm_geometry('500x500+250+250')

form.title("Mete'nin Denemeleri-8")
label=tk.Label(text="Geometrik Yöneticiler",fg="blue",bg="red")
label.pack(side=tk.LEFT,fill=tk.Y)
buton=tk.Button(text="Pack()",fg="blue",bg="red")
buton.pack(ipadx=50,ipady=80)




form.mainloop()