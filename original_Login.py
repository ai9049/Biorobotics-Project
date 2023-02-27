import customtkinter
import tkinter
import time
from PIL import Image







        
        
class LoginApp(customtkinter.CTk):
    def exitbutton(app):
        time.sleep(0.5)
        app.after(1500, app.destroy)
    
    def logincheck(app,username_entry, password_entry):
        
        if username_entry == 'ahmadibraa' and password_entry == '54321':
            entry_label = customtkinter.CTkLabel(app, text = 'Please wait a moment while you are logged in...', text_color='#44c9a4', font=('Segoe UI', 15))
            entry_label.place(x=796, y= 415)
            time.sleep(2)
            
        else:
            entry_label = customtkinter.CTkLabel(app, text = 'Invalid username and/or password, please try again', text_color='maroon', font=('Segoe UI', 15))
            entry_label.place(x=796, y= 415)
            entry_label.after(3000, lambda: entry_label.destroy())    
    
    def __init__(app):
        super().__init__()
        DARK_MODE = "dark"
        customtkinter.set_appearance_mode(DARK_MODE)
        customtkinter.set_default_color_theme("dark-blue")
        app.title('Welcome')
        app.geometry("1920x1080")
        logo = customtkinter.CTkImage(dark_image= Image.open(r"C:\Users\ahmad\OneDrive\Documents\python\RITBIO_DARK.png"),size=(700,700))
        logobutton = customtkinter.CTkButton(app,image= logo, bg_color= 'transparent', text= None, fg_color="transparent", hover=False)
        logobutton.place( x=600, y=-50)

        notice_label = customtkinter.CTkLabel(app, text='-S U P E R V I S O R   L O G I N-')
        notice_label.configure(font=('Segoe UI', 15))
        notice_label.place(x=860, y= 950)

        username_label=customtkinter.CTkLabel(app, text='Username', bg_color= 'transparent')
        username_label.configure(font=('Segoe UI', 26))
        username_label.place(x=761, y=450)

        password_label=customtkinter.CTkLabel(app, text='Password',bg_color= 'transparent')
        password_label.configure(font=('Segoe UI', 26))
        password_label.place(x=761, y=500)
        username_entry = customtkinter.CTkEntry(master=app, fg_color='#252526', font= ('Segoe UI', 15), text_color='#a3adb7', corner_radius=3,width=250,height=40,bg_color= 'transparent')
        username_entry.place(x=908, y=450)
        username_entry.bind('<Return>', lambda event:app.logincheck(username_entry.get(), password_entry.get()))

        password_entry = customtkinter.CTkEntry(master=app, fg_color='#252526', font= ('Segoe UI', 15), text_color='#a3adb7', corner_radius=3,width=250,height=40,show="•",bg_color= 'transparent')
        password_entry.place(x=908, y=500)
        password_entry.bind('<Return>', lambda event:app.logincheck(username_entry.get(), password_entry.get()))

        exitbtn = customtkinter.CTkButton(master=app, text="Back", text_color= 'black', command=app.exitbutton, fg_color='white', width=120, hover_color='maroon',bg_color= 'transparent')
        exitbtn.place(x=761, y=550)

        loginbt = customtkinter.CTkButton(master=app, text="Login", width=250, command=lambda: app.logincheck(username_entry.get(), password_entry.get()),bg_color= 'transparent')
        loginbt.place(x=908,y=550 )



    

    
    



loginscreen = LoginApp()
loginscreen.attributes("-fullscreen", True)
loginscreen.mainloop()

