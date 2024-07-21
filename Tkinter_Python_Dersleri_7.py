import tkinter as tk

form=tk.Tk()
form.title("Mete'nin Denemeleri-7")
form.wm_geometry('500x450+250+250')

entry=tk.Entry(fg="red", bg="yellow")
entry.pack(side=tk.RIGHT)
entry2=tk.Entry(fg="yellow", bg="red")
entry2.pack(side=tk.LEFT)


form.mainloop()