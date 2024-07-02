from tkinter import *
import ctypes as ct

def dark_title_bar(window):
    """
    MORE INFO:
    https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value), 4)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

splash_screen = Tk()
splash_screen.title('Register Patients')

splash_screen.configure(bg='#10c4e0')
splash_screen.resizable(False, False)
dark_title_bar(splash_screen)

app_width = 300
app_height = 200
center_window(splash_screen, app_width, app_height)

welcome_label = Label(splash_screen, text='Welcome to HealthCheckBR!', font=('Helvetica', 16), 
                      bg='darkgreen', fg='white', width=28)
welcome_label.pack()

welcome_text = Label(splash_screen,text='This app is made to check the \nhealth of a person for quarantine \nexamination. You can add patients one by one.', 
                     height=5, width=35, font=('Arial', 15), bg='white', wraplength=290)
welcome_text.pack()

def main_window():
    splash_screen.destroy()
    root = Tk()
    root.configure(bg='#242424')
    root.title('HealthCheckBR')
    dark_title_bar(root)
    
    main_width = 720
    main_height = 480
    center_window(root, main_width, main_height)

    # You can add more widgets to the main window here
    title_label = Label(root, text='All Patients', font=('Arial', 20, 'bold'), bg='#242424', fg='white')
    title_label.pack()

    add_patient = Button(root, text='+ Add patient', font=('Arial', 28,'bold'), width=25, bg='#181818', fg='white', 
                         activebackground='#555', activeforeground='white', border=0)
    add_patient.pack(pady=5)

    remove_patient = Button(root, text='- Remove patient', font=('Arial', 28, 'bold'), width=25, bg='#181818', fg='white',
                            activebackground='#555', activeforeground='white', border=0)
    remove_patient.pack(pady=5)

    root.mainloop()

accept_button = Button(splash_screen, text='Understood!', bg='green', fg='white',
                       font=('Helvetica', 18), activebackground='darkgreen', activeforeground='white', border=0,
                       command=main_window)
accept_button.pack(pady=5)

splash_screen.mainloop()
