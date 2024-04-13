from Heema import *

from tkextrafont import Font

state = "on"

toggle_on_symbol = u"\ued0a"  # Symbol for the "on" state
toggle_off_symbol = u"\ued09"  # Symbol for the "off" state

settings_page = create_window()
heema_icons = Font(file="heema-icons.ttf", family="heema-icons")


def turn_on_or_off():
    global state  # Access and update the global variable 'state'
    toggle_text = toggle_off_symbol if state == "on" else toggle_on_symbol

    if (state == "on"):
        state = "off"
        switch_button1.config(text=toggle_text, fg="#787878")
        switch_button1.update()
    else:
        state = "on"
        switch_button1.config(text=toggle_text, fg="#ffffff")
        switch_button1.update()


def toggle_switch_button(frame_name, text, command=do_nothing):
    l = Button(frame_name, font=('calibri', "11"), text=text, border=label_bd, bg=label_bg, fg="white", command=command)
    l.config(activebackground="#202020", activeforeground="white", bg="#202020", fg="#ffffff", )  # 018574

    return l


switch_button1 = toggle_switch_button(
    frame_name=settings_page, text=toggle_on_symbol if state == "on" else "off", command=turn_on_or_off
)

switch_button1.config(font=("SegoeUI", 50))
switch_button1.pack()


make_rounded(settings_page)
settings_page.mainloop()