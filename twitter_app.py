from tkinter import *
from helper import *

def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()
    

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Twitter Mod App")  
        self.master.geometry("470x250")
        # self.master.resizable(0, 0)
        self.master.configure(background='light blue')
        
        #setting frame
        self.frame = Frame(self.master, bg = 'light blue')
        self.frame.pack()

        #created textbox for profile info
        self.profile_label = Label(self.frame,text="My Profile:")
        self.profile_label.grid(row=0,columnspan=2)
        self.text = Text(self.frame, height=5, width=50)
        self.text.grid(row=1,columnspan=2)

        #created buttons
        self.follow_list = Button(self.frame, text="Get followers List",width = 30, bg = 'green', fg = 'white', )

        self.following_list = Button(self.frame, text="Get followings List", width = 30, bg = 'green', fg = 'white')
    
        self.follow_random = Button(self.frame, text="Follow people randomly", width = 30, bg = 'green', fg = 'white')

        self.unfollow = Button(self.frame, text="Unfollow who didn't followed back",width = 30, bg = 'green', fg = 'white')

        self.follow_excel = Button(self.frame, text="export excel for followers", width = 30, bg = 'green', fg = 'white')

        self.following_excel = Button(self.frame, text="export excel for followings", width = 30, bg = 'green', fg = 'white')

        self.output_btn = Button(self.frame, text="Output",bg='orange', command=self.set_profile)

        self.follow_list.grid(row=8,column=0, pady=5, padx=5)
        self.following_list.grid(row=8,column=1, pady=5, padx=5)
        self.follow_random.grid(row=10,column=0, pady=5, padx=5)
        self.unfollow.grid(row=10,column=1, pady=5, padx=5)
        self.follow_excel.grid(row=11,column=0, pady=5, padx=5)
        self.following_excel.grid(row=11,column=1, pady=5, padx=5)
        self.output_btn.grid(row=12, column=1,pady=5, padx=5)

    def set_profile(self):
        profile_value = view_my_profile("Hadd_hai_bhai")
        self.text.insert(INSERT, profile_value)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = OutputWindow(self.newWindow)
    
if __name__ == '__main__':
    main()