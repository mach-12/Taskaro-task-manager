from distutils.command.config import config
from pathlib import Path
from tkinter import *
from tkinter import colorchooser

from task import Subjectlist_file, Task

# To store input of subject
subject_list = []
subject_dict = {'subject':'', 'color':''}



# Pointing Path to assests
ASSETS_PATH = Path("./assets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Functions to take color input
def color_box(button):
    color = choose_color()
    subject_dict['color'] = color_code
    button.config(bg=color_code[1])

def choose_color():
    global color_code
    color_code = colorchooser.askcolor(title ="Choose color")    

# Functions of different pages
def showTomorrow():
    pass
def showToday():
    pass
def showWeek():
    pass
def showSubjects():
    pass
def ManageWeekly():
    pass

# Add Task Page
def AddTaskPage():
    window = Tk()

    window.geometry("1920x1080")
    window.attributes('-fullscreen',True)
    window.configure(bg = "#FFFFFF")
        
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 1080,
        width = 1920,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    
    Tommorow_panel_img = PhotoImage(
        file = relative_to_assets("Tomorrow.png"))
    Tommorow_panel = Button(
        image = Tommorow_panel_img,
        borderwidth=0,
        highlightthickness=0,
        command = lambda: showTomorrow(),
        relief = "flat"
    )
    Tommorow_panel.place(
        x=674.0000000000001,
        y=0.0,
        width=571.0,
        height=102.0
    )

    Today_panel_img = PhotoImage(
        file=relative_to_assets("Today.png"))
    Today_panel = Button(
        image=Today_panel_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showToday(),
        relief="flat"
    )
    Today_panel.place(
        x=102.00000000000011,
        y=0.0,
        width=571.0,
        height=102.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("ManageWeekly.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("ManageWeekly clik"),
        relief="flat"
    )

    button_4.place(
        x=960.0,
        y=1016.0,
        width=650.0,
        height=64.0
    )

    ThisWeekPanel_img = PhotoImage(
        file=relative_to_assets("ThisWeek.png"))
    ThisWeekPanel = Button(
        image=ThisWeekPanel_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showWeek(),
        relief="flat"
    )
    ThisWeekPanel.place(
        x=1245.0,
        y=0.0,
        width=571.0,
        height=102.0
    )

    Tommorow_panel_img = PhotoImage(
        file = relative_to_assets("Tomorrow.png"))
    Tommorow_panel = Button(
        image = Tommorow_panel_img,
        borderwidth=0,
        highlightthickness=0,
        command = lambda: showTomorrow(),
        relief = "flat"
    )
    Tommorow_panel.place(
        x=674.0000000000001,
        y=0.0,
        width=571.0,
        height=102.0
    )


    button_image_6 = PhotoImage(
        file=relative_to_assets("exit-button.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: exit(),
        relief="flat"
    )
    button_6.place(
        x=1816.0,
        y=0.0,
        width=104.0,
        height=102.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("ManageSubjects.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("ManageSubjects clicked"),
        relief="flat"
    )
    button_3.place(
        x=310.0,
        y=1016.0,
        width=650.0,
        height=64.0
)


    canvas.create_text(
        800.0,
        121.0,
        anchor="nw",
        text="Add Task",
        fill="#3C3C3C",
        font=("RobotoRoman Regular", 83 * -1)
    )

    entry_1 = Entry(
        font=("RobotoRoman Light", 60 * -1),
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0
    )
    entry_1.place(
        x=543.0,
        y=304.0,
        width=958.0,
        height=99.0
    )


    canvas.create_text(
        283.0,
        304.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("RobotoRoman Light", 72 * -1)
    )


    global is_on

    is_on = True

    checked_graphic = PhotoImage(relative_to_assets("box_empty.png"))
    unchecked_graphic = PhotoImage(relative_to_assets("box_marked.png"))
    # Define our switch function

    box_empty_image = PhotoImage(
        file=relative_to_assets("box_empty.png"))

    box_marked_image = PhotoImage(
        file=relative_to_assets("box_marked.png"))

    button_7 = Button(
        image= box_empty_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: switch(),
        relief="flat"
    )

    def switch():
        global is_on
        if is_on:
            button_7.config(image = box_marked_image)
            is_on = False
        else:
            button_7.config(image = box_empty_image)
            is_on = True

    button_7.place(
        x=548.0,
        y=591.0,
        width=72.0,
        height=72.0
    )


    canvas.create_text(
        182.0,
        576.0,
        anchor="nw",
        text="Repeats?",
        fill="#000000",
        font=("RobotoRoman Light", 72 * -1)
    )

    canvas.create_text(
        238.0,
        712.0,
        anchor="nw",
        text="Subject",
        fill="#000000",
        font=("RobotoRoman Light", 72 * -1)
    )

    canvas.create_text(
        283.0,
        440.0,
        anchor="nw",
        text="Day",
        fill="#000000",
        font=("RobotoRoman Light", 72 * -1)
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("Mon.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=543.0,
        y=440.0,
        width=155.0,
        height=101.0
    )


    #dropdown_list = [i.get('subject') for i in subject_list]
    dropdown_list = ['a', 'b', 'c']
    print(dropdown_list)
    color_list = ['red', 'green', 'blue', 'yellow', 'grey']
    selection = StringVar(canvas)
    selection.set("choose")
    drop = OptionMenu(canvas, selection, *dropdown_list)
    drop.place(   
        x=550.3677368164062,
        y=712.0,
        width= 640,
        height=100
        )
    
    drop.config(font=("RobotoRoman Light", 60 * -1))
    menu = canvas.nametowidget(drop.menuname)
    menu.config(font=("RobotoRoman Light", 20 * -1))

    button_image_9 = PhotoImage(
        file=relative_to_assets("Tue.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    button_9.place(
        x=704.0,
        y=440.0,
        width=154.0,
        height=101.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("Wed.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_10 clicked"),
        relief="flat"
    )
    button_10.place(
        x=866.0,
        y=440.0,
        width=153.0,
        height=101.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("Thu.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_11 clicked"),
        relief="flat"
    )
    button_11.place(
        x=1027.0,
        y=440.0,
        width=153.0,
        height=101.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("Fri.png"))
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_12 clicked"),
        relief="flat"
    )
    button_12.place(
        x=1186.0,
        y=440.0,
        width=154.0,
        height=101.0
    )

    button_image_13 = PhotoImage(
        file=relative_to_assets("Sat.png"))
    button_13 = Button(
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Sat clicked"),
        relief="flat"
    )
    button_13.place(
        x=1348.0,
        y=440.0,
        width=153.0,
        height=101.0
    )

    button_image_14 = PhotoImage(
        file=relative_to_assets("Sun.png"))
    button_14 = Button(
        image=button_image_14,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Sun clicked"),
        relief="flat"
    )
    button_14.place(
        x=1509.0,
        y=440.0,
        width=153.0,
        height=101.0
    )

    button_image_15 = PhotoImage(
        file=relative_to_assets("confirm.png"))
    button_15 = Button(
        image=button_image_15,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_15 clicked"),
        relief="flat"
    )
    button_15.place(
        x=1245.0,
        y=711.0,
        width=417.0,
        height=102.0
    )

    window.resizable(False, False)

    window.mainloop()

# Add Subject page
def AddSubject():
    window = Tk()

    window.geometry("1920x1080")
    window.attributes('-fullscreen',True)
    window.configure(bg = "#FFFFFF")



    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 1080,
        width = 1920,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    Tommorow_panel_img = PhotoImage(
        file = relative_to_assets("Tomorrow.png"))
    Tommorow_panel = Button(
        image = Tommorow_panel_img,
        borderwidth=0,
        highlightthickness=0,
        command = lambda: showTomorrow(),
        relief = "flat"
    )
    Tommorow_panel.place(
        x=674.0000000000001,
        y=0.0,
        width=571.0,
        height=102.0
    )

    Today_panel_img = PhotoImage(
        file=relative_to_assets("Today.png"))
    Today_panel = Button(
        image=Today_panel_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showToday(),
        relief="flat"
    )
    Today_panel.place(
        x=102.00000000000011,
        y=0.0,
        width=571.0,
        height=102.0
    )

    ThisWeekPanel_img = PhotoImage(
        file=relative_to_assets("ThisWeek.png"))
    ThisWeekPanel = Button(
        image=ThisWeekPanel_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showWeek(),
        relief="flat"
    )
    ThisWeekPanel.place(
        x=1245.0,
        y=0.0,
        width=571.0,
        height=102.0
    )


    Confirm_img = PhotoImage(
        file=relative_to_assets("Confirm.png"))
    Confirm_panel = Button(
        image=Confirm_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: subject_entry(),
        relief="flat"
    )
    Confirm_panel.place(
        x=673.0000000000001,
        y=712.0,
        width=571.0,
        height=102.0
    )

    Exit_Button_img = PhotoImage(
        file=relative_to_assets("exit-button.png"))
    Exit_Button = Button(
        image=Exit_Button_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: exit(),
        relief="flat"
    )
    Exit_Button.place(
        x=1816.0,
        y=0.0,
        width=104.0,
        height=102.0
    )



    

    canvas.create_text(
        700,
        125.0,
        anchor="nw",
        text="Add Subject",
        fill="#3C3C3C",
        font=("RobotoRoman Regular", 90 * -1)
    )

    subject_input_img = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        960.0000000000001,
        547.5,
        image=subject_input_img
    )
    subject_input = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        font=("RobotoRoman Regular", 90 * -1)
    )

    subject_input.place(
        x=481.0000000000001,
        y=497.0,
        width=958.0,
        height=99.0
    )

        
    canvas.create_text(
        106.00000000000011,
        497.0,
        anchor="nw",
        text="Name",
        fill="#000000",
        font=("RobotoRoman Light", 72 * -1)
    )


    button_6 = Button(
        borderwidth=0,
        highlightthickness=0,
        command=lambda: color_box(button_6),
        relief="flat"
    )

    button_6.place(
        x=1531.0,
        y=497.0,
        width=101.0,
        height=101.0
    )
    

    button_image_7 = PhotoImage(
        file=relative_to_assets("ManageSubjects.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: showSubjects(),
        relief="flat"
    )
    button_7.place(
        x=310.0000000000001,
        y=1016.0,
        width=650.0,
        height=64.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("ManageWeekly.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ManageWeekly(),
        relief="flat"
    )
    button_8.place(
        x=960.0000000000001,
        y=1016.0,
        width=650.0,
        height=64.0
        )

    def subject_entry():
        
        subject_dict['subject'] = subject_input.get()
        subject_input.delete(0, last = len(subject_input.get()))
        subject_list.append(subject_dict)
        print(subject_list[0])
        
       
    window.resizable(False, False)
    window.mainloop()

AddTaskPage()
#AddSubject()


