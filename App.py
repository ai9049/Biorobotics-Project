import customtkinter
from tkinter import *
import time
from PIL import Image

##                                  ---Creating functionality first, minor graphic modifications included---
## 27/2/2023 - Supervisor Screen frame designed + return button with confirmation 
## 25/2/2023 - Home screen frame designed with supervisor login and exit buttons, white patch on right side of screen to display information
##           - Login Screen integrated with supervisor login button, detects valid username password, can go back to home screen 

class LoginScreen(customtkinter.CTkFrame):   #Each Screen is a different CTK Frame
    def backbutton(self,master):            #self relates to frame, master relates to App(). 
        self.pack_forget()                  #pack_forget allows for the frame to be packed again, while destroy() requires another initialization of the frame
        master.HomeFrame()                  #after frame is removed, go back to home frame
        
    
    def logincheck(self,master,username_entry, password_entry):
        
        if username_entry.get() == 'ahmad' and password_entry.get() == '54321':    # enter password here, or replace with variable linked to an excel doc, etc.
            username_entry.delete(0,END),password_entry.delete(0,END) # deletes text so it wont show on another login attempt                                                                                         #|
            ## Here is where the supervisor frame call would be, and pack_forget login frame
            self.pack_forget()
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

        username_label=customtkinter.CTkLabel(self, text='Username',bg_color= '#252526',fg_color="#252526", text_color='white')
        username_label.configure(font=('Segoe UI', 26))
        username_label.place(x=761, y=450)

        password_label=customtkinter.CTkLabel(self, text='Password',bg_color= '#252526',fg_color="#252526", text_color='white')
        password_label.configure(font=('Segoe UI', 26))
        password_label.place(x=761, y=500)
        username_entry = customtkinter.CTkEntry(master=self, fg_color='#252526', font= ('Segoe UI', 15), text_color='#a3adb7', corner_radius=3,width=250,height=40,bg_color= '#252526')
        username_entry.place(x=908, y=450)
        username_entry.bind('<Return>', lambda event:self.logincheck(master,username_entry, password_entry)) #binds return key to login press, as per login standards

        password_entry = customtkinter.CTkEntry(master=self, fg_color='#252526', font= ('Segoe UI', 15), text_color='#a3adb7', corner_radius=3,width=250,height=40,show="•",bg_color= '#252526')
        password_entry.place(x=908, y=500)
        password_entry.bind('<Return>', lambda event:self.logincheck(master,username_entry, password_entry)) #same as above

        backarrows = customtkinter.CTkImage(dark_image= Image.open(r"backbtn.png"),size=(100,100))   # change logo here - insert path if not in same folder, r" converts to raw string
        backbtn = customtkinter.CTkButton(master=self, command =lambda:self.backbutton(master), width=120, hover_color='maroon',bg_color= '#252526', fg_color='#252526', image= backarrows, text=None)
        backbtn.place(x=10, y=10)

        loginbt = customtkinter.CTkButton(master=self, text="Login", width=400, command=lambda: self.logincheck(master,username_entry, password_entry),bg_color= '#252526')
        loginbt.place(x=760,y=550 )

class HomeScreen(customtkinter.CTkFrame):
    def exitbutton(self,master):
        master.destroy()
    def sv_login(self,master):
        master.LoginFrame()
        self.after(500,self.pack_forget())

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        logo = customtkinter.CTkImage(dark_image= Image.open(r"RITBIO.png"),size=(400,400))   # change logo here - insert path if not in same folder, r" converts to raw string
        logobutton = customtkinter.CTkButton(self,image= logo,bg_color= 'transparent',fg_color="transparent", text= None, hover=False)
        logobutton.place( x=-70, y=-100)

        ## left panel
        exitbtn = customtkinter.CTkButton(master=self, text="Exit", text_color= 'white', command=lambda:self.exitbutton(master), fg_color='black', width=280, height = 40, hover_color='maroon',bg_color= 'transparent', corner_radius= 10)
        exitbtn.place(x=10, y=1030)

        sv_loginbtn = customtkinter.CTkButton(master=self, text="Supervisor Login", text_color= 'White', command = lambda:self.sv_login(master), width=280, height = 40, corner_radius= 10)
        sv_loginbtn.place(x=10, y=970)

        ## main screen
        mainscreen = customtkinter.CTkLabel(self, text=None, fg_color='#c1c1c1', height=1060, width=1610, corner_radius = 10)
        mainscreen.place(x=300, y=10)

class SupervisorScreen(customtkinter.CTkFrame):
    def setreturncode(self,master, returncode,confirmation,conf_text,conf_cancel,conf_OK):
        if returncode == 1:
            confirmation.destroy(),conf_text.destroy(),conf_cancel.destroy(),conf_OK.destroy()
            self.pack_forget()
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
        self.login_frame.pack()
    def HomeFrame(self):
        self.home_frame.pack()
    def SVFrame(self):
        self.sv_frame.pack()


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
        self.home_frame.pack(side="top", expand=True, fill="both")              # packing Homescreen frame by default
        


homescreen1 = App()
homescreen1.attributes("-fullscreen", True)         #always full screen
homescreen1.bind('<F11>', lambda event: homescreen1.attributes("-fullscreen", False))
homescreen1.bind('<F12>', lambda event: homescreen1.attributes("-fullscreen", True))
homescreen1.mainloop()