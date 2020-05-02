# Para instalar pyton https://www.python.org/downloads/
# Para instar numpy correr en consola pip3 install numpy o https://www.youtube.com/watch?v=MC-74iN9QmQ
# para correr Entrar a la carpeta donde está el archivo VEIPyVEIM.py, esto se hace utilizando el comando cd
# Por ejemplo en mi computadora está en la carpeta Desktop, así que ejecutaré: cd Desktop   
# después ls   para verificar que el archivo se encuentra ahí y lo ejecutaré con: python3 VEIPyVEIM.py
import numpy as np
def VEIP():
    continuar = "SI"
    while continuar.upper() == "SI":
        VEIP=[]
        VECIP =0
        VME =[]
        A=[]
        S = []
        Atrans =[]
        print("VALOR ESPERADO DE LA INFORMACIÓN PERFECTA")
        print("INGRESE LA CANTIDAD DE ALTERNATIVAS")
        alternativas = int(input())
        print("INGRESE LA CANTIDAD DE ESTADOS DE LA NATURALEZA")
        esna = int(input())
        if type(alternativas) == int:
            for i in range(alternativas):
                print("Se ingresarán los valores de la alternativa %i" %(i+1))
                semimatriz=[]
                for j in range(esna):
                    print("Ingresa un valor y presiona ENTER")
                    a = float(input())
                    if type(a) == type(2.0):
                        semimatriz.append(a)
                A.append(semimatriz)
        print("INGRESA LOS VALORES DE TUS PROBABILIDADES")
        for j in range(esna):
            print("Ingresa un valor y presiona ENTER")
            a = float(input())
            S.append(a)
        print("Valores de las alternativas ",A)
        print("Valores de las probabilidades ",S)
        Atrans=np.transpose(A)
        print(Atrans)
        Sum=sum(S)
        if Sum == 1:
            vecip=[]
            for i in range(alternativas):
                resultados=[]
                for j in range(esna):
                    valores = A[i][j]*S[j]
                    resultados.append(valores)
                VME.append(sum(resultados))
            for i in range(len(VME)):
                print("Valor esperado en VME%i = %f" %(i+1,VME[i]))
            for i in range(esna):
                a=0
                operacion=0
                a=max(Atrans[i])
                operacion = a*S[i]
                vecip.append(operacion)
            VECIP=sum(vecip)
            print("Valor esperado en VECIP = %f" %(VECIP))
            VEIP = VECIP - max(VME)
            print("Valor esperado en VEIP = %f" %(VEIP))
        else:
            print("La suma de todas las probabilidades debe ser igual a 1")


        ######## CÁLCULO DE VEIM ######################################################
        print("¿Desea realizar el cálculo de VEIM SI/NO")
        print("VALOR ESPERADO DE LA INFORMACIÓN MUESTRAL")
        estadoSS=['Favorable','Desfavorable']
        PSS=[]
        SS = []
        SSD=[]
        SSF=[]
        VEIM= []
        VEconIM=[]
        E=[]
        decVEIM=input()
        print("Ingrese el costo por investigar")    
        costo = float(input())
        if decVEIM.upper() == "SI":
            for i in range(esna):
                probabilidad=[]
                print('Ingrese los valores para los estados de la naturaleza %i'%(i+1))
                for j in range(2):
                    if j ==0:
                        print("Ingrese el valor para el estado %s"%estadoSS[j])
                        a= float(input())
                        probabilidad.append(a)
                    elif j==1 and probabilidad[0]<=1:
                        print("El valor para el estado %s es %f"%(estadoSS[j],1-probabilidad[0]))
                        probabilidad.append(1-probabilidad[0])
                    else:
                        print("Los valores de la probabilidad fueron incorrectos, deben sumar 1")
                SS.append(probabilidad)
            print(SS)
            for i in range(len(S)):
                for j in range(2):
                    if j == 0:
                        a=S[i]*SS[i][j]
                        SSF.append(a)
                    elif j == 1:
                        a=S[i]*SS[i][j]
                        SSD.append(a)
            SS=[]
            SS.append(sum(SSF))
            SS.append(sum(SSD))
            for i,ss in enumerate(SS):
                pss=[]
                if i == 1:
                    for ssd in SSD:
                        pss.append(ssd/ss)
                    PSS.append(pss)
                elif i == 0:
                    for ssf in SSF:
                        pss.append(ssf/ss)
                    PSS.append(pss)          
            print(PSS)
            A = np.asmatrix(A)
            PSS = np.transpose(PSS)
            PSS = np.asmatrix(PSS)
            E = np.dot(A,PSS)
            print("Matriz de estados",E)
            E = E.tolist()
            for i in range(len(E)):
                VEconIM.append(E[i][0]*SS[i])
            VEconIM=sum(VEconIM)
            print("El valor de VEconIM es", VEconIM)
            print("El valor del costo es", costo)
            print("El máximo valor de VME es", max(VME))
            VEIM = VEconIM + costo - max(VME)
            print("Por lo tanto el valor de VEIM es", VEIM)
        print("Deseas realizar otro cálculo SI/NO")
        continuar=input()


try:
    #print("Si quieres realizar un cálculo de VEIP presiona 1 y ENTER, si quieres un cálculo de VEIM presiona 2")
    #elegir = input()
    #if elegir == '1':
    #    print("Elegiste VEIM")
    VEIP()
    #elif elegir == '2':
    #    print("Elegiste VEIM")

        
except ValueError:
    print('TODO LO QUE DEBES INGRESAR SON NÚMEROS')

