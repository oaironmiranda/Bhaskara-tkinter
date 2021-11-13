from tkinter import *
from math import sqrt

root = Tk()
root.geometry("250x300")
root.title("Main phase")

def cls_command():
    a.delete(0, END)
    b.delete(0, END)
    c.delete(0, END)

def submit():
    top = Toplevel(root)
    top.geometry("250x300")
    top.title("Resultados")
    na = int(a.get())
    nb = int(b.get())
    nc = int(c.get())

    p = "{}x² +{}x +{} = 0".format(na, nb, nc)

    delta = ((nb**2)-4*na*nc)
    raiz = round(sqrt(delta), 2)
    x1 = (((-nb)+raiz)/(2*na))
    x2 = (((-nb)-raiz)/(2*na))

    if nb < 0 and nc < 0:
        p = "{}x² {}x {} = 0".format(na, nb, nc)
    elif nb < 0:
        p = "{}x² {}x +{} = 0".format(na, nb, nc)
    elif nc < 0:
        p = "{}x² +{}x {} = 0".format(na, nb, nc)

    frame_all = LabelFrame(top, text=p)
    frame_all.pack()

    frame_dlt = LabelFrame(frame_all, text="Delta")
    frame_dlt.pack()
    delta_text = Label(frame_dlt, text=delta)
    delta_text.pack()

    frame_rz = LabelFrame(frame_all, text="Raiz Quadrada")
    frame_rz.pack()
    raiz_text = Label(frame_rz, text= raiz)
    raiz_text.pack()

    frame_x1 = LabelFrame(frame_all, text="X1")
    frame_x1.pack()
    x1_txt = Label(frame_x1, text=round(x1, 2))
    x1_txt.pack()

    frame_x2 = LabelFrame(frame_all, text="X2")
    frame_x2.pack()
    x2_txt = Label(frame_x2, text=round(x2, 2))
    x2_txt.pack()

    close = Button(top, text="Close", command=top.destroy)
    close.pack()

    top.mainloop()
    
frame1 = LabelFrame(root, text="Ax²", padx=10, pady=10)
frame1.pack(padx=10, pady=10)
a = Entry(frame1,width=10)
a.grid()

frame2 = LabelFrame(root, text="Bx",padx=10, pady=10)
frame2.pack(padx=10, pady=10)
b = Entry(frame2,width=10)
b.grid()

frame3 = LabelFrame(root, text="C", padx=10, pady=10)
frame3.pack(padx=10, pady=10)
c = Entry(frame3,width=10)
c.grid()

submit_btn = Button(root,text="Submit",command= submit)
submit_btn.pack()

clean = Button(root, text="Clean", command=cls_command)
clean.pack()

root.mainloop()
