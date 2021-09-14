# Import librarys
from tkinter import *
import random
import sys
from PIL import ImageTk, Image


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def setP(valor):
    global PS
    PS = valor
    print(PS)
    return


def setL(valor):
    global LS
    LS = valor
    print(LS)
    return


def setA(valor):
    global AS
    AS = valor
    print(AS)
    return


def p1():
    btn.grid_forget()
    btn.pack_forget()
    btn.place_forget()
    lbl.configure(text="Tenemos cinco sospechosos,\n cinco lugares posibles\n y cinco armas posibles",
                  font=("Arial", 25))
    btn1.place(x=340, y=360, anchor="center")


def p2():
    btn1.grid_forget()
    btn1.pack_forget()
    btn1.place_forget()
    lbl.configure(text="Puedes hacer cinco preguntas, \ndepues debes elegir, \nBuena suerte!", font=("Arial", 25))
    btn2.place(x=340, y=360, anchor="center")


def p3():
    global count
    btnJP.grid_forget()
    btnJP.pack_forget()
    btnJP.place_forget()
    btnRO.grid_forget()
    btnRO.pack_forget()
    btnRO.place_forget()
    btnIG.grid_forget()
    btnIG.pack_forget()
    btnIG.place_forget()
    btnDG.grid_forget()
    btnDG.pack_forget()
    btnDG.place_forget()
    btnST.grid_forget()
    btnST.pack_forget()
    btnST.place_forget()
    #
    btnL1.grid_forget()
    btnL1.pack_forget()
    btnL1.place_forget()
    btnL5.grid_forget()
    btnL5.pack_forget()
    btnL5.place_forget()
    btnB2.grid_forget()
    btnB2.pack_forget()
    btnB2.place_forget()
    btnRE.grid_forget()
    btnRE.pack_forget()
    btnRE.place_forget()
    btnOS.grid_forget()
    btnOS.pack_forget()
    btnOS.place_forget()
    #
    btnDE.grid_forget()
    btnDE.pack_forget()
    btnDE.place_forget()
    btnCU.grid_forget()
    btnCU.pack_forget()
    btnCU.place_forget()
    btnPV.grid_forget()
    btnPV.pack_forget()
    btnPV.place_forget()
    btnCA.grid_forget()
    btnCA.pack_forget()
    btnCA.place_forget()
    btnLC.grid_forget()
    btnLC.pack_forget()
    btnLC.place_forget()
    #
    btnRegresar.grid_forget()
    btnRegresar.pack_forget()
    btnRegresar.place_forget()
    #
    lbl.grid_forget()
    lbl.pack_forget()
    lbl.place_forget()
    btn2.grid_forget()
    btn2.pack_forget()
    btn2.place_forget()
    if count < 5:
        btnp.place(x=340, y=100, anchor="center")
        btnl.place(x=340, y=200, anchor="center")
        btna.place(x=340, y=300, anchor="center")
    else:
        lbl.configure(text="Debes elegir a un culpable, ahora", font=("Arial", 25))
        lbl.place(x=340, y=190, anchor="center")
        btnCulpable.place(x=340, y=360, anchor="center")


def personajes():
    btnp.grid_forget()
    btnp.pack_forget()
    btnp.place_forget()
    btnl.grid_forget()
    btnl.pack_forget()
    btnl.place_forget()
    btna.grid_forget()
    btna.pack_forget()
    btna.place_forget()
    btnJP.place(x=340, y=60, anchor="center")
    btnRO.place(x=340, y=110, anchor="center")
    btnIG.place(x=340, y=160, anchor="center")
    btnDG.place(x=340, y=210, anchor="center")
    btnST.place(x=340, y=260, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def JP():
    global count, P, mensaje
    count += 1
    btnJP.grid_forget()
    btnJP.pack_forget()
    btnJP.place_forget()
    btnRO.grid_forget()
    btnRO.pack_forget()
    btnRO.place_forget()
    btnIG.grid_forget()
    btnIG.pack_forget()
    btnIG.place_forget()
    btnDG.grid_forget()
    btnDG.pack_forget()
    btnDG.place_forget()
    btnST.grid_forget()
    btnST.pack_forget()
    btnST.place_forget()
    if P == "1":
        mensaje = "Se vio a Juan en Línea 5"
    else:
        mensaje = "Se vio a Juan en recibo en la mañana"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def RO():
    global count, P, mensaje
    count += 1
    btnJP.grid_forget()
    btnJP.pack_forget()
    btnJP.place_forget()
    btnRO.grid_forget()
    btnRO.pack_forget()
    btnRO.place_forget()
    btnIG.grid_forget()
    btnIG.pack_forget()
    btnIG.place_forget()
    btnDG.grid_forget()
    btnDG.pack_forget()
    btnDG.place_forget()
    btnST.grid_forget()
    btnST.pack_forget()
    btnST.place_forget()
    if P == "2":
        mensaje = "Se vio a Rita en la oficina de seguridad"
    else:
        mensaje = "Se vio a Rita en Bullpen"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def IG():
    global count, P, mensaje
    count += 1
    btnJP.grid_forget()
    btnJP.pack_forget()
    btnJP.place_forget()
    btnRO.grid_forget()
    btnRO.pack_forget()
    btnRO.place_forget()
    btnIG.grid_forget()
    btnIG.pack_forget()
    btnIG.place_forget()
    btnDG.grid_forget()
    btnDG.pack_forget()
    btnDG.place_forget()
    btnST.grid_forget()
    btnST.pack_forget()
    btnST.place_forget()
    if P == "3":
        mensaje = "Se vio a Iván en el Recibo"
    else:
        mensaje = "Se vio a Ivan en Línea 1"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def DG():
    global count, P, mensaje
    count += 1
    btnJP.grid_forget()
    btnJP.pack_forget()
    btnJP.place_forget()
    btnRO.grid_forget()
    btnRO.pack_forget()
    btnRO.place_forget()
    btnIG.grid_forget()
    btnIG.pack_forget()
    btnIG.place_forget()
    btnDG.grid_forget()
    btnDG.pack_forget()
    btnDG.place_forget()
    btnST.grid_forget()
    btnST.pack_forget()
    btnST.place_forget()
    if P == "4":
        mensaje = "Se vio a David en Bullpen 2"
    else:
        mensaje = "Se vio a David en recibo en Linea 5"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def ST():
    global count, P, mensaje
    count += 1
    btnJP.grid_forget()
    btnJP.pack_forget()
    btnJP.place_forget()
    btnRO.grid_forget()
    btnRO.pack_forget()
    btnRO.place_forget()
    btnIG.grid_forget()
    btnIG.pack_forget()
    btnIG.place_forget()
    btnDG.grid_forget()
    btnDG.pack_forget()
    btnDG.place_forget()
    btnST.grid_forget()
    btnST.pack_forget()
    btnST.place_forget()
    if P == "5":
        mensaje = "Se vio a Juan en Línea 5"
    else:
        mensaje = "Se vio a Sandra en la oficina de seguridad"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def locaciones():
    btnp.grid_forget()
    btnp.pack_forget()
    btnp.place_forget()
    btnl.grid_forget()
    btnl.pack_forget()
    btnl.place_forget()
    btna.grid_forget()
    btna.pack_forget()
    btna.place_forget()
    btnL1.place(x=340, y=60, anchor="center")
    btnL5.place(x=340, y=110, anchor="center")
    btnB2.place(x=340, y=160, anchor="center")
    btnRE.place(x=340, y=210, anchor="center")
    btnOS.place(x=340, y=260, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def L1():
    global count, P, mensaje
    count += 1
    btnL1.grid_forget()
    btnL1.pack_forget()
    btnL1.place_forget()
    btnL5.grid_forget()
    btnL5.pack_forget()
    btnL5.place_forget()
    btnB2.grid_forget()
    btnB2.pack_forget()
    btnB2.place_forget()
    btnRE.grid_forget()
    btnRE.pack_forget()
    btnRE.place_forget()
    btnOS.grid_forget()
    btnOS.pack_forget()
    btnOS.place_forget()
    if L == "1":
        mensaje = "En Línea 1 se perdió un\n cable del inventario"
    else:
        mensaje = "Se inspecciono Línea 1 \ny no hubo discrepancias"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def L5():
    global count, P, mensaje
    count += 1
    btnL1.grid_forget()
    btnL1.pack_forget()
    btnL1.place_forget()
    btnL5.grid_forget()
    btnL5.pack_forget()
    btnL5.place_forget()
    btnB2.grid_forget()
    btnB2.pack_forget()
    btnB2.place_forget()
    btnRE.grid_forget()
    btnRE.pack_forget()
    btnRE.place_forget()
    btnOS.grid_forget()
    btnOS.pack_forget()
    btnOS.place_forget()
    if L == "2":
        mensaje = "En Línea 5 se pueden observar una \nventana rota y algunos pedazos de vidrio"
    else:
        mensaje = "Línea 5 esta está cerrada"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def B2():
    global count, P, mensaje
    count += 1
    btnL1.grid_forget()
    btnL1.pack_forget()
    btnL1.place_forget()
    btnL5.grid_forget()
    btnL5.pack_forget()
    btnL5.place_forget()
    btnB2.grid_forget()
    btnB2.pack_forget()
    btnB2.place_forget()
    btnRE.grid_forget()
    btnRE.pack_forget()
    btnRE.place_forget()
    btnOS.grid_forget()
    btnOS.pack_forget()
    btnOS.place_forget()
    if L == "3":
        mensaje = "Están realizando un trabajo\n y hay cajas de herramienta"
    else:
        mensaje = "Pasa mucha gente por aquí y todo\n está grabado, no se ve nada sospechoso"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def RE():
    global count, P, mensaje
    count += 1
    btnL1.grid_forget()
    btnL1.pack_forget()
    btnL1.place_forget()
    btnL5.grid_forget()
    btnL5.pack_forget()
    btnL5.place_forget()
    btnB2.grid_forget()
    btnB2.pack_forget()
    btnB2.place_forget()
    btnRE.grid_forget()
    btnRE.pack_forget()
    btnRE.place_forget()
    btnOS.grid_forget()
    btnOS.pack_forget()
    btnOS.place_forget()
    if L == "4":
        mensaje = "Se acaba de recibir una carga de químicos"
    else:
        mensaje = "Hoy fue un dia muy tranquilo en recibo"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def OS():
    global count, P, mensaje
    count += 1
    btnL1.grid_forget()
    btnL1.pack_forget()
    btnL1.place_forget()
    btnL5.grid_forget()
    btnL5.pack_forget()
    btnL5.place_forget()
    btnB2.grid_forget()
    btnB2.pack_forget()
    btnB2.place_forget()
    btnRE.grid_forget()
    btnRE.pack_forget()
    btnRE.place_forget()
    btnOS.grid_forget()
    btnOS.pack_forget()
    btnOS.place_forget()
    if L == "5":
        mensaje = "Seguridad confisco \nvarios cuter días antes"
    else:
        mensaje = "No se registró movimiento\n sospechoso en seguridad"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def armas():
    btnp.grid_forget()
    btnp.pack_forget()
    btnp.place_forget()
    btnl.grid_forget()
    btnl.pack_forget()
    btnl.place_forget()
    btna.grid_forget()
    btna.pack_forget()
    btna.place_forget()
    btnDE.place(x=340, y=60, anchor="center")
    btnCU.place(x=340, y=110, anchor="center")
    btnPV.place(x=340, y=160, anchor="center")
    btnCA.place(x=340, y=210, anchor="center")
    btnLC.place(x=340, y=260, anchor="center")


def DE():
    global count, P, mensaje
    count += 1
    btnDE.grid_forget()
    btnDE.pack_forget()
    btnDE.place_forget()
    btnCU.grid_forget()
    btnCU.pack_forget()
    btnCU.place_forget()
    btnPV.grid_forget()
    btnPV.pack_forget()
    btnPV.place_forget()
    btnCA.grid_forget()
    btnCA.pack_forget()
    btnCA.place_forget()
    btnLC.grid_forget()
    btnLC.pack_forget()
    btnLC.place_forget()
    if A == "1":
        mensaje = "Se encontró un desarmador fuera de lugar"
    else:
        mensaje = "Los desarmadores están en su lugar y bajo lave"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def CU():
    global count, P, mensaje
    count += 1
    btnDE.grid_forget()
    btnDE.pack_forget()
    btnDE.place_forget()
    btnCU.grid_forget()
    btnCU.pack_forget()
    btnCU.place_forget()
    btnPV.grid_forget()
    btnPV.pack_forget()
    btnPV.place_forget()
    btnCA.grid_forget()
    btnCA.pack_forget()
    btnCA.place_forget()
    btnLC.grid_forget()
    btnLC.pack_forget()
    btnLC.place_forget()
    if A == "2":
        mensaje = "Un cuter fue encontrado en la basura,\n alguien se deshizo de el"
    else:
        mensaje = "Los cuter están prohibidos y no se ha\n visto uno por ningún lado"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def PV():
    global count, P, mensaje
    count += 1
    btnDE.grid_forget()
    btnDE.pack_forget()
    btnDE.place_forget()
    btnCU.grid_forget()
    btnCU.pack_forget()
    btnCU.place_forget()
    btnPV.grid_forget()
    btnPV.pack_forget()
    btnPV.place_forget()
    btnCA.grid_forget()
    btnCA.pack_forget()
    btnCA.place_forget()
    btnLC.grid_forget()
    btnLC.pack_forget()
    btnLC.place_forget()
    if A == "3":
        mensaje = "Hoy se rompió una ventana"
    else:
        mensaje = "No ha habido accidentes con \ncosas de cristal"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def CA():
    global count, P, mensaje
    count += 1
    btnDE.grid_forget()
    btnDE.pack_forget()
    btnDE.place_forget()
    btnCU.grid_forget()
    btnCU.pack_forget()
    btnCU.place_forget()
    btnPV.grid_forget()
    btnPV.pack_forget()
    btnPV.place_forget()
    btnCA.grid_forget()
    btnCA.pack_forget()
    btnCA.place_forget()
    btnLC.grid_forget()
    btnLC.pack_forget()
    btnLC.place_forget()
    if A == "4":
        mensaje = "Los cables están por todos lados"
    else:
        mensaje = "Todos los cables están en su \nlugar y no falta ninguno"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def LC():
    global count, P, mensaje
    count += 1
    btnDE.grid_forget()
    btnDE.pack_forget()
    btnDE.place_forget()
    btnCU.grid_forget()
    btnCU.pack_forget()
    btnCU.place_forget()
    btnPV.grid_forget()
    btnPV.pack_forget()
    btnPV.place_forget()
    btnCA.grid_forget()
    btnCA.pack_forget()
    btnCA.place_forget()
    btnLC.grid_forget()
    btnLC.pack_forget()
    btnLC.place_forget()
    if A == "5":
        mensaje = "Hay varios envases abiertos\n y les falta contenido"
    else:
        mensaje = "Todos los envases están sellados\n y no falta ninguno"
    lbl.configure(text=mensaje, font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")
    btnRegresar.place(x=340, y=360, anchor="center")


def eleccionP():
    btnCulpable.grid_forget()
    btnCulpable.pack_forget()
    btnCulpable.place_forget()
    lbl.configure(text="¿Quien realizo el asesinato?", font=("Arial", 25))
    lbl.place(x=340, y=60, anchor="center")
    btnJPS.place(x=340, y=120, anchor="center")
    btnROS.place(x=340, y=170, anchor="center")
    btnIGS.place(x=340, y=220, anchor="center")
    btnDGS.place(x=340, y=270, anchor="center")
    btnSTS.place(x=340, y=320, anchor="center")

    btnSiguienteL.place(x=340, y=370, anchor="center")


def eleccionL():
    btnJPS.grid_forget()
    btnJPS.pack_forget()
    btnJPS.place_forget()
    btnROS.grid_forget()
    btnROS.pack_forget()
    btnROS.place_forget()
    btnIGS.grid_forget()
    btnIGS.pack_forget()
    btnIGS.place_forget()
    btnDGS.grid_forget()
    btnDGS.pack_forget()
    btnDGS.place_forget()
    btnSTS.grid_forget()
    btnSTS.pack_forget()
    btnSTS.place_forget()
    btnSiguienteL.grid_forget()
    btnSiguienteL.pack_forget()
    btnSiguienteL.place_forget()
    lbl.configure(text="¿Donde se realizo el asesinato?", font=("Arial", 25))
    lbl.place(x=340, y=60, anchor="center")
    btnL1S.place(x=340, y=120, anchor="center")
    btnL5S.place(x=340, y=170, anchor="center")
    btnB2S.place(x=340, y=220, anchor="center")
    btnRES.place(x=340, y=270, anchor="center")
    btnOSS.place(x=340, y=320, anchor="center")
    btnSiguienteA.place(x=340, y=370, anchor="center")


def eleccionA():
    btnL1S.grid_forget()
    btnL1S.pack_forget()
    btnL1S.place_forget()
    btnL5S.grid_forget()
    btnL5S.pack_forget()
    btnL5S.place_forget()
    btnB2S.grid_forget()
    btnB2S.pack_forget()
    btnB2S.place_forget()
    btnRES.grid_forget()
    btnRES.pack_forget()
    btnRES.place_forget()
    btnOSS.grid_forget()
    btnOSS.pack_forget()
    btnOSS.place_forget()
    btnSiguienteA.grid_forget()
    btnSiguienteA.pack_forget()
    btnSiguienteA.place_forget()
    lbl.configure(text="¿Que arma utilizo el asesino?", font=("Arial", 25))
    lbl.place(x=340, y=60, anchor="center")
    btnDES.place(x=340, y=120, anchor="center")
    btnCUS.place(x=340, y=170, anchor="center")
    btnPVS.place(x=340, y=220, anchor="center")
    btnCAS.place(x=340, y=270, anchor="center")
    btnLCS.place(x=340, y=320, anchor="center")
    btnFinal.place(x=340, y=370, anchor="center")


def Final():
    btnDES.grid_forget()
    btnDES.pack_forget()
    btnDES.place_forget()
    btnCUS.grid_forget()
    btnCUS.pack_forget()
    btnCUS.place_forget()
    btnPVS.grid_forget()
    btnPVS.pack_forget()
    btnPVS.place_forget()
    btnCAS.grid_forget()
    btnCAS.pack_forget()
    btnCAS.place_forget()
    btnLCS.grid_forget()
    btnLCS.pack_forget()
    btnLCS.place_forget()
    btnFinal.grid_forget()
    btnFinal.pack_forget()
    btnFinal.place_forget()
    if P == PS and L == LS and A == AS:
        lbl.configure(text="¡Acertaste!\n El asesino recibirá su castigo", font=("Arial", 25))
        lbl.place(x=340, y=160, anchor="center")
    else:
        lbl.configure(text="Te equivocaste, el asesino escapo", font=("Arial", 25))
        lbl.place(x=340, y=160, anchor="center")
    btnJugar.place(x=340, y=370, anchor="center")


def Volver():
    sys.exit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    global case, P, L, A, count, PS, LS, AS
    lista = ["1 2 3", "3 4 5", "5 1 4", "2 5 2", "4 3 1"]
    case = random.choice(lista)
    P = case.split()[0]
    L = case.split()[1]
    A = case.split()[2]
    count = 0

    PS = "0"
    LS = "0"
    AS = "0"

    print(P, L, A)

    root = Tk()
    root.title('Clue')
    root.geometry('680x380')
    lbl = Label(root, text="¡Oh no alguien mato al gerente!", font=("Arial", 25))
    lbl.place(x=340, y=190, anchor="center")

    btn = Button(root, text="Continuar", command=p1, height=2, width=30, bg='blue', fg='white')
    btn1 = Button(root, text="Continuar", command=p2, height=2, width=30, bg='blue', fg='white')
    btn2 = Button(root, text="Continuar", command=p3, height=2, width=30, bg='blue', fg='white')
    ###Opciones
    btnp = Button(root, text="Personaje", command=personajes, height=2, width=30, bg='blue', fg='white')
    btnl = Button(root, text="Locaciones", command=locaciones, height=2, width=30, bg='blue', fg='white')
    btna = Button(root, text="Armas", command=armas, height=2, width=30, bg='blue', fg='white')
    ###Regresar
    btnRegresar = Button(root, text="Regesar", command=p3, height=2, width=30, bg='blue', fg='white')
    ###Personajes
    btnJP = Button(root, text="Juan Perez, Ingeniero", command=JP, height=2, width=40, bg='blue', fg='white')
    btnRO = Button(root, text="Rita Ortiz, Gerente de piso", command=RO, height=2, width=40, bg='blue', fg='white')
    btnIG = Button(root, text="Ivan Gutierrez, Tecnico", command=IG, height=2, width=40, bg='blue', fg='white')
    btnDG = Button(root, text="David Guzman, Chofer", command=DG, height=2, width=40, bg='blue', fg='white')
    btnST = Button(root, text="Sandra Torrez, RH", command=ST, height=2, width=40, bg='blue', fg='white')
    ###Locaciones
    btnL1 = Button(root, text="Linea 1", command=L1, height=2, width=40, bg='blue', fg='white')
    btnL5 = Button(root, text="Linea 5", command=L5, height=2, width=40, bg='blue', fg='white')
    btnB2 = Button(root, text="Bullpen 2", command=B2, height=2, width=40, bg='blue', fg='white')
    btnRE = Button(root, text="Recibo", command=RE, height=2, width=40, bg='blue', fg='white')
    btnOS = Button(root, text="Oficina de seguridad", command=OS, height=2, width=40, bg='blue', fg='white')
    ###Armas
    btnDE = Button(root, text="Desarmador", command=DE, height=2, width=40, bg='blue', fg='white')
    btnCU = Button(root, text="Cuter", command=CU, height=2, width=40, bg='blue', fg='white')
    btnPV = Button(root, text="Pedazo de vidrio", command=PV, height=2, width=40, bg='blue', fg='white')
    btnCA = Button(root, text="Cable", command=CA, height=2, width=40, bg='blue', fg='white')
    btnLC = Button(root, text="Liquido corrosivo", command=LC, height=2, width=40, bg='blue', fg='white')
    ##Elejir culpable
    btnCulpable = Button(root, text="Elejir culpable", command=eleccionP, height=2, width=40, bg='blue', fg='white')
    ###Seleccion Personajes
    btnJPS = Button(root, text="Juan Perez, Ingeniero", command=lambda: setP("1"), height=2, width=40, bg='blue', fg='white')
    btnROS = Button(root, text="Rita Ortiz, Gerente de piso", command=lambda: setP("2"),
                    height=2, width=40, bg='blue', fg='white')
    btnIGS = Button(root, text="Ivan Gutierrez, Tecnico", command=lambda: setP("3"), height=2, width=40, bg='blue', fg='white')
    btnDGS = Button(root, text="David Guzman, Chofer", command=lambda: setP("4"), height=2, width=40, bg='blue', fg='white')
    btnSTS = Button(root, text="Sandra Torrez, RH", command=lambda: setP("5"), height=2, width=40, bg='blue', fg='white')
    ###Seleccion Locaciones
    btnL1S = Button(root, text="Linea 1", command=lambda: setL("1"), height=2, width=40, bg='blue', fg='white')
    btnL5S = Button(root, text="Linea 5", command=lambda: setL("2"), height=2, width=40, bg='blue', fg='white')
    btnB2S = Button(root, text="Bullpen 2", command=lambda: setL("3"), height=2, width=40, bg='blue', fg='white')
    btnRES = Button(root, text="Recibo", command=lambda: setL("4"), height=2, width=40, bg='blue', fg='white')
    btnOSS = Button(root, text="Oficina de seguridad", command=lambda: setL("5"),
                    height=2, width=40, bg='blue', fg='white')
    #Siguiente Lugar
    btnSiguienteL = Button(root, text="Siguiente", command=eleccionL, height=2, width=30, bg='blue', fg='white')
    ###Arma Seleccionada
    btnDES = Button(root, text="Desarmador", command=lambda: setA("1"), height=2, width=40, bg='blue', fg='white')
    btnCUS = Button(root, text="Cuter", command=lambda: setA("2"), height=2, width=40, bg='blue', fg='white')
    btnPVS = Button(root, text="Pedazo de vidrio", command=lambda: setA("3"), height=2, width=40, bg='blue', fg='white')
    btnCAS = Button(root, text="Cable", command=lambda: setA("4"), height=2, width=40, bg='blue', fg='white')
    btnLCS = Button(root, text="Liquido corrosivo", command=lambda: setA("5"), height=2, width=40, bg='blue', fg='white')
    # Siguiente Arma
    btnSiguienteA = Button(root, text="Siguiente", command=eleccionA, height=2, width=30, bg='blue', fg='white')
    ##Final
    btnFinal = Button(root, text="Momento de saber la verdad", command=Final, height=2, width=40, bg='blue', fg='white')
    ##Volver a jugar
    btnJugar = Button(root, text="Salir", command=Volver, height=2, width=40, bg='blue', fg='white')

    btn.place(x=340, y=360, anchor="center")
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
