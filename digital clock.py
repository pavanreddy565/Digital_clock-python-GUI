from tkinter import*
from time import strftime
root=Tk()
root.title('digital clock')
root.geometry('577x330')

H=strftime('%H')
print(H)
#night
if int(H)<6 or int(H)>=18:
    configure_colour='black'
    opp_configure_colour='white'
    bigbutton_colour='#1F1F1F'
    date_colour='#a9a9a9'
    smallbutton_colour='#444444'
 #day   
else:
    configure_colour='#f6fafc'
    opp_configure_colour='black'
    bigbutton_colour='#CBCBCB'
    date_colour='#888888'
    smallbutton_colour='#eeeeee'
root.configure(bg=configure_colour)
def time():
    string=strftime('%I:%M:%S:%p')
    day=strftime('%A')
    Hour,Minute,Second,meridan=string.split(':')
    if int(Hour)<10:
        Hour=Hour[1]
        hour_label.config(text=Hour)
    else:
           hour_label.config(text=Hour)
    day=day[:3]
    Second1=Second[0]
    Second2=Second[1]
    seconds1_label.config(text=Second1)
    seconds2_label.config(text=Second2)
        
    day_label.config(text=day)
    date=strftime('%Y-%m-%d')
    date_label.config(text=date)
 
    minute_label.config(text=Minute)
    merdian_label.config(text=meridan)
    
    root.after(1000,time)
    
hour_label=Button(bg=bigbutton_colour,justify=CENTER ,width=3,height=1,relief=FLAT,bd=5,font=('anonymous pro',100,'bold'),fg=opp_configure_colour,activebackground=configure_colour,activeforeground=opp_configure_colour)
hour_label.place(x=20,y=30)
minute_label=Button(bg=bigbutton_colour,justify=CENTER ,width=3,height=1,relief=FLAT,bd=5,font=('anonymous pro',100,'bold'),fg=opp_configure_colour,activebackground=configure_colour,activeforeground=opp_configure_colour)
minute_label.place(x=292,y=30)
merdian_label=Label(bg=bigbutton_colour,font=('ds-digital',14,'bold'),fg=opp_configure_colour)
merdian_label.place(x=24,y=265)
seconds1_label=Button(bg=smallbutton_colour,font=('ds-digital',16,'bold'),relief=FLAT,fg=opp_configure_colour,activebackground=smallbutton_colour,activeforeground=opp_configure_colour)
seconds1_label.place(x=480,y=255)
seconds2_label=Button(bg=smallbutton_colour,font=('ds-digital',16,'bold'),relief=FLAT,fg=opp_configure_colour,activebackground=smallbutton_colour,activeforeground=opp_configure_colour)
seconds2_label.place(x=518,y=255)
# dark1=Button(bg=bigbutton_colour,width=22,height=0,font=('arial',1),relief=FLAT,activebackground='#1F1F1F',activeforeground='white',state=DISABLED)
# dark1.place(x=480,y=273)
# dark2=Button(bg=bigbutton_colour,width=22,height=0,font=('arial',1),relief=FLAT,activebackground='#1F1F1F',activeforeground='white',state=DISABLED)
# dark2.place(x=518,y=273)
day_label=Label(bg=bigbutton_colour,font=('ds-digital',14,'bold'),fg=opp_configure_colour)
day_label.place(x=490,y=34)
date_label=Label(bg=configure_colour,font=('ds-digital',14,'bold'),fg=date_colour)
date_label.place(x=10,y=0)
# dark=Button(bg=configure_colour,width=1000,height=1,font=('arial',1),relief=FLAT,activebackground=configure_colour,activeforeground='white',state=DISABLED)
# dark.place(x=0,y=167)
time()
#root.attributes('-fullscreen',True)
#root.state('zoomed')

root.mainloop()
