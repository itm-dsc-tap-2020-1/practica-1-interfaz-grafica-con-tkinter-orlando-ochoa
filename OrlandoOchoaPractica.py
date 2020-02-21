import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as mBox

ventana=tk.Tk()
barra_menu=Menu(ventana)

ventana.title("Sistema escolar")
ventana.configure(menu=barra_menu)
tabControl=ttk.Notebook(ventana)
tab1=ttk.Frame(tabControl)
tabControl.add(tab1,text='Datos personales')
tabControl.pack(expand=1,fill="both")

nombre=ttk.Label(tab1,text="Nombre")
nombre.grid(column=1,row=1)
nom=tk.StringVar()
preguntarnom=ttk.Entry(tab1,width=50,textvariable=nom)
preguntarnom.grid(column=2,row=1)

ap=ttk.Label(tab1,text="Apellido P")
ap.grid(column=1,row=2)
app=tk.StringVar()
preguntarap=ttk.Entry(tab1,width=50,textvariable=app)
preguntarap.grid(column=2,row=2)

apm=ttk.Label(tab1,text='Apellido M')
apm.grid(column=1,row=3)
apmm=tk.StringVar()
preguntarapm=ttk.Entry(tab1,width=50,textvariable=apmm)
preguntarapm.grid(column=2,row=3)

dirr=ttk.Label(tab1,text='Direccion')
dirr.grid(column=1,row=4)
dirrr=tk.StringVar()
preguntardirr=ttk.Entry(tab1,width=50,textvariable=dirrr)
preguntardirr.grid(column=2,row=4)

lista1=ttk.Label(tab1,text='Colonia')
lista1.grid(column=1,row=5)
list1=ttk.Combobox(tab1,width=50,textvariable=lista1)
list1['values']=("Col1","Col2","Col3")
list1.grid(column=2,row=5)
list1.current(0)

lista2=ttk.Label(tab1,text='Municipio')
lista2.grid(column=1,row=6)
list2=ttk.Combobox(tab1,width=50,textvariable=lista2)
list2['values']=("Mun1","Mun2","Mun3")
list2.grid(column=2,row=6)
list2.current(0)

lista3=ttk.Label(tab1,text='Ciudad')
lista3.grid(column=1,row=7)
list3=ttk.Combobox(tab1,width=50,textvariable=lista3)
list3['values']=("Ci1","Ci2","Ci3")
list3.grid(column=2,row=7)
list3.current(0)

def fun():
    awar=ttk.Label(tab1,text='Llena todo')
    if(preguntarap==""):
        awar.grid(column=5,row=9)
    if(preguntarapm==""):
        awar.grid(column=5,row=9)
    if(preguntardirr==""):
        awar.grid(column=5,row=9)
    if(preguntarnom==""):
        awar.grid(column=5,row=9)
    
    accion.configure(text='Impreso')
accion=ttk.Button(tab1,text='Imprimir Formulario',command=fun)
accion.grid(column=5,row=10)

tab2=ttk.Frame(tabControl)
tabControl.add(tab2,text='DatosExtras')

pas=ttk.Label(tab2,text='Pasatiempos')
pas.grid(column=1,row=1)

opcion=tk.IntVar()
opcion2=tk.IntVar()
opcion3=tk.IntVar()
radio1=ttk.Radiobutton(tab2,text='Leer',variable=opcion)
radio1.grid(column=1,row=2,sticky=tk.W)

radio2=ttk.Radiobutton(tab2,text='Peliculas',variable=opcion2)
radio2.grid(column=3,row=2,sticky=tk.W)

radio3=ttk.Radiobutton(tab2,text='Redes Sociales',variable=opcion3)
radio3.grid(column=5,row=2,sticky=tk.W)

opcion4=tk.IntVar()
ec=ttk.Label(tab2,text='Estado Civil')
ec.grid(column=1,row=3)
radio4=ttk.Radiobutton(tab2,text='Soltero',variable=opcion4)
radio4.grid(column=1,row=4,sticky=tk.W)
radio5=ttk.Radiobutton(tab2,text='Casado',variable=opcion4)
radio5.grid(column=3,row=4,sticky=tk.W)
radio6=ttk.Radiobutton(tab2,text='Viudo',variable=opcion4)
radio6.grid(column=5,row=4,sticky=tk.W)

caj=ttk.Label(tab2,text='Proposito en la vida')
caj.grid(column=1,row=6)
scrol_ancho=30
scrol_alto=6
caja=scrolledtext.ScrolledText(tab2,width=scrol_ancho,height=scrol_alto,wrap=tk.WORD)
caja.grid(column=1,row=7)

def fun2():
    bot.configure(text='Impreso')

bot=ttk.Button(tab2,text='Imprimir datos',command=fun2)
bot.grid(column=7,row=9)

def fun5():
    mBox.showinfo('Pagina creada por Orlando Ochoa Magallan')

def fun4():
    ventana.quit()
    ventana.destroy()
    exit()

ventana.configure(menu=barra_menu)
menua=Menu(barra_menu,tearoff=0)
menua.add_command(label="Acerca de",command=fun5)
barra_menu.add_cascade(label="Ayuda",menu=menua)


menub=Menu(barra_menu,tearoff=0)
menub.add_command(label="Salir",command=fun4)
menub.add_command(label="Imprimir")
barra_menu.add_cascade(label="Sistema",menu=menub)
ventana.mainloop()


