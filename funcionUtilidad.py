# Para instalar pyton https://www.python.org/downloads/
# Para instalar numpy correr en consola pip3 install numpy  https://pypi.org/project/numpy/
# Para instalar matplotlib correr en consola pip3 install matplotlib  https://pypi.org/project/matplotlib/
# Para instalar math correr en consola pip3 install maths https://pypi.org/project/maths/
# para correr Entrar a la carpeta donde está el archivo funcionUtilidad.py, esto se hace utilizando el comando cd
# Por ejemplo en mi computadora está en la carpeta Desktop, así que ejecutaré: cd Desktop   
# después ls   para verificar que el archivo se encuentra ahí y lo ejecutaré con: python3 funcionUtilidad.py
import numpy as np
import math
import matplotlib.pyplot as plt
def funcionUtilidad():
    continuar = "SI"
    while continuar.upper() == "SI":
        maxC = []
        minC = []
        Costs =[]
        Utility=[]
        A=[]
        print("¿Cuántos costos diferentes deseas analizar?")
        nC = int(input())
        print("Si conoce las utilidades presione 1, si conoce la funcion de utilidad presione 2")
        decision=input()
        if decision == '1':
            print("Ingrese sus costos y las utilidades asignadas a ellos")
            for i in range(nC):
                print("Ingrese su costo %i"%(i+1))
                cost=float(input())
                print("Ingrese su utilidad %i"%(i+1))
                utility=float(input())
                Costs.append([cost,utility])
            Costs.sort()
            A = np.transpose(Costs)
            print("COSTOS:",A[0])
            print("UTILIDADES:",A[1])
            maxC = max(A[0])
            minC = min(A[0])
            plt.plot(A[1], A[0])
            plt.xlabel('Utilidad')
            plt.ylabel('Costo')
            plt.show()
        elif decision == '2':
            print("Ingrese sus costos")
            for i in range(nC):
                print("Ingrese su costo %i"%(i+1))
                cost=float(input())
                Costs.append(cost)
            for costo in Costs:
############ LA FUNCION DEPENDE DE QUIEN TOME LA DECISIÓN  ######################################################
                funcionUtilidad = math.sqrt(costo)
                Utility.append(funcionUtilidad)
            for i,costo in enumerate(Costs):
                A.append([costo,Utility[i]])
            print("COSTOS:",Costs)
            print("UTILIDADES:",Utility)
            A.sort()
            A = np.transpose(A)
            plt.plot(A[1], A[0])
            plt.xlabel('Utilidad')
            plt.ylabel('Costo')
            plt.show()
            maxC = max(Costs)
            minC = min(Costs)
        else:
            print("No se eligió una opción válida")
        print("Deseas realizar otro cálculo SI/NO")
        continuar=input()

try:
    funcionUtilidad()
except ValueError:
    print('TODO LO QUE DEBES INGRESAR SON NÚMEROS')
