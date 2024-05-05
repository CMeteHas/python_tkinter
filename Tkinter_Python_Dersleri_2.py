import tkinter as tk

form=tk.Tk()
form.title("Mete'nin Denemeleri-2")
label=tk.Label(form,text="Çağan Mete HAS", fg="green",bg="yellow")
label.pack()
label2=tk.Label(form,text="Uzayda.",fg="red",bg="pink")
label2.pack()
label3=tk.Label(form,text="Çağan Mete HAS Uzayda.",fg="blue",bg="purple")
label3.pack()
label4=tk.Label(form,text="Çağan Mete HAS Uzayda.,Çağan Mete HAS Uzayda.", fg="blue", bg="red",font="Times 15 italic")
label4.pack()
label5=tk.Label(form,text="Çağan Mete HAS Uzayda.,Çağan Mete HAS Uzayda.,Çağan Mete HAS Uzayda.,Çağan Mete HAS Uzayda.", fg="yellow", bg="pink", font="Times 17 bold")
label5.pack()


form.mainloop()