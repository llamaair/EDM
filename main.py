from tkinter import *
window=Tk()
# add widgets here
btn=Button(window, text="Update", fg='blue')
btn.place(x=80, y=100)
lbl=Label(window, text="EDM", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
window.title('EDM')
window.geometry("300x200+10+20")
window.mainloop()