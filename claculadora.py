def calculadora():
    print("Calculadora Robusta v1.0")
    print("Bienvenido, GojoWill!")

    while True:
        print("/n---Nueva operacion---")
        #Pedir primer numero
        while True:
            try:
                num1=float(input("Ingresa el primer numero: "))
                break
            except ValueError:
                print("Eso no es un numero. Intenta de nuevo.")
        while True:
            try:
                num2=float(input("Ingresa el segundo numero: "))
                break
            except ValueError:
                print("Eso no es un numero. Intenta de nuevo.")
        #Mostrar las opciones
        print("/nOperaciones:")
        print("1. Sumar (+)")
        print("2. Restar (-)")
        print("3. Multiolicar (*)")
        print("4. Dividir (/)")
        operacion=input("Elige una de estas opciones (1/2/3/4): ")
        
        #Hacer el calculo
        if operacion=="1":
            resultado=num1+num2
            print(f"{num1}+{num2}={resultado}")
        elif operacion=="2":
            resultado=num1-num2
            print(f"{num1}-{num1}={resultado}")
        elif operacion=="3":
            resultado=num1*num2
            print(f"{num1}*{num2}={resultado}")
        elif operacion=="4":
            if num2==0:
                print("Error: no se puede dividir por cero.")
            else:
                resultado=num1/num2
                print(f"{num1}/{num2}={resultado}")
        else:
            print("Opcion no valida.")
        
        #Preguntar si quiere continuar
        continuar=input("n/Quieres hacer otra operacion? (s/n): ").lower()
        if continuar != "s":
            print("Hasta luego, GojoWill")
            break

#Llamar la funcion
calculadora()
