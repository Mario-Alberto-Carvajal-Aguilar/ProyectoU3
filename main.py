import numpy as np
from math import *
res1 = 0
while res1 != 3:
    print("---- Menu Programa ----")
    print("1.- Metodo Jacobi")
    print("2.- Metodo Newton")
    print("3.- Salir del programa")
    opcion1 = input("Ingrese una opcion: ")
    if opcion1 == "1":
        res = 0
        while res != 5:
            print("---- Menu metodo jacobi ----")
            print("1.- Matriz 3x3")
            print("2.- Matriz 4x4")
            print("3.- Matriz 5x5")
            print("4.- Matriz 6x6")
            print("5.- Salir del programa")
            opcion = input("Ingrese una opcion: ")

            if opcion == "1":
                print("Programa para matrices 3x3")
                print("Ingreso de valores de la matriz T")
                print("Ingrese los valores de la primera fila")

                # datos de fila 1
                d1f1 = float(input("Dato x11: "))
                d2f1 = float(input("Dato x12: "))
                d3f1 = float(input("Dato x13: "))

                print("Ingrese los valores de la segunda fila")
                # datos de fila 2
                d1f2 = float(input("Dato x21: "))
                d2f2 = float(input("Dato x22: "))
                d3f2 = float(input("Dato x23: "))

                print("Ingrese los valores de la tercera fila")
                # datos de fila 3
                d1f3 = float(input("Dato x31: "))
                d2f3 = float(input("Dato x32: "))
                d3f3 = float(input("Dato x33: "))

                print("Ingreso de valores de la matriz C")
                d1mc = float(input("Dato x1: "))
                d2mc = float(input("Dato x2: "))
                d3mc = float(input("Dato x3: "))

                print("Ingrese el vector de valores iniciales ")
                d1x = float(input("Dato x1: "))
                d2x = float(input("Dato x2: "))
                d3x = float(input("Dato x3: "))

                erroraceptado = float(input("Ingrese el error aceptado: "))

                # definir matriz

                T = np.array(
                    [[d1f1, d2f1, d3f1], [d1f2, d2f2, d3f2], [d1f3, d2f3, d3f3]])
                c = np.array([d1mc, d2mc, d3mc])
                x = np.array([d1x, d2x, d3x])  # vector de valores iniciales

                error = 1
                while error > erroraceptado:
                    resultado = np.dot(T, x) + c
                    print(resultado)
                    numerador = np.amax(abs((resultado - x)))
                    denominador = np.amax(abs(resultado))
                    error = numerador / denominador
                    x = resultado

            elif opcion == "2":
                print("Programa para matrices 4x4")
                print("Ingreso de valores de la matriz T")
                print("Ingrese los valores de la primera fila")

                # datos de fila 1
                d1f1 = float(input("Dato x11: "))
                d2f1 = float(input("Dato x12: "))
                d3f1 = float(input("Dato x13: "))
                d4f1 = float(input("Dato x14: "))

                print("Ingrese los valores de la segunda fila")
                # datos de fila 2
                d1f2 = float(input("Dato x21: "))
                d2f2 = float(input("Dato x22: "))
                d3f2 = float(input("Dato x23: "))
                d4f2 = float(input("Dato x24: "))

                print("Ingrese los valores de la tercera fila")
                # datos de fila 3
                d1f3 = float(input("Dato x31: "))
                d2f3 = float(input("Dato x32: "))
                d3f3 = float(input("Dato x33: "))
                d4f3 = float(input("Dato x34: "))

                print("Ingrese los valores de la cuarta fila")
                # datos de fila 4
                d1f4 = float(input("Dato x41: "))
                d2f4 = float(input("Dato x42: "))
                d3f4 = float(input("Dato x43: "))
                d4f4 = float(input("Dato x44: "))

                print("Ingreso de valores de la matriz C")
                d1mc = float(input("Dato x1: "))
                d2mc = float(input("Dato x2: "))
                d3mc = float(input("Dato x3: "))
                d4mc = float(input("Dato x4: "))

                print("Ingrese el vector de valores iniciales ")
                d1x = float(input("Dato x1: "))
                d2x = float(input("Dato x2: "))
                d3x = float(input("Dato x3: "))
                d4x = float(input("Dato x4: "))

                erroraceptado = float(input("Ingrese el error aceptado: "))

                # definir matriz

                T = np.array(
                    [[d1f1, d2f1, d3f1, d4f1], [d1f2, d2f2, d3f2, d4f2], [d1f3, d2f3, d3f3, d4f3],
                     [d1f4, d2f4, d3f4, d4f4]])
                c = np.array([d1mc, d2mc, d3mc, d4mc])
                x = np.array([d1x, d2x, d3x, d4x])  # vector de valores iniciales

                error = 1
                while error > erroraceptado:
                    resultado = np.dot(T, x) + c
                    print(resultado)
                    numerador = np.amax(abs((resultado - x)))
                    denominador = np.amax(abs(resultado))
                    error = numerador / denominador
                    x = resultado

            elif opcion == "3":
                print("Programa para matrices 5x5")
                print("Ingreso de valores de la matriz T")
                print("Ingrese los valores de la primera fila")

                # datos de fila 1
                d1f1 = float(input("Dato x11: "))
                d2f1 = float(input("Dato x12: "))
                d3f1 = float(input("Dato x13: "))
                d4f1 = float(input("Dato x14: "))
                d5f1 = float(input("Dato x15: "))

                print("Ingrese los valores de la segunda fila")
                # datos de fila 2
                d1f2 = float(input("Dato x21: "))
                d2f2 = float(input("Dato x22: "))
                d3f2 = float(input("Dato x23: "))
                d4f2 = float(input("Dato x24: "))
                d5f2 = float(input("Dato x25: "))

                print("Ingrese los valores de la tercera fila")
                # datos de fila 3
                d1f3 = float(input("Dato x31: "))
                d2f3 = float(input("Dato x32: "))
                d3f3 = float(input("Dato x33: "))
                d4f3 = float(input("Dato x34: "))
                d5f3 = float(input("Dato x35: "))

                print("Ingrese los valores de la cuarta fila")
                # datos de fila 4
                d1f4 = float(input("Dato x41: "))
                d2f4 = float(input("Dato x42: "))
                d3f4 = float(input("Dato x43: "))
                d4f4 = float(input("Dato x44: "))
                d5f4 = float(input("Dato x45: "))

                print("Ingrese los valores de la quinta fila")
                # datos de fila 5
                d1f5 = float(input("Dato x51: "))
                d2f5 = float(input("Dato x52: "))
                d3f5 = float(input("Dato x53: "))
                d4f5 = float(input("Dato x54: "))
                d5f5 = float(input("Dato x55: "))

                print("Ingreso de valores de la matriz C")
                d1mc = float(input("Dato x1: "))
                d2mc = float(input("Dato x2: "))
                d3mc = float(input("Dato x3: "))
                d4mc = float(input("Dato x4: "))
                d5mc = float(input("Dato x5: "))

                print("Ingrese el vector de valores iniciales ")
                d1x = float(input("Dato x1: "))
                d2x = float(input("Dato x2: "))
                d3x = float(input("Dato x3: "))
                d4x = float(input("Dato x4: "))
                d5x = float(input("Dato x5: "))

                erroraceptado = float(input("Ingrese el error aceptado: "))

                # definir matriz

                T = np.array(
                    [[d1f1, d2f1, d3f1, d4f1, d5f1], [d1f2, d2f2, d3f2, d4f2, d5f2], [d1f3, d2f3, d3f3, d4f3, d5f3],
                     [d1f4, d2f4, d3f4, d4f4, d5f4], [d1f5, d2f5, d3f5, d4f5, d5f5]])
                c = np.array([d1mc, d2mc, d3mc, d4mc, d5mc])
                x = np.array([d1x, d2x, d3x, d4x, d5x])  # vector de valores iniciales

                error = 1
                while error > erroraceptado:
                    resultado = np.dot(T, x) + c
                    print(resultado)
                    numerador = np.amax(abs((resultado - x)))
                    denominador = np.amax(abs(resultado))
                    error = numerador / denominador
                    x = resultado

            elif opcion == "4":

                print("Programa para matrices 6x6")
                print("Ingreso de valores de la matriz T")
                print("Ingrese los valores de la primera fila")

                # datos de fila 1
                d1f1 = float(input("Dato x11: "))
                d2f1 = float(input("Dato x12: "))
                d3f1 = float(input("Dato x13: "))
                d4f1 = float(input("Dato x14: "))
                d5f1 = float(input("Dato x15: "))
                d6f1 = float(input("Dato x16: "))

                print("Ingrese los valores de la segunda fila")
                # datos de fila 2
                d1f2 = float(input("Dato x21: "))
                d2f2 = float(input("Dato x22: "))
                d3f2 = float(input("Dato x23: "))
                d4f2 = float(input("Dato x24: "))
                d5f2 = float(input("Dato x25: "))
                d6f2 = float(input("Dato x26: "))

                print("Ingrese los valores de la tercera fila")
                # datos de fila 3
                d1f3 = float(input("Dato x31: "))
                d2f3 = float(input("Dato x32: "))
                d3f3 = float(input("Dato x33: "))
                d4f3 = float(input("Dato x34: "))
                d5f3 = float(input("Dato x35: "))
                d6f3 = float(input("Dato x36: "))

                print("Ingrese los valores de la cuarta fila")
                # datos de fila 4
                d1f4 = float(input("Dato x41: "))
                d2f4 = float(input("Dato x42: "))
                d3f4 = float(input("Dato x43: "))
                d4f4 = float(input("Dato x44: "))
                d5f4 = float(input("Dato x45: "))
                d6f4 = float(input("Dato x46: "))

                print("Ingrese los valores de la quinta fila")
                # datos de fila 5
                d1f5 = float(input("Dato x51: "))
                d2f5 = float(input("Dato x52: "))
                d3f5 = float(input("Dato x53: "))
                d4f5 = float(input("Dato x54: "))
                d5f5 = float(input("Dato x55: "))
                d6f5 = float(input("Dato x56: "))

                print("Ingrese los valores de la sexta fila")
                # datos de fila 5
                d1f6 = float(input("Dato x61: "))
                d2f6 = float(input("Dato x62: "))
                d3f6 = float(input("Dato x63: "))
                d4f6 = float(input("Dato x64: "))
                d5f6 = float(input("Dato x65: "))
                d6f6 = float(input("Dato x66: "))

                print("Ingreso de valores de la matriz C")
                d1mc = float(input("Dato x1: "))
                d2mc = float(input("Dato x2: "))
                d3mc = float(input("Dato x3: "))
                d4mc = float(input("Dato x4: "))
                d5mc = float(input("Dato x5: "))
                d6mc = float(input("Dato x6: "))

                print("Ingrese el vector de valores iniciales ")
                d1x = float(input("Dato x1: "))
                d2x = float(input("Dato x2: "))
                d3x = float(input("Dato x3: "))
                d4x = float(input("Dato x4: "))
                d5x = float(input("Dato x5: "))
                d6x = float(input("Dato x6: "))

                erroraceptado = float(input("Ingrese el error aceptado: "))

                # definir matriz

                T = np.array(
                    [[d1f1, d2f1, d3f1, d4f1, d5f1, d6f1], [d1f2, d2f2, d3f2, d4f2, d5f2, d6f2],
                     [d1f3, d2f3, d3f3, d4f3, d5f3, d6f3],
                     [d1f4, d2f4, d3f4, d4f4, d5f4, d6f4], [d1f5, d2f5, d3f5, d4f5, d5f5, d6f5],
                     [d1f6, d2f6, d3f6, d4f6, d5f6, d6f6]])
                c = np.array([d1mc, d2mc, d3mc, d4mc, d5mc, d6mc])
                x = np.array([d1x, d2x, d3x, d4x, d5x, d6x])  # vector de valores iniciales

                error = 1
                while error > erroraceptado:
                    resultado = np.dot(T, x) + c
                    print(resultado)
                    numerador = np.amax(abs((resultado - x)))
                    denominador = np.amax(abs(resultado))
                    error = numerador / denominador
                    x = resultado

            elif opcion == "5":
                print("---Saliendo del programa---")
                res = 5
            else:
                print("Seleccione una opcion valida")

    elif opcion1 == "2":
        print("---- Menu metodo Newton ----")
        print("-----------------------------")
        print("sistema no lineal: ")
        print("x")
        print("4x21 -625x22 + 2x2 - 1 = 0")
        print("e^-x1x2 + 20x3 + 10pi - 3/3 = 0")
        print("-----------------------------")
        cota = float(input("Ingrese la cota: "))
        maxiteraciones = int(input('introduzca numero de iteraciones'))


        def jacobiano(x):
            J = np.array(
                [[3, x[2] * sin(x[1] * x[2]), x[1] * sin(x[1] * x[2])], [2 * x[0], -162 * (x[1] + 0.1), cos(x[2])],
                 [-x[1] * exp(-x[0] * x[1]), -x[0] * exp(-x[0] * x[1]), 20]])
            JInversa = np.linalg.inv(J)
            return JInversa


        def Fx(x):
            x1 = x[0] ** 2 + x[1] - 37
            x2 = x[0] - x[1] ** 2 - 5
            x3 = x[0] + x[1] + x[2] - 3
            xk = np.array([x1, x2, x3])
            return xk

        x = np.array([0, 0, 0])  # vector de valores iniciales
        error = 1
        c = 0
        while error > cota and c < maxiteraciones:
            c += 1
            r = jacobiano(x)
            feval = Fx(x)
            resultado = x - np.dot(r, feval)
            numerador = np.amax(abs((resultado - x)))
            denominador = np.amax(abs(resultado))
            error = numerador / denominador
            x = resultado

            print("Iteración:", c, " Resultado", resultado)




