from tkinter import *
from tkinter import messagebox

root = Tk()

root.title('Casino Crew - GTA Online')
root.resizable(False, False)


#------Formulas y Funciones-----

opcionConductor = IntVar()

opcionPistolero = IntVar()

opcionHacker = IntVar()

opcionBotin = IntVar()





tajadaTotal = 0

costoCrew = 0

def calculo_tajada():

    '''
    Calcula el valor de la tajada basado
    en el costo porcentual de la crew.

    '''
    def tajada():

        global opcionBotin

        global tajadaTotal

        if opcionBotin.get() == 1:
            tajadaTotal = 2326500

        if opcionBotin.get() == 2:
            tajadaTotal = 2585000

        if opcionBotin.get() == 3:
            tajadaTotal = 2843500

        if opcionBotin.get() == 4:
            tajadaTotal = 3619000

        return tajadaTotal

    def calculoCrew():

        global opcionConductor
        global opcionPistolero
        global opcionHacker
        global costoCrew

        conductor = opcionConductor.get()
        pistolero = opcionPistolero.get()
        hacker = opcionHacker.get()

        costoCrew = (conductor + pistolero + hacker) / 100

        return costoCrew

    tajada()

    calculoCrew()


    valor1 = tajadaTotal*costoCrew

    valor2 = tajadaTotal-valor1


    return messagebox.showinfo('Calcular tajada', 'La tajada total es: '+ str(valor2))





#---------Frames---------
Frame0 = Frame(root)
Frame0.pack()

Frame1 = Frame(Frame0)
Frame1.pack(side=LEFT)

Frame2 = Frame(Frame0)
Frame2.pack(side=LEFT)

Frame3 = Frame(Frame0)
Frame3.pack(side=LEFT)

Frame4 = Frame(root)
#Frame4.grid(row=7, column=0, rowspan=1, columnspan=4)
Frame4.pack(side=BOTTOM)

#--------Pistoleros--------

LabelPistolero = Label(Frame1, text='PISTOLERO', pady=10)
LabelPistolero.grid(row=0, column=0)

BotonPistolero1 = Radiobutton(Frame1, text='Karl Abolaji (5%)', variable=opcionPistolero, value=5)
BotonPistolero1.grid(row=1, column=0)
BotonPistolero2 = Radiobutton(Frame1, text='Charlie Reed (7%)', variable=opcionPistolero, value=7)
BotonPistolero2.grid(row=2, column=0)
BotonPistolero3 = Radiobutton(Frame1, text='Patrick McReary (8%)', variable=opcionPistolero, value=8)
BotonPistolero3.grid(row=3, column=0)
BotonPistolero4 = Radiobutton(Frame1, text='Gustavo Mota (9%)', variable=opcionPistolero, value=9)
BotonPistolero4.grid(row=4, column=0)
BotonPistolero5 = Radiobutton(Frame1, text='Chester Mckoy (10%)', variable=opcionPistolero, value=10)
BotonPistolero5.grid(row=5, column=0)

#---------Conductores--------

LabelConductor = Label(Frame2, text='CONDUCTOR', pady=10)
LabelConductor.grid(row=0, column=0)


BotonConductor1 = Radiobutton(Frame2, text='Karim Denz (5%)', variable=opcionConductor, value=5)
BotonConductor1.grid(row=1, column=0)
BotonConductor2 = Radiobutton(Frame2, text='Zach Nelson (6%)', variable=opcionConductor, value=6)
BotonConductor2.grid(row=2, column=0)
BotonConductor3 = Radiobutton(Frame2, text='Taliana Martinez (7%)', variable=opcionConductor, value=7)
BotonConductor3.grid(row=3, column=0)
BotonConductor4 = Radiobutton(Frame2, text='Eddie Toh (9%)', variable=opcionConductor, value=9)
BotonConductor4.grid(row=4, column=0)
BotonConductor5 = Radiobutton(Frame2, text='Chester Mckoy (10%)', variable=opcionConductor, value=10)
BotonConductor5.grid(row=5, column=0)


#----------Hackers-----------

LabelHacker = Label(Frame3, text='HACKER', pady=10)
LabelHacker.grid(row=0, column=0)


BotonHacker1 = Radiobutton(Frame3, text='Rickie Lukens (3%)', variable=opcionHacker, value=3)
BotonHacker1.grid(row=1, column=0)
BotonHacker2 = Radiobutton(Frame3, text='Yohan Blair (5%)', variable=opcionHacker, value=5)
BotonHacker2.grid(row=2, column=0)
BotonHacker3 = Radiobutton(Frame3, text='Christian Feltz (7%)', variable=opcionHacker, value=7)
BotonHacker3.grid(row=3, column=0)
BotonHacker4 = Radiobutton(Frame3, text='Paige Harris (9%)', variable=opcionHacker, value=9)
BotonHacker4.grid(row=4, column=0)
BotonHacker5 = Radiobutton(Frame3, text='Avi Schwartzman (10%)', variable=opcionHacker, value=10)
BotonHacker5.grid(row=5, column=0)


#---------Botines----------

LabelBotin = Label(Frame4, text='BOTIN')
LabelBotin.grid(row=0, columnspan=4)

BotonDinero = Radiobutton(Frame4, text='Dinero', variable=opcionBotin, value=1, pady=20)
BotonDinero.grid(row=1, column=0)
BotonCuadros = Radiobutton(Frame4, text='Obras de Arte', variable=opcionBotin, value=2, pady=20)
BotonCuadros.grid(row=1, column=1)
BotonOro = Radiobutton(Frame4, text='Oro', variable=opcionBotin, value=3, pady=20)
BotonOro.grid(row=1, column=2)
BotonDiamantes = Radiobutton(Frame4, text='Diamantes', variable=opcionBotin, value=4, pady=20)
BotonDiamantes.grid(row=1, column=3)


#------Boton de resultado-------

BotonResultado = Button(Frame4, text='Calcular tajada', padx=15, pady=5, command=calculo_tajada)
BotonResultado.grid(row=3, columnspan=4)





root.mainloop()
