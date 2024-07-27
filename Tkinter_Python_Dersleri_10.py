import tkinter as tk
form=tk.Tk()
form.wm_geometry('500x300')
form.title("Mete'nin Denemeleri-10")
def verial():
    etiket['text']=entry.get()
def sil():
    etiket['text']=""
    entry.delete(0,"end")
    entry2.delete(0,"end")



entry=tk.Entry()
entry.pack()
entry2=tk.Entry(show="*")
entry2.pack()
buton=tk.Button(text="Verileri Al",fg="red",bg="green",command=verial)
buton.pack()
buton2=tk.Button(text="Veirleri Sil",fg="red",bg="green",command=sil)
buton2.pack()

etiket=tk.Label(text="Verilerin Buraya Getirilmesi Lazim")
etiket.pack()

form.mainloop()