from tkinter import *
from helper import *

def custom():
    print("TBD")

if __name__ == "__main__": 
    root = Tk()
    root.configure(background='light blue') 
    root.title("Twitter Mod App")  
    root.geometry("450x250")
    root.resizable(0, 0)
    
    #created menu for outpust screen
    menubar = Menu(root)
    output = Menu(menubar, tearoff = 0)
    output.add_command(label="Output Screen", command=custom)
    menubar.add_cascade(label="Output",menu = output)
    
    #frame for content
    content = Frame(root, bg='cyan')
    content.grid(row=0, column=0)

    #created frame for my profile
    frame1 = Frame(content, bg='yellow').grid(row=0,column=2)
    profile_label = Label(frame1,text="My Profile:")
    profile_label.grid(row=0,column=0)
    text = Text(frame1, height=5, width=50)
    text.insert(INSERT, "Hi, ")
    text.insert(END, "\nBye Bye.....")
    text.grid(row=1,columnspan=3)

    #created frame for buttons
    frame2 = Frame(content, bg = 'red').grid(row=1,columnspan=2)

    follow_list = Button(frame2, text="Get followers List")

    following_list = Button(frame2, text="Get followings List")
 
    follow_random = Button(frame2, text="Follow people randomly")

    unfollow = Button(frame2, text="Unfollow who didn't followed back")

    follow_excel = Button(frame2, text="export excel for followers")

    following_excel = Button(frame2, text="export excel for followings")

    follow_list.grid(row=8,column=0, pady=5, padx=5)
    following_list.grid(row=8,column=1, pady=5, padx=5)
    follow_random.grid(row=10,column=0, pady=5, padx=5)
    unfollow.grid(row=10,column=1, pady=5, padx=5)
    follow_excel.grid(row=11,column=0, pady=5, padx=5)
    following_excel.grid(row=11,column=1, pady=5, padx=5)


    root.config(menu = menubar)
    # start the GUI 
    root.mainloop() 