
from tkinter import*
from tkinter import ttk

import requests
 

def get_data():
     
         
 
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7e25b1cd5860f281162542b3d7a3384b").json()
    
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    wt_label1.config(text=str(data["main"]["temp"]-273))
    pre_label1.config(text=data["main"]["pressure"])
    




win=Tk()
win.title('weather app')
win.config(bg='black')
win.geometry('500x570')

name_label=Label(win,text="weather app",font=("Time New Roman",30,"bold"))

name_label.place(x=50,y=50,height=50,width=415)

city_name=StringVar()

list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="weather app",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=50,y=125,height=45,width=415)



w_label=Label(win,text="weather climate",font=("Time New Roman",15))
w_label.place(x=25,y=260,height=50,width=200)

w_label1=Label(win,text="",font=("Time New Roman",15))
w_label1.place(x=250,y=260,height=50,width=200)

wd_label=Label(win,text="weather description",font=("Time New Roman",15))
wd_label.place(x=25,y=330,height=50,width=200)

wd_label1=Label(win,text="",font=("Time New Roman",15))
wd_label1.place(x=250,y=330,height=50,width=200)


wt_label=Label(win,text="temptratutre",font=("Time New Roman",15))
wt_label.place(x=25,y=400,height=50,width=200)


wt_label1=Label(win,text="",font=("Time New Roman",15))
wt_label1.place(x=250,y=400,height=50,width=200)


pre_label=Label(win,text="pressure",font=("Time New Roman",15))
pre_label.place(x=25,y=470,height=50,width=200)

pre_label1=Label(win,text="",font=("Time New Roman",15))
pre_label1.place(x=250,y=470,height=50,width=200)

#adding a submit button 
submit_button=Button(win,text="Submit",font=("Time New Roman",10,"bold"),command=get_data)
submit_button.place(x=200,y=190,height=45,width=80)

win.mainloop()

