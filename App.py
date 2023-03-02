import customtkinter
import tkinter
from tkinter import *
from tkcalendar import DateEntry
import time
from PIL import Image
import pandas as pd
import numpy as np
from datetime import date

##                                  ---Creating functionality first, minor graphic modifications included---
## 28/2/2023 - Widget slots made, colors standardized to variables
##           - RPM dropdown added
##           - History set initialized and displayed
## 27/2/2023 - Supervisor Screen frame designed + return button with confirmation 
## 25/2/2023 - Home screen frame designed with supervisor login and exit buttons, white patch on right side of screen to display information
##           - Login Screen integrated with supervisor login button, detects valid username password, can go back to home screen 
global History_Set
db_count=0
History_set = pd.read_excel(r'Test_Set.xlsx')

for hist_setup in range (0,10):                                          # Adds 5 extra rows to History_set dataframe
    History_set.loc[History_set.shape[0]] = [None, None, None, None]    # Avoids index out of bounds errors


class LoginScreen(customtkinter.CTkFrame):   #Each Screen is a different CTK Frame
    def backbutton(self,master):            #self relates to frame, master relates to App(). 
        #self.pack_forget()                  #pack_forget allows for the frame to be packed again, while destroy() requires another initialization of the frame
        master.HomeFrame()                  #after frame is removed, go back to home frame
        
    
    def logincheck(self,master,username_entry, password_entry):
        
        if username_entry.get() == 'ahmad' and password_entry.get() == '54321':    # enter password here, or replace with variable linked to an excel doc, etc.
            username_entry.delete(0,END),password_entry.delete(0,END) # deletes text so it wont show on another login attempt                                                                                         #|
            ## Here is where the supervisor frame call would be, and pack_forget login frame
            
            master.SVFrame()
            
        else:
            entry_label = customtkinter.CTkLabel(self, text = 'Invalid username and/or password, please try again', text_color='maroon', font=('Segoe UI', 15)) 
            entry_label.place(x=796, y= 415)
            entry_label.after(3000, lambda: entry_label.destroy())      #can use destroy() here since it is initialized above^ on every iteration - typically keep pack() for frames only
    

    
    def __init__(self, master, **kwargs):                               #arguments here would be frame size
        super().__init__(master, **kwargs)
        mainscreen = customtkinter.CTkLabel(self, text=None, fg_color='#252526', height=1080, width=1920, corner_radius = 0)
        mainscreen.place(x=0, y=0)
        logo = customtkinter.CTkImage(dark_image= Image.open(r"RITBIO_DARK.png"),size=(700,700))   # change logo here - insert path if not in same folder, r" converts to raw string
        logobutton = customtkinter.CTkButton(self,image= logo,bg_color= '#252526',fg_color="#252526", text= None, hover=False)
        logobutton.place( x=600, y=-50)

        notice_label = customtkinter.CTkLabel(self, text='-S U P E R V I S O R   L O G I N-',bg_color= '#252526',fg_color="#252526", text_color='white')      
        notice_label.configure(font=('Segoe UI', 15))
        notice_label.place(x=860, y= 950)

        #username_label=customtkinter.CTkLabel(self, text='Username',bg_color= '#252526',fg_color="#252526", text_color='white')
        #username_label.configure(font=('Segoe UI', 26))
        #username_label.place(x=761, y=450)

        #password_label=customtkinter.CTkLabel(self, text='Password',bg_color= '#252526',fg_color="#252526", text_color='white')
        #password_label.configure(font=('Segoe UI', 26))
        #password_label.place(x=761, y=500)
        username_entry = customtkinter.CTkEntry(master=self,placeholder_text='Username', fg_color='#252526', font= ('Segoe UI', 15), text_color='#a3adb7', corner_radius=3,width=400,height=40,bg_color= '#252526')
        username_entry.place(x=760, y=450)
        username_entry.bind('<Return>', lambda event:self.logincheck(master,username_entry, password_entry)) #binds return key to login press, as per login standards

        password_entry = customtkinter.CTkEntry(master=self, placeholder_text='Password',fg_color='#252526', font= ('Segoe UI', 15), text_color='#a3adb7', corner_radius=3,width=400,height=40,show="•",bg_color= '#252526')
        password_entry.place(x=760, y=500)
        password_entry.bind('<Return>', lambda event:self.logincheck(master,username_entry, password_entry)) #same as above

        backarrows = customtkinter.CTkImage(dark_image= Image.open(r"backbtn.png"),size=(100,100))   # change logo here - insert path if not in same folder, r" converts to raw string
        backbtn = customtkinter.CTkButton(master=self, command =lambda:self.backbutton(master), width=120, hover_color='maroon',bg_color= '#252526', fg_color='#252526', image= backarrows, text=None)
        backbtn.place(x=10, y=10)

        loginbt = customtkinter.CTkButton(master=self, text="Login", width=400,height=30, command=lambda: self.logincheck(master,username_entry, password_entry),bg_color= '#252526',corner_radius=5)
        loginbt.place(x=760,y=550 )

class HomeScreen(customtkinter.CTkFrame):
    def exitbutton(self,master):
        master.destroy()
    def sv_login(self,master):
        master.LoginFrame()
    def newmethodbtn(self,master):
        master.NewMethodFrame()

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global History_set

        logo = customtkinter.CTkImage(dark_image= Image.open(r"RITBIO.png"),size=(400,400))   # change logo here - insert path if not in same folder, r" converts to raw string
        logobutton = customtkinter.CTkButton(self,image= logo,bg_color= 'transparent',fg_color="transparent", text= None, hover=False)
        logobutton.place( x=-70, y=-100)

        ## left panel
        exitbtn = customtkinter.CTkButton(master=self, text="Exit", text_color= 'white', command=lambda:self.exitbutton(master), 
                                          width=280, height = 30, hover_color='maroon',bg_color= 'transparent', corner_radius= 5).place(x=10, y=1030)
        
        sv_loginbtn = customtkinter.CTkButton(master=self, text="Supervisor Login", text_color= 'White', command = lambda:self.sv_login(master), 
                                              width=280, height = 30, corner_radius= 5).place(x=10, y=990)
        
        homebtn = customtkinter.CTkButton(master=self, text="Home", text_color= 'White', 
                                              width=280, height = 30, corner_radius= 5, fg_color='#1e1e1e', hover=False).place(x=10, y=200)
        
        history_entrybtn = customtkinter.CTkButton(master=self, text="Record New Method", text_color= 'White', command = lambda:self.newmethodbtn(master), 
                                              width=280, height = 30, corner_radius= 5).place(x=10, y=240)

        ## main screen
        global main_bg,main_fg,main_text,widget_color
        main_bg = '#1e1e1e'
        main_fg = '#151515'
        main_text = 'White'
        widget_color='#376489'

        mainscreen = customtkinter.CTkLabel(self, text=None, fg_color=main_bg, height=1100, width=1620, corner_radius = 10)
        mainscreen.place(x=300, y=-10)

        History_slot = customtkinter.CTkLabel(self, text=None, fg_color=main_fg, bg_color=main_bg, width = 1600, height = 500, corner_radius= 10).place(x=310, y=10)
        #History_Frame = customtkinter.CTkLabel(self, text=None, fg_color=widget_color, bg_color=main_fg, width=1560, height= 460, corner_radius=10).place(x=330, y=30)
        History_Date_Label = customtkinter.CTkLabel(self, text="Date", fg_color='#223e55', bg_color=main_fg,width=400, height=30, corner_radius=0,font=('Segoe UI', 20), text_color=main_text).place(x=330,y=30)
        History_X_Label = customtkinter.CTkLabel(self, text="Label X", fg_color='#223e55', bg_color=main_fg,width=386, height=30, corner_radius=0,font=('Segoe UI', 20), text_color=main_text).place(x=731,y=30)
        History_Y_Label = customtkinter.CTkLabel(self, text="Label Y", fg_color='#223e55', bg_color=main_fg,width=386, height=30, corner_radius=0,font=('Segoe UI', 20), text_color=main_text).place(x=1118,y=30)
        History_Z_Label = customtkinter.CTkLabel(self, text="Label Z", fg_color='#223e55', bg_color=main_fg,width=386, height=30, corner_radius=0,font=('Segoe UI', 20), text_color=main_text).place(x=1505,y=30)
        History_set=History_set.sort_values(by="Date", ascending=False)
        count=0

        for y_pos in range(100,500,50):     #alternative method is to use TreeView, which seemed very clunky and confusing + had the same #, if not more, lines of code
            if np.isnat(np.datetime64(str(History_set.iloc[count,0]))) == False:
                History_Date=customtkinter.CTkLabel(self,  text=History_set.iloc[count,0], width = 400, height=30, bg_color=main_fg, fg_color=main_fg, text_color=main_text, font=('Segoe UI', 20)).place(x=330, y=y_pos)
                History_X=customtkinter.CTkLabel(self, text=History_set.iloc[count,1], width = 400, height=30, bg_color=main_fg, fg_color=main_fg, text_color=main_text, font=('Segoe UI', 20)).place(x=731, y=y_pos)
                History_Y=customtkinter.CTkLabel(self, text=History_set.iloc[count,2], width = 400, height=30, bg_color=main_fg, fg_color=main_fg, text_color=main_text, font=('Segoe UI', 20)).place(x=1118, y=y_pos)
                History_Z=customtkinter.CTkLabel(self, text=History_set.iloc[count,3], width = 400, height=30, bg_color=main_fg, fg_color=main_fg, text_color=main_text, font=('Segoe UI', 20)).place(x=1505, y=y_pos)
            count+=1
        


        TS_RPM_options = ['400','600','750','900','1000','1150','1250','1350','1500']
        TS_RPM_slot = customtkinter.CTkLabel(self, text=None, fg_color=main_fg, bg_color=main_bg, width = 500, height = 100, corner_radius= 5).place(x=310, y=520)
        TS_RPM_Label = customtkinter.CTkLabel(self, text = "Select Thermal Shaker RPM: ", fg_color=main_fg, bg_color=main_fg, text_color=main_text
                                              ,font=('Segoe UI', 20)).place(x=330, y=555)
        
        TS_RPM_Menu = customtkinter.CTkOptionMenu(self, fg_color=widget_color, bg_color=main_fg, values=TS_RPM_options, width=190, height=30,dropdown_font=('Segoe UI', 15)
                                                  ,font=('Segoe UI', 15)).place(x=585,y=555)

        temp1_slot = customtkinter.CTkLabel(self, text=None, fg_color=main_fg, bg_color=main_bg, width = 500, height = 430, corner_radius= 5).place(x=310, y=630)

        temp2_slot = customtkinter.CTkLabel(self, text=None, fg_color=main_fg, bg_color=main_bg, width = 500, height = 540, corner_radius= 5).place(x=820, y=520)

        temp3_slot = customtkinter.CTkLabel(self, text=None, fg_color=main_fg, bg_color=main_bg, width = 580, height = 265, corner_radius= 5).place(x=1330, y=520)

        temp4_slot = customtkinter.CTkLabel(self, text=None, fg_color=main_fg, bg_color=main_bg, width = 580, height = 265, corner_radius= 5).place(x=1330, y=795)

        
        

class NewMethodScreen(customtkinter.CTkFrame):
    def exitbutton(self,master):
        master.destroy()
    def sv_login(self,master):
        master.LoginFrame()
    def newmethodbtn(self,master):
        master.NewMethodFrame()
    def backbutton(self,master):            #self relates to frame, master relates to App(). 
        #self.pack_forget()                  #pack_forget allows for the frame to be packed again, while destroy() requires another initialization of the frame
        master.HomeFrame()                  #after frame is removed, go back to home frame
    def changedate(self,date_btn_status,date_btn):
        global db_count
        if db_count == 0:
            date_btn_status.set("Set Date")
            db_count=1
            
        elif db_count==1:
            date_btn_status.set(str(date.today()))
            db_count=0
            


        

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global History_set
        logo = customtkinter.CTkImage(dark_image= Image.open(r"RITBIO.png"),size=(400,400))   # change logo here - insert path if not in same folder, r" converts to raw string
        logobutton = customtkinter.CTkButton(self,image= logo,bg_color= 'transparent',fg_color="transparent", text= None, hover=False)
        logobutton.place( x=-70, y=-100)
        ## left panel
        exitbtn = customtkinter.CTkButton(master=self, text="Exit", text_color= 'white', command=lambda:self.exitbutton(master), 
                                          width=280, height = 30, hover_color='maroon',bg_color= 'transparent', corner_radius= 5).place(x=10, y=1030)
        
        sv_loginbtn = customtkinter.CTkButton(master=self, text="Supervisor Login", text_color= 'White', command = lambda:self.sv_login(master), 
                                              width=280, height = 30, corner_radius= 5).place(x=10, y=990)
        
        homebtn = customtkinter.CTkButton(master=self, text="Home", text_color= 'White', 
                                              width=280, height = 30, corner_radius= 5, command= lambda: self.backbutton(master)).place(x=10, y=200)

        history_entrybtn = customtkinter.CTkButton(master=self, text="Record New Method", text_color= 'White', 
                                              width=280, height = 30, corner_radius= 5, fg_color='#1e1e1e', hover=False).place(x=10, y=240)
        

        ## main screen
        main_bg = '#1e1e1e'
        main_fg = '#151515'
        main_text = 'White'
        widget_color='#376489'

        mainscreen = customtkinter.CTkLabel(self, text=None, fg_color=main_bg, height=1100, width=1620, corner_radius = 10)
        mainscreen.place(x=300, y=-10)
        
        

        History_slot = customtkinter.CTkLabel(self, text=None, fg_color=main_fg, bg_color=main_bg, width = 1600, height = 860, corner_radius= 10).place(x=310, y=190)
        #History_Frame = customtkinter.CTkLabel(self, text=None, fg_color=widget_color, bg_color=main_fg, width=1560, height= 460, corner_radius=10).place(x=330, y=30)
        History_Date_Label = customtkinter.CTkLabel(self, text="Date", fg_color='#223e55', bg_color=main_fg,width=400, height=30, corner_radius=0,font=('Segoe UI', 20), text_color=main_text).place(x=330,y=210)
        History_X_Label = customtkinter.CTkLabel(self, text="Label X", fg_color='#223e55', bg_color=main_fg,width=386, height=30, corner_radius=0,font=('Segoe UI', 20), text_color=main_text).place(x=731,y=210)
        History_Y_Label = customtkinter.CTkLabel(self, text="Label Y", fg_color='#223e55', bg_color=main_fg,width=386, height=30, corner_radius=0,font=('Segoe UI', 20), text_color=main_text).place(x=1118,y=210)
        History_Z_Label = customtkinter.CTkLabel(self, text="Label Z", fg_color='#223e55', bg_color=main_fg,width=386, height=30, corner_radius=0,font=('Segoe UI', 20), text_color=main_text).place(x=1505,y=210)
        History_set=History_set.sort_values(by="Date", ascending=False)
        count=0

        for y_pos in range(290,990,50):     #alternative method is to use TreeView, which seemed very clunky and confusing + had the same #, if not more, lines of code
            if np.isnat(np.datetime64(str(History_set.iloc[count,0]))) == False:
                History_Date=customtkinter.CTkLabel(self,  text=History_set.iloc[count,0], width = 400, height=30, bg_color=main_fg, fg_color=main_fg, text_color=main_text, font=('Segoe UI', 20)).place(x=330, y=y_pos)
                History_X=customtkinter.CTkLabel(self, text=History_set.iloc[count,1], width = 400, height=30, bg_color=main_fg, fg_color=main_fg, text_color=main_text, font=('Segoe UI', 20)).place(x=731, y=y_pos)
                History_Y=customtkinter.CTkLabel(self, text=History_set.iloc[count,2], width = 400, height=30, bg_color=main_fg, fg_color=main_fg, text_color=main_text, font=('Segoe UI', 20)).place(x=1118, y=y_pos)
                History_Z=customtkinter.CTkLabel(self, text=History_set.iloc[count,3], width = 400, height=30, bg_color=main_fg, fg_color=main_fg, text_color=main_text, font=('Segoe UI', 20)).place(x=1505, y=y_pos)
            count+=1
        db_count=0
        newmethod_label = customtkinter.CTkLabel(self,text="Add a new method:", text_color=main_text,bg_color=main_bg,fg_color=main_bg, font=('Segoe UI', 20), width = 1600, height=50).place(x=310,y=10)
        default_date = date.today()
        calendar_picker = DateEntry(self, selectmode = 'day', day=default_date.day, month = default_date.month, year = default_date.year,width=40,background=widget_color, 
                                    forground='white', bordercolor = main_bg,headersbackground = main_fg, headersforeground = main_text, selectedbackground = widget_color,
                                    selectedforeground = main_text,weekendbackground = main_fg, weekendforeground = main_text, othermonthbackground =main_bg, othermonthforeground = main_text,
                                    othermonthwebackground =main_bg, othermonthweforeground = main_text,
                                    normalbackground = main_fg, normalforeground = main_text).place(x=410, y=100) 
        LabelX_Entry = customtkinter.CTkEntry(self, bg_color=main_fg,fg_color='white',placeholder_text='Label X', text_color='black',width=280, height=10, corner_radius=0).place(x=790, y=100)
        LabelY_Entry = customtkinter.CTkEntry(self, bg_color=main_fg,fg_color='white',placeholder_text='Label Y', text_color='black',width=280, height=10, corner_radius=0).place(x=1177, y=100)
        LabelZ_Entry = customtkinter.CTkEntry(self, bg_color=main_fg,fg_color='white',placeholder_text='Label Z', text_color='black',width=280, height=10, corner_radius=0).place(x=1564, y=100)
        newmethod_btn = customtkinter.CTkButton(self, bg_color=main_fg, corner_radius=5,text='Add',width=1500, height=30, fg_color='#223e55').place(x=360, y=150)
        
        
        


           

class SupervisorScreen(customtkinter.CTkFrame):
    def setreturncode(self,master, returncode,confirmation,conf_text,conf_cancel,conf_OK):
        if returncode == 1:
            confirmation.destroy(),conf_text.destroy(),conf_cancel.destroy(),conf_OK.destroy()
            master.HomeFrame()
            returncode=0
        elif returncode == 2:
            returncode=0
            confirmation.destroy(),conf_text.destroy(),conf_cancel.destroy(),conf_OK.destroy()
        
    def exitbutton(self,master):
        master.destroy()
    def sv_return(self,master):
        confirmation = customtkinter.CTkButton(self, text=None, fg_color='#1e1e1e', height=300, width=600, corner_radius = 10, hover=False)
        confirmation.place(x=660,y=390)
        #conf_title = customtkinter.CTkLabel(self, text="Are you sure?", font= ('Segoe UI', 24), text_color='white', bg_color='#1e1e1e', fg_color='#1e1e1e')
        #conf_title.place(x=880, y=410)
        conf_text = customtkinter.CTkLabel(self, text="Any unsaved changes will be lost. Press OK to be logged out of supervisor mode.", font= ('Segoe UI', 15), text_color='white', bg_color='#1e1e1e', fg_color='#1e1e1e')
        conf_text.place(x=700, y=520)
        conf_OK = customtkinter.CTkButton(self, text = 'OK', bg_color='#1e1e1e', width = 100, height = 20, corner_radius=10, command = lambda: self.setreturncode(master,1,confirmation,conf_text,conf_cancel,conf_OK))
        conf_OK.place(x=1150, y=660)
        conf_cancel = customtkinter.CTkButton(self, text = 'Cancel', bg_color='#1e1e1e', fg_color='white', width = 100, height = 20, corner_radius=10, hover_color='maroon', text_color='black', command = lambda: self.setreturncode(master,2,confirmation,conf_text,conf_cancel,conf_OK))
        conf_cancel.place(x=1040, y=660)
        
        

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        logo = customtkinter.CTkImage(dark_image= Image.open(r"RITBIO.png"),size=(400,400))   # change logo here - insert path if not in same folder, r" converts to raw string
        logobutton = customtkinter.CTkButton(self,image= logo,bg_color= 'transparent',fg_color="transparent", text= None, hover=False)
        logobutton.place( x=-70, y=-100)

        sv_notice = customtkinter.CTkButton(master=self, text="Supervisor Mode", text_color='White', font= ('Segoe UI', 15), fg_color='maroon', width=1920, height=10, corner_radius=0)
        

        ## left panel
        exitbtn = customtkinter.CTkButton(master=self, text="Exit", text_color= 'white', command=lambda:self.exitbutton(master), fg_color='black', width=280, height = 40, hover_color='maroon',bg_color= 'transparent', corner_radius= 10)
        exitbtn.place(x=10, y=1030)

        sv_returnbtn = customtkinter.CTkButton(master=self, text="Return to user mode", text_color= 'White', command = lambda:self.sv_return(master), width=280, height = 40, corner_radius= 10)
        sv_returnbtn.place(x=10, y=970)

        ## main screen
        mainscreen = customtkinter.CTkLabel(self, text=None, fg_color='#c1c1c1', height=1060, width=1610, corner_radius = 10)
        mainscreen.place(x=300, y=10)
        sv_notice.place(x=0,y=0)
        sv_notice.lift()



class App(customtkinter.CTk):       
    def LoginFrame(self):                # we could name the arguments 'master' instead of 'self', but self typically relates to current class
        self.newmethod_frame.pack_forget()
        self.home_frame.pack_forget()
        self.login_frame.pack()
    def HomeFrame(self):
        self.newmethod_frame.pack_forget()
        self.login_frame.pack_forget()
        self.sv_frame.pack_forget()
        self.home_frame.pack()
    def SVFrame(self):
        self.login_frame.pack_forget()
        self.sv_frame.pack()
    def NewMethodFrame(self):
        self.home_frame.pack_forget()
        self.newmethod_frame.pack()


    def exitbutton(self):
        self.destroy()
    
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("light")                   #could be changed to match system appearance and other widgets could be modified based on appearance mode
        customtkinter.set_default_color_theme("dark-blue")
        self.geometry("1920x1080")                                  
        self.login_frame = LoginScreen(master=self, width = 1920, height = 1080) # initializing Login Screen frame
        self.home_frame = HomeScreen(master=self, width = 1920, height = 1080)  # initializing Home Screen frame
        self.sv_frame = SupervisorScreen(master=self, width = 1920, height = 1080)  # initializing Supervisor Screen frame
        self.newmethod_frame = NewMethodScreen(master=self, width = 1920, height = 1080)  # initializing Supervisor Screen frame
        self.home_frame.pack(side="top", expand=True, fill="both")              # packing Homescreen frame by default

        


homescreen1 = App()
homescreen1.attributes("-fullscreen", True)         #always full screen
homescreen1.bind('<F11>', lambda event: homescreen1.attributes("-fullscreen", False))
homescreen1.bind('<F12>', lambda event: homescreen1.attributes("-fullscreen", True))
homescreen1.mainloop()