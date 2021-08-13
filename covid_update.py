import requests
import datetime
from bs4 import BeautifulSoup
from tkinter import *



def update():

    url = "https://www.worldometers.info/coronavirus/"
    r = requests.get(url)
    s = BeautifulSoup(r.text,"html.parser")
    data = s.find_all("div", class_ = "maincounter-number")
    t = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    infected_cases.set(data[0].text.strip())
    death_cases.set(data[1].text.strip())
    recovered_cases.set(data[2].text.strip())
    update_time.set("Last update: " + t)

#--------------------------------------------------GUI-------------------------------------------------------
root = Tk()
root.title("Coronavirus Tracker")
root.config(bg="black")
root.geometry("400x500")

frame_tracker = Frame(root)
frame_tracker.grid()
frame_tracker.config(bg="black")

label_titulo = Label(frame_tracker, text="COVID CASES TRACKER")
label_titulo.grid(padx=25)
label_titulo.config(bg="black", fg="lightgrey", font=("Arial",20,"bold"))

#Total Confirmed
infected_cases = StringVar()
infected_cases.set("-")

label_confirmed_title = Label(frame_tracker, text="Total Confirmed")
label_confirmed_title.grid(pady=10)
label_confirmed_title.config(bg="black", fg="grey", font=("Arial",16,"bold"))

label_confirmed_cases = Label(frame_tracker, textvariable=infected_cases)
label_confirmed_cases.grid(pady=10)
label_confirmed_cases.config(bg="black", fg="red", font=("Arial",16,"bold"))

#Total Death
death_cases = StringVar()
death_cases.set("-")

label_death_title = Label(frame_tracker, text="Total Deaths")
label_death_title.grid(pady=10)
label_death_title.config(bg="black", fg="grey", font=("Arial",16,"bold"))

label_death_cases = Label(frame_tracker, textvariable=death_cases)
label_death_cases.grid(pady=10)
label_death_cases.config(bg="black", fg="lightgrey", font=("Arial",16,"bold"))

#Total Recovered
recovered_cases = StringVar()
recovered_cases.set("-")

label_recovered_title = Label(frame_tracker, text="Total Recovered")
label_recovered_title.grid(pady=10)
label_recovered_title.config(bg="black", fg="grey", font=("Arial",16,"bold"))

label_recovered_cases = Label(frame_tracker, textvariable=recovered_cases)
label_recovered_cases.grid(pady=10)
label_recovered_cases.config(bg="black", fg="green", font=("Arial",16,"bold"))

#Update
update_time = StringVar()
update_time.set("-")

btn_update = Button(frame_tracker, text="Update", command= update)
btn_update.grid(pady=10)
btn_update.config(bg="black", fg="grey", font=("Arial",12,"bold"))

label_recovered_title = Label(frame_tracker, textvariable=update_time)
label_recovered_title.grid(pady=5)
label_recovered_title.config(bg="black", fg="lightgrey", font=("Arial",10))

root.mainloop()
