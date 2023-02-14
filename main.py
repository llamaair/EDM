from datetime import date

today = date.today()
print(f"Logged start of EDM at {today}")

from tkinter import *
window=Tk()
# add widgets here

lbl=Label(window, text="EDM", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
window.title('EDM')
window.geometry("300x200+10+20")
window.mainloop()