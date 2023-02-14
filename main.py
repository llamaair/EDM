from datetime import date

today = date.today()
print(f"Logged start of EDM at {today}")

from tkinter import *
window=Tk()
# add widgets here

window.title('EDM')
window.geometry("300x200+10+20")
window.mainloop()