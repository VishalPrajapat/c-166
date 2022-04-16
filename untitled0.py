from tkinter import *
from PIL import ImageTk,Image 

root=Tk()
root.title("Working on Canvas With Function")
root.geometry("600x600")

color_lable=Label(root,text="Enter A Color :")
color_lable.place(relx=0.6,rely=0.9,anchor=CENTER)

input_box=Entry(root)
input_box.insert(0,"black")
input_box.place(relx=0.8,rely=0.9,anchor=CENTER)

canvas=Canvas(root,width=590,height=510,bg="blue",highlightbackground="black")
canvas.pack()

img=ImageTk.PhotoImage(Image.open("start_point1.png"))
my_image=canvas.create_image(50,50,image=img)
direction=""
odlx=50
oldy=50
newx=50
newy=50
def right_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx+5
    direction="Right"
    draw(direction,oldx,oldy,newx,newy)
def left_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx-5
    draw(direction,oldx,oldy,newx,newy)

def up_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    odly=newy
    newy=newy-5
    draw(direction,oldx,oldy,newx,newy)
    
def down_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    odly=newy
    newy=newy+5
    draw(direction,oldx,oldy,newx,newy)    
    
def draw(direction,oldx,oldy,newx,newy):
    fill_color=input_box.get()
    if(direction=="Right"):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)        
    if(direction=="Left"):
        left_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)            
    if(direction=="Up"):
        up_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)            
    if(direction=="Down"):
        down_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)            
canvas.pack()        
root.bind("<Right>",right_dir)    
root.bind("<Left>",left_dir)   
root.bind("<Up>",up_dir)    
root.bind("<Down>",down_dir)     

root.mainloop()