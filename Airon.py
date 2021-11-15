from tkinter import *
from math import sqrt

root = Tk()
#root.geometry("250x300")
root.title("Main phase")

def cls_command():
    a.delete(0, END)
    b.delete(0, END)
    c.delete(0, END)

def submit():
    top = Toplevel(root)
    #top.geometry("250x300")
    top.title("Resultados")
    na = int(a.get())
    nb = int(b.get())
    nc = int(c.get())

    p = "{}x² +{}x +{} = 0".format(na, nb, nc)

    delta = ((nb**2)-4*na*nc)
    raiz = round(sqrt(delta), 2)
    x1 = (((-nb)+raiz)/(2*na))
    x2 = (((-(nb))-raiz)/(2*na))
    xv = ((-nb)/2*na)
    yv = ((-(delta))/4*na)

    if nb < 0 and nc < 0:
        p = "{}x² {}x {} = 0".format(na, nb, nc)
    elif nb < 0:
        p = "{}x² {}x +{} = 0".format(na, nb, nc)
    elif nc < 0:
        p = "{}x² +{}x {} = 0".format(na, nb, nc)

    frame_all = LabelFrame(top, text=p)
    frame_all.grid(row=0, column=0)

    frame_dlt = LabelFrame(frame_all, text="Delta")
    frame_dlt.grid(row=0, column=0)
    delta_text = Label(frame_dlt, text=delta)
    delta_text.grid(row=0, column=1)
    
    frame_rz = LabelFrame(frame_all, text="Raiz Quadrada")
    frame_rz.grid(row=0, column=1)
    raiz_text = Label(frame_rz, text= raiz)
    raiz_text.grid(row=0, column=0)
    
    frame_x1 = LabelFrame(frame_all, text="X1")
    frame_x1.grid(row=0, column=3)
    x1_txt = Label(frame_x1, text=round(x1, 2))
    x1_txt.grid()
    
    frame_x2 = LabelFrame(frame_all, text="X2")
    frame_x2.grid(row=0, column=4)
    x2_txt = Label(frame_x2, text=round(x2, 2))
    x2_txt.grid()

    vertice = LabelFrame(frame_all, text="Vertices")
    vertice.grid(row=1, column=0)
    xv_l = Label(vertice, text="Xv: ")
    xv_l.grid(row=0, column=0)
    xv_label = Label(vertice, text=xv)
    xv_label.grid(row=0, column=1)
    yv_l = Label(vertice, text="Yv: ")
    yv_l.grid(row=1, column=0)
    yv_label = Label(vertice, text=yv)
    yv_label.grid(row=1, column=1)

    conc = LabelFrame(frame_all, text="Concavidade")
    conc.grid(row=1, column=1)
    if na < 0:
        var = Label(conc, text="Para Cima")
    else:
        var = Label(conc, text="Para Baixo")
    var.grid()

    
    close = Button(top, text="Close", command=top.destroy)
    close.grid(row=1, column=0)

    top.mainloop()
    
frame1 = LabelFrame(root, text="Ax²", padx=10, pady=10)
frame1.grid(row=0, column=0)
a = Entry(frame1,width=10)
a.grid()

frame2 = LabelFrame(root, text="Bx",padx=10, pady=10)
frame2.grid(row=0, column=1)
b = Entry(frame2,width=10)
b.grid()

frame3 = LabelFrame(root, text="C", padx=10, pady=10)
frame3.grid(row=0, column=2)
c = Entry(frame3,width=10)
c.grid()

submit_btn = Button(root,text="Submit",command= submit)
submit_btn.grid(row=1, column=0, columnspan=2)

clean = Button(root, text="Clean", command=cls_command)
clean.grid(row=1, column=1, columnspan=2)

root.mainloop()