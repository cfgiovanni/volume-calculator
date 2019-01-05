import tkinter as tk
from functools import partial
import numpy as np

 
def call_result(label_result, n1, n2, n3, n4, n5):
    p = float(n1.get())
    t = float(n2.get())
    pc = float(n3.get())
    tc = float(n4.get())
    fa = float(n5.get())

    # Equação dos Gases Ideiais

    volumeGI = 8.314*t/p

    # Equação de Van der Waals
    
    u=0
    w=0
    a=0.421875*69.122596*tc*tc/pc
    b=8.314*tc/(8*pc)

    poly = np.polynomial.Polynomial([(-p*w*b**3-8.314*t*w*b**2-a*b),(p*w*b**2-p*u*b**2-8.314*t*u*b+a),(p*u*b-p*b-8.314*t),p])
    lista = poly.roots()

    cont=0
    msg0 = str(lista)
    
    for i in range(len(lista)):
        if round(lista[i].imag,3) == 0:
            cont=cont+1
    if cont == 3:
        if round(lista[0].real,4) == round(lista[1].real,4) == round(lista[2].real,4):
            msg1 = ("Há três raízes reais e iguais (Composto no Ponto Crítico) ")
            for i in range(len(lista)):
                if lista[i].imag == 0:
                    msg2 = ("Volume = " + str(round(lista[i].real,6))+ " m3/mol")

        elif round(lista[0].real,4) != round(lista[1].real,4) != round(lista[2].real,4):
            msg1 = ("Há três raízes reais diferentes (Líquido e vapor) ")
            if round(lista[0].real,4)>round(lista[1].real,4) and round(lista[0].real,4)>round(lista[2].real,4):
                if round(lista[1].real,4)>round(lista[2].real,4):
                    msg2 = ("Volume da fase gasosa = " + str(round(lista[0].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[2].real,6)) + " m3/mol")
                else:
                    msg2 = ("Volume da fase gasosa = " + str(round(lista[0].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[1].real,6)) + " m3/mol")

            elif round(lista[1].real,4)>round(lista[0].real,4) and round(lista[1].real,4)>round(lista[2].real,4):
                if round(lista[2].real,4)>round(lista[0].real,4):
                    msg2 = ("Volume da fase gasosa = " + str(round(lista[1].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[0].real,6)) + " m3/mol")
                else:
                    msg2 = ("Volume da fase gasosa = " + str(round(lista[1].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[2].real,6)) + " m3/mol")

            elif round(lista[2].real,4)>round(lista[0].real,4) and round(lista[2].real,4)>round(lista[1].real,4):
                if round(lista[1].real,4)>round(lista[0].real,4):
                    msg2 = ("Volume da fase gasosa = " + str(round(lista[2].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[0].real,6)) + " m3/mol")
                else:
                    msg2 = ("Volume da fase gasosa = " + str(round(lista[2].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[1].real,6)) + " m3/mol")
        else:
            
             msg1 = ("Composto na região crítica (Dois valores de volumes iguais)")
             msg2 = ("Volume 1 = " + str(round(lista[0].real,6))+" m3/mol"+
                     "\nVolume  2 = " + str(round(lista[1].real,6))+" m3/mol"+
                     "\nVolume  3 = " + str(round(lista[2].real,6))+" m3/mol")
            
    if cont == 1:
        msg1 = ("Há um volume real (Vapor superaquecido) ")
        for i in range(len(lista)):
             if round(lista[i].imag,3) == 0:
                msg2 = ("Volume = " + str(round(lista[i].real,6))+" m3/mol")


    # Equação de Redlich-Kwong

    u=1
    w=0
    a=(0.42748*(8.314**2)*tc**(2.5))/(pc*t**0.5)
    b=0.08664*8.314*tc/pc

    poly = np.polynomial.Polynomial([(-p*w*b**3-8.314*t*w*b**2-a*b),(p*w*b**2-p*u*b**2-8.314*t*u*b+a),(p*u*b-p*b-8.314*t),p])
    lista = poly.roots()

    cont=0
    msg00 = str(lista)
    
    for i in range(len(lista)):
        if round(lista[i].imag,3) == 0:
            cont=cont+1
    if cont == 3:
        if round(lista[0].real,4) == round(lista[1].real,4) == round(lista[2].real,4):
            msg11 = ("Há três raízes reais e iguais (Composto no Ponto Crítico) ")
            for i in range(len(lista)):
                if lista[i].imag == 0:
                    msg22 = ("Volume = " + str(round(lista[i].real,6))+ " m3/mol")

        elif round(lista[0].real,4) != round(lista[1].real,4) != round(lista[2].real,4):
            msg11 = ("Há três raízes reais diferentes (Líquido e vapor) ")
            if round(lista[0].real,4)>round(lista[1].real,4) and round(lista[0].real,4)>round(lista[2].real,4):
                if round(lista[1].real,4)>round(lista[2].real,4):
                    msg22 = ("Volume da fase gasosa = " + str(round(lista[0].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[2].real,6)) + " m3/mol")
                else:
                    msg22 = ("Volume da fase gasosa = " + str(round(lista[0].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[1].real,6)) + " m3/mol")

            elif round(lista[1].real,4)>round(lista[0].real,4) and round(lista[1].real,4)>round(lista[2].real,4):
                if round(lista[2].real,4)>round(lista[0].real,4):
                    msg22 = ("Volume da fase gasosa = " + str(round(lista[1].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[0].real,6)) + " m3/mol")
                else:
                    msg22 = ("Volume da fase gasosa = " + str(round(lista[1].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[2].real,6)) + " m3/mol")

            elif round(lista[2].real,4)>round(lista[0].real,4) and round(lista[2].real,4)>round(lista[1].real,4):
                if round(lista[1].real,4)>round(lista[0].real,4):
                    msg22 = ("Volume da fase gasosa = " + str(round(lista[2].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[0].real,6)) + " m3/mol")
                else:
                    msg22 = ("Volume da fase gasosa = " + str(round(lista[2].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[1].real,6)) + " m3/mol")

        else:
             msg11 = ("Composto na região crítica (Dois valores de volumes iguais)")
             msg22 = ("Volume 1 = " + str(round(lista[0].real,6))+" m3/mol"+
                     "\nVolume  2 = " + str(round(lista[1].real,6))+" m3/mol"+
                     "\nVolume  3 = " + str(round(lista[2].real,6))+" m3/mol")
            
    if cont == 1:
        msg11 = ("Há um volume real (Vapor superaquecido) ")
        for i in range(len(lista)):
             if round(lista[i].imag,3) == 0:
                msg22 = ("Volume = " + str(round(lista[i].real,6))+" m3/mol")


    # Equação de Peng-Robinson

    u=2
    w=-1
    k=0.37464+1.54226*fa-0.26992*fa**2
    alfa=(1+k*(1-(t/tc)**0.5))**2
    a=0.45724*(8.314**2)*(tc**2)*alfa/pc 
    b=0.07780*8.314*tc/pc

    poly = np.polynomial.Polynomial([(-p*w*b**3-8.314*t*w*b**2-a*b),(p*w*b**2-p*u*b**2-8.314*t*u*b+a),(p*u*b-p*b-8.314*t),p])
    lista = poly.roots()

    cont=0
    msg000 = str(lista)
    
    for i in range(len(lista)):
        if round(lista[i].imag,3) == 0:
            cont=cont+1
    if cont == 3:
        if round(lista[0].real,4) == round(lista[1].real,4) == round(lista[2].real,4):
            msg111 = ("Há três raízes reais e iguais (Composto no Ponto Crítico) ")
            for i in range(len(lista)):
                if lista[i].imag == 0:
                    msg222 = ("Volume = " + str(round(lista[i].real,6))+ " m3/mol")

        elif round(lista[0].real,4) != round(lista[1].real,4) != round(lista[2].real,4):
            msg111 = ("Há três raízes reais diferentes (Líquido e vapor) ")
            if round(lista[0].real,4)>round(lista[1].real,4) and round(lista[0].real,4)>round(lista[2].real,4):
                if round(lista[1].real,4)>round(lista[2].real,4):
                    msg222 = ("Volume da fase gasosa = " + str(round(lista[0].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[2].real,6)) + " m3/mol")
                else:
                    msg222 = ("Volume da fase gasosa = " + str(round(lista[0].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[1].real,6)) + " m3/mol")

            elif round(lista[1].real,4)>round(lista[0].real,4) and round(lista[1].real,4)>round(lista[2].real,4):
                if round(lista[2].real,4)>round(lista[0].real,4):
                    msg222 = ("Volume da fase gasosa = " + str(round(lista[1].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[0].real,6)) + " m3/mol")
                else:
                    msg222 = ("Volume da fase gasosa = " + str(round(lista[1].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[2].real,6)) + " m3/mol")

            elif round(lista[2].real,4)>round(lista[0].real,4) and round(lista[2].real,4)>round(lista[1].real,4):
                if round(lista[1].real,4)>round(lista[0].real,4):
                    msg222 = ("Volume da fase gasosa = " + str(round(lista[2].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[0].real,6)) + " m3/mol")
                else:
                    msg222 = ("Volume da fase gasosa = " + str(round(lista[2].real,6)) + " m3/mol"+
                            "\nVolume da fase líquida = " + str(round(lista[1].real,6)) + " m3/mol")

        else:
             msg111 = ("Composto na região crítica (Dois valores de volumes iguais)")
             msg222 = ("Volume 1 = " + str(round(lista[0].real,6))+" m3/mol"+
                     "\nVolume  2 = " + str(round(lista[1].real,6))+" m3/mol"+
                     "\nVolume  3 = " + str(round(lista[2].real,6))+" m3/mol")
            
    if cont == 1:
        msg111 = ("Há um volume real (Vapor superaquecido) ")
        for i in range(len(lista)):
             if round(lista[i].imag,3) == 0:
                msg222 = ("Volume = " + str(round(lista[i].real,6))+" m3/mol")



    label_result.config(text= "(1) Equação de Gás Ideal: " + "Volume = "+str(round(volumeGI,7)) +" m3/mol"+
                        "\n " +
                        "\n(2) Equação de Van der Waals: " + "\n " + " \nRaízes de volume : " + msg0 + "\n " + "\n"+msg1 + "\n"+msg2+
                        "\n " +
                        "\n(3) Equação de Redlich-Kwong: " + "\n " + " \nRaízes de volume : " + msg00 + "\n " + "\n"+msg11 + "\n"+msg22+
                        "\n " +
                        "\n(4) Equação de Peng-Robinson: " + "\n " + " \nRaízes de volume : " + msg000 + "\n " + "\n"+msg111 + "\n"+msg222+
                        "\n " +
                        "\nImportante: desconsiderou-se partes imaginárias da ordem de décimo de milésimo (10^-4). As partes reais foram " +
                        "\narredondadas para quatro casas a fim de se comparar igualdade. As características físicas podem mudar conforme" +
                        "\ncondições dadas, portanto é importante também inspecionar os valores de raízes de volume fornecidos.")
    return

 
root = tk.Tk()
root.geometry('800x700+0+0')
root.title('Calculador de Volume')
 
number1 = tk.StringVar()
number2 = tk.StringVar()
number3 = tk.StringVar()
number4 = tk.StringVar()
number5 = tk.StringVar()
 
labelTitle = tk.Label(root, text="Calculador de Volume").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Pressão (Pa) ").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Temperatura (K) ").grid(row=2, column=0)
labelNum2 = tk.Label(root, text="Pressão Crítica (Pa)").grid(row=3, column=0)
labelNum2 = tk.Label(root, text="Temperatura Crítica (K) ").grid(row=4, column=0)
labelNum2 = tk.Label(root, text="Fator Acêntrico").grid(row=5, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)
 
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=3, column=2)
entryNum4 = tk.Entry(root, textvariable=number4).grid(row=4, column=2)
entryNum5 = tk.Entry(root, textvariable=number5).grid(row=5, column=2)
call_result = partial(call_result, labelResult, number1, number2, number3, number4, number5)
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=6, column=0)

root.mainloop()
    
