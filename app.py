from tkinter import *
import parser

root=Tk() 
root.title("Calculadora")

display=Entry(root) #aqui estoy agregando el input de salida que mostrar los resultados de las operaciones matematicas
display.grid(row=1,columnspan=6,sticky=W+E) # EL STICKy es para decir que ocupe de este a oeste o sea todo el ancho, ademas el columnspan indica cuantas columnas ocupara

#Botones de los Numeros
Button(root,text='1',command=lambda:obtenerNumeros(1)).grid(row=2, column=0,sticky=W+E) # el metodo grid me permite darla la ubicacion a este boton que estoy creando, el row indica la fila donde sera ubicado y la colmun indica la columna en donde sera ubicado
Button(root,text='2',command=lambda:obtenerNumeros(2)).grid(row=2, column=1,sticky=W+E)
Button(root,text='3',command=lambda:obtenerNumeros(3)).grid(row=2, column=2,sticky=W+E)

Button(root,text='4',command=lambda:obtenerNumeros(4)).grid(row=3, column=0,sticky=W+E)
Button(root,text='5',command=lambda:obtenerNumeros(5)).grid(row=3, column=1,sticky=W+E)
Button(root,text='6',command=lambda:obtenerNumeros(6)).grid(row=3, column=2,sticky=W+E)

Button(root,text='7',command=lambda:obtenerNumeros(7)).grid(row=4, column=0,sticky=W+E)
Button(root,text='8',command=lambda:obtenerNumeros(8)).grid(row=4, column=1,sticky=W+E)
Button(root,text='9',command=lambda:obtenerNumeros(9)).grid(row=4, column=2,sticky=W+E)

Button(root,text='0',command=lambda:obtenerNumeros(0)).grid(row=5, column=1,sticky=W+E)


# Botones de Operadores
Button(root,text='C',command=lambda :limpiarCalculadora()).grid(row=2, column=5,sticky=W+E)
Button(root,text='%',command=lambda:obtnerOperacion("%")).grid(row=2, column=6,sticky=W+E)
Button(root,text='+',command=lambda:obtnerOperacion("+")).grid(row=3, column=5,sticky=W+E)
Button(root,text='-',command=lambda:obtnerOperacion("-")).grid(row=3, column=6,sticky=W+E)
Button(root,text='*',command=lambda:obtnerOperacion("*")).grid(row=4, column=5,sticky=W+E)
Button(root,text='/',command=lambda:obtnerOperacion("/")).grid(row=4, column=6,sticky=W+E)

#Botones de Acciones
Button(root,text='⟵',command=lambda :borrarElemento()).grid(row=5, column=5,columnspan=2,sticky=W+E)
Button(root,text='(',command=lambda:obtnerOperacion("(")).grid(row=6, column=6,sticky=W+E)
Button(root,text=')',command=lambda:obtnerOperacion(")")).grid(row=6, column=5,sticky=W+E)
Button(root,text='^2',command=lambda:obtnerOperacion("**2")).grid(row=7, column=6,sticky=W+E)
Button(root,text='exp',command=lambda:obtnerOperacion("**")).grid(row=7, column=5,sticky=W+E)
Button(root,text='=',command=lambda:calcular()).grid(row=8, column=5,columnspan=2,sticky=W+E)

#Funciones
i=0 #Obtener números para mostrar

def obtenerNumeros(n):
    global i
    display.insert(i, n) # aqui estoy insertando en el input el numero que quiero ingresar 
    i += 1
    
def obtnerOperacion(operador):
    global i
    longitudOperador = len(operador)
    display.insert(i, operador)
    i+=longitudOperador


def limpiarCalculadora():
    display.delete(0, END)


def borrarElemento():
    estadoActual = display.get()
    if len(estadoActual):
        nuevoEstado = estadoActual[:-1]
        limpiarCalculadora()
        display.insert(0, nuevoEstado)
    else:
        limpiarCalculadora()
        display.insert(0, 'Error')


def calcular():
    estadoActual=display.get()
    try:
        expresionMatematica = parser.expr(estadoActual).compile()
        resultado = eval(expresionMatematica)
        limpiarCalculadora()
        display.insert(0, resultado)
    except Exception:
        limpiarCalculadora()
        display.insert(0, 'Error')
    


    


root.mainloop() # Con este metododo mainloop para puedo ejecutar la apliacion ejecutando este archivo python