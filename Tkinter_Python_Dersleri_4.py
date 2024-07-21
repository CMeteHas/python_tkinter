import tkinter as tk

form=tk.Tk()
form.title("Mete'nin Denemeleri-4")

label1=tk.Label(form,text="Mete'nin Denemeleri-4")
label1.pack()

form.state("normal")
#form.state("zoomed")
#form.state("iconic")
form.wm_attributes("-alpha",0,1)

form.mainloop()