from tkinter import *
from PIL import ImageTk , Image

root=Tk()


frame = LabelFrame(root, text="My frame", padx=10, pady=20)  # this will give the inner padding
frame.pack(padx=10, pady=10) # this will give the outer padding , you can use pack as well as grid in this case




root.title("Image Viewer")
# root.geometry("500x400")
# root.iconbitmap()
number =0;


my_img1=ImageTk.PhotoImage(Image.open("images/1.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("images/3.jpg"))
    
image_list = [my_img1,my_img2,my_img3]

my_img= Label(image=my_img1)
my_img.grid(row=0,column=0, columnspan=3)

status = Label(root, text="Image 1 of "+ str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2,column=0, columnspan=3,sticky=W+E)


def exit_program():
    root.quit()


def forward():
    global my_img
    global number
    global button_forward
    button_back = Button(root, text="Back", padx=30, pady=5, command=Backward)
    button_back.grid(row=1,column=2)

    number +=1
    if number==2:
        button_forward = Button(root,text="Next", padx=30, pady=5, command=forward, state= DISABLED)
        button_forward.grid(row=1,column=0)
        

    my_img.grid_forget()
    my_img=Label(image=image_list[number])
    my_img.grid(row=0,column=0, columnspan=3)

    status = Label(root, text="Image "+ str(number+1) +" of "+ str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0, columnspan=3,sticky=W+E)
   
       

def Backward():
    global my_img
    global number
    button_forward = Button(root,text="Next", padx=30, pady=5, command=forward)
    button_forward.grid(row=1,column=0)
    number = number-1
    if number ==0:
        button_back = Button(root, text="Back", padx=30, pady=5, command=Backward, state=DISABLED)
        button_back.grid(row=1,column=2)

    my_img.grid_forget()
    my_img=Label(image=image_list[number])
    my_img.grid(row=0,column=0, columnspan=3)

    status = Label(root, text="Image "+ str(number+1) +" of "+ str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0, columnspan=3,sticky=W+E)



button_forward = Button(root,text="Next", padx=30, pady=5, command=forward)
button_forward.grid(row=1,column=0)


button_exit =Button(root,text="Exit", padx=30, pady=5, command=exit_program)
button_exit.grid(row=1, column=1)


button_back = Button(root, text="Back", padx=30, pady=5, command=Backward)
button_back.grid(row=1,column=2)


root.mainloop()