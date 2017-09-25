
# coding: utf-8

# In[17]:

import numpy as np
import cv2

try:
	import tkinter as tk   ## notice lowercase 't' in tkinter here 
except ImportError:
	import Tkinter as tk

try:
	from tkinter import filedialog as filedialog
except ImportError:
	import tkFileDialog as filedialog 

#variables
path = None;
p = []

def open_image():
    global path, f
    #opens file chooser window and allows user to select a file
    #if path is None:
    #print("Error select image")
    #else:
    path = filedialog.askopenfilename()
    
    #input an image
    f = cv2.imread(path)
    #displays image
    cv2.imshow("image",f)
    #cv2.waitKey(0)

def save_data():
    name = filedialog.asksaveasfile(mode='w',defaultextension=".dat")
    name.write(str(pp))
    name.close()    
    
def close_image():
    #destroys image window
    cv2.destroyWindow("image")

def set_xmin():
    global ux_min
    ux_min = E1.get()

def set_ymin():
    global uy_min
    uy_min = E2.get()    

def set_xmax():
    global ux_max
    ux_max = E3.get()
    
def set_ymax():
    global uy_max
    uy_max = E4.get()
    
def xmin(event, x, y, flags, param):
    global x_min
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(f,(x,y),5, (0,255,0), -1)
        cv2.imshow("image",f)
        x_min = x

def ymin(event, x, y, flags, param):
    global y_min
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(f,(x,y),5, (0,255,0), -1)
        cv2.imshow("image",f)
        y_min = y        
        
def xmax(event, x, y, flags, param):
    global x_max
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(f,(x,y),5, (0,255,0), -1)
        cv2.imshow("image",f)
        x_max = x
        
def ymax(event, x, y, flags, param):
    global y_max
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(f,(x,y),5, (0,255,0), -1)
        cv2.imshow("image",f)
        y_max = y    

def points(event, x, y, flags, param):
    global points, x1, y1
    if event == cv2.EVENT_LBUTTONDOWN:
        if p:
            cv2.line(f,(x1,y1),(x,y),(255,255,0),2)
            cv2.imshow("image",f)
        p.append([x, y])        
        x1 = x
        y1 = y
        
def pick_xmin():
    cv2.setMouseCallback("image", xmin)
    
def pick_ymin():
    cv2.setMouseCallback("image", ymin)
    
def pick_xmax():
    cv2.setMouseCallback("image", xmax)
    
def pick_ymax():
    cv2.setMouseCallback("image", ymax)

def pick_points():
    cv2.setMouseCallback("image", points)
    
def done():
    global pp
    a = (float(ux_max)-float(ux_min))/(x_max-x_min)
    b = (float(uy_max)-float(uy_min))/(y_max-y_min)
    pp = np.asfarray(p)
    pp[:,0] = float(ux_min) + a*(pp[:,0] - float(x_min))
    pp[:,1] = float(uy_min) + b*(pp[:,1] - float(y_min))
    #print(pp)
    
#initialize the window toolkit
root = tk.Tk()

root.title("MyPlotDigitizer")

#root.geometry("512x512")

#creating a button
btn1 = tk.Button(root, text="Select an image", command=open_image)
btn1.grid(row=0,column=0)
btn2 = tk.Button(root, text="Close image", command=close_image)
btn2.grid(row=4,column=0)
btn3 = tk.Button(root, text="Exit", command=root.destroy)
btn3.grid(row=5,column=0)

#creating a frame
frame1 = tk.Frame(root)
frame1.grid(row=2,column=0)

frame2 = tk.Frame(root)
frame2.grid(row=3,column=0)

#creating entries
L1 = tk.Button(frame1, text="x min", command=set_xmin)
L1.grid(row=0,column=0)
E1 = tk.Entry(frame1, bd =5)
E1.grid(row=0,column=1)

L2 = tk.Button(frame1, text="y min", command=set_ymin)
L2.grid(row=1,column=0)
E2 = tk.Entry(frame1, bd =5)
E2.grid(row=1,column=1)

L3 = tk.Button(frame1, text="x max", command=set_xmax)
L3.grid(row=2,column=0)
E3 = tk.Entry(frame1, bd =5)
E3.grid(row=2,column=1)

L4 = tk.Button(frame1, text="y max", command=set_ymax)
L4.grid(row=3,column=0)
E4 = tk.Entry(frame1, bd =5)
E4.grid(row=3,column=1)

L5 = tk.Button(frame2, text="Pick x min", command=pick_xmin)
L5.grid(row=0,column=0)

L6 = tk.Button(frame2, text="Pick y min", command=pick_ymin)
L6.grid(row=1,column=0)

L7 = tk.Button(frame2, text="Pick x max", command=pick_xmax)
L7.grid(row=2,column=0)

L8 = tk.Button(frame2, text="Pick y max", command=pick_ymax)
L8.grid(row=3,column=0)

L9 = tk.Button(frame2, text="Pick data points", command=pick_points)
L9.grid(row=4,column=0)

L10 = tk.Button(frame2, text="Done", command=done)
L10.grid(row=5,column=0)

L11 = tk.Button(frame2, text="Save data", command=save_data)
L11.grid(row=6,column=0)

#creating menu
#menubar = tk.Menu(root)
#filemenu = tk.Menu(menubar, tearoff=0)
#filemenu.add_command(label="Exit", command=root.quit)
#menubar.add_cascade(label="File", menu=filemenu)
#root.config(menu=menubar)

#scale option
#var = tk.DoubleVar()
#scale = tk.Scale( root, variable = var, from_=1, to=4,orient=tk.VERTICAL, label = "Zoom")
#scale.pack(side="bottom")
#scale.grid(row=2,column=1)

# kick off the GUI
root.mainloop()


