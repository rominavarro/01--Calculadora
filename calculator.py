#Importacion de la libreria TKinder para la GUI de Python

from tkinter import *
from tkinter import ttk
import math

#funcion para tema oscuro de la calculadora
def TemaOscuro(*args):
    estilos.configure('mainframe.TFrame', background="#010924")

    estilos_label1.configure('Label1.TLabel', background="#010924", foreground="white")
    estilos_label2.configure('Label2.TLabel', background="#010924", foreground="white")

    estilo_boton_num.configure('Botones_numeros.TButton', background="#00044A", foreground="white")
    estilo_boton_num.map('Botones_numeros.TButton', background=[('active', '#000AB1')])

    estilo_boton_borrar.configure('Botones_borrar.TButton', background="#010924", foreground="white")
    estilo_boton_borrar.map('Botones_borrar.TButton', background=[('active', '#000AB1')])

    estilo_botones_restantes.configure('Botones_restantes.TButton', background="#010924", foreground="white")
    estilo_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#000AB1')])


#funcion para tema claro de la calculadora
def TemaClaro(*args):
    estilos.configure('mainframe.TFrame', background="#DBDBDB", foreground="black")

    estilos_label1.configure('Label1.TLabel', background="#DBDBDB", foreground="black")
    estilos_label2.configure('Label2.TLabel', background="#DBDBDB", foreground="black")

    estilo_boton_num.configure('Botones_numeros.TButton', background="#FFFFFF", foreground="black")
    estilo_boton_num.map('Botones_numeros.TButton', background=[('active', '#B9B9B9')])
    
    estilo_boton_borrar.configure('Botones_borrar.TButton', background="#CECECE", foreground="black")
    estilo_boton_borrar.map('Botones_borrar.TButton', background=[('active', '#858585')])
    
    estilo_botones_restantes.configure('Botones_restantes.TButton', background="#CECECE", foreground="black")
    estilo_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#858585')])

#funcion para ingresar valores
def ingresarValores(tecla):
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)
    
    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == "-":
            entrada1.set(entrada2.get() + '-')
        
        entrada2.set('')
    
    if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

#funcion para ingresar los valores desde el teclado
def ingresarValoresTeclado(event):
     tecla = event.char
     print(event)

     if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada2.set(entrada2.get() + tecla)
    
     if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
        if tecla == '*':
            entrada1.set(entrada2.get() + '*')
        elif tecla == '/':
            entrada1.set(entrada2.get() + '/')
        elif tecla == '+':
            entrada1.set(entrada2.get() + '+')
        elif tecla == "-":
            entrada1.set(entrada2.get() + '-')
        
        entrada2.set('')
    
     if tecla == '=':
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

#funcion para calcular la raiz cuadrada de un numero
def raiz():
    entrada1.set('')
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)

#funcion para borrar 
def borrar(*args):
    inicio = 0
    final = len(entrada2.get())

    entrada2.set(entrada2.get()[inicio:final-1])

#funcion para eliminar todas las operaciones
def borrarTodo(*args):
    entrada1.set('')
    entrada2.set('')

#establecer el root de la calculadora
root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

estilos = ttk.Style()
estilos.configure('mainframe.TFrame', background="#DBDBDB")
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")

#diseño del mainframe
mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))

#diseño responsive del mainframe
#diseño de las columnas
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

#diseño de las filas
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

#estilos de los labels
estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel', font="arial 15", anchor="E")

estilos_label2 = ttk.Style()
estilos_label2.configure('Label2.TLabel', font="arial 40", anchor="E")

#estilos para los botones
estilo_boton_num = ttk.Style()
estilo_boton_num.configure('Botones_numeros.TButton', font="arial 22", width=5, background="#FFFFFF", relief="flat")
estilo_boton_num.map('Botones_numeros.TButton', background=[('active', '#B9B9B9')])


estilo_boton_borrar = ttk.Style()
estilo_boton_borrar.configure('Botones_borrar.TButton', font="arial 22", width=5, background="#CECECE", relief="flat")
estilo_boton_borrar.map('Botones_borrar.TButton', foreground=[('active', '#FF0000')], background=[('active', '#858585')])

estilo_botones_restantes = ttk.Style()
estilo_botones_restantes.configure('Botones_restantes.TButton', font="arial 22", width=5, background="#CECECE", relief="flat")
estilo_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#858585')])

#entradas de la calculadora
entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))

#creacion de botones
#botones numericos
button0 = ttk.Button(mainframe, text="0", style="Botones_numeros.TButton", command=lambda: ingresarValores('0'))
button1 = ttk.Button(mainframe, text="1", style="Botones_numeros.TButton", command=lambda: ingresarValores('1'))
button2 = ttk.Button(mainframe, text="2", style="Botones_numeros.TButton", command=lambda: ingresarValores('2'))
button3 = ttk.Button(mainframe, text="3", style="Botones_numeros.TButton", command=lambda: ingresarValores('3'))
button4 = ttk.Button(mainframe, text="4", style="Botones_numeros.TButton", command=lambda: ingresarValores('4'))
button5 = ttk.Button(mainframe, text="5", style="Botones_numeros.TButton", command=lambda: ingresarValores('5'))
button6 = ttk.Button(mainframe, text="6", style="Botones_numeros.TButton", command=lambda: ingresarValores('6'))
button7 = ttk.Button(mainframe, text="7", style="Botones_numeros.TButton", command=lambda: ingresarValores('7'))
button8 = ttk.Button(mainframe, text="8", style="Botones_numeros.TButton", command=lambda: ingresarValores('8'))
button9 = ttk.Button(mainframe, text="9", style="Botones_numeros.TButton", command=lambda: ingresarValores('9'))

#botones de funcionalidad
button_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton", command=lambda: borrar())
button_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton", command=lambda: borrarTodo())
button_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_restantes.TButton", command=lambda: ingresarValores('('))
button_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_restantes.TButton", command=lambda: ingresarValores(')'))
button_punto = ttk.Button(mainframe, text=".", style="Botones_restantes.TButton", command=lambda: ingresarValores('.'))

#botones de operaciones
button_division = ttk.Button(mainframe, text=chr(247), style="Botones_restantes.TButton", command=lambda: ingresarValores('/'))
button_multiplicacion = ttk.Button(mainframe, text="x", style="Botones_restantes.TButton", command=lambda: ingresarValores('*'))
button_resta = ttk.Button(mainframe, text="-", style="Botones_restantes.TButton", command=lambda: ingresarValores('-'))
button_suma = ttk.Button(mainframe, text="+", style="Botones_restantes.TButton", command=lambda: ingresarValores('+'))
button_igual = ttk.Button(mainframe, text="=", style="Botones_restantes.TButton", command=lambda: ingresarValores('='))
button_raiz = ttk.Button(mainframe, text="√", style="Botones_restantes.TButton", command=lambda: raiz())

#Colocar botones en pantalla
button_parentesis1.grid(column=0, row=2, sticky=(W, N, E, S))
button_parentesis2.grid(column=1, row=2, sticky=(W, N, E, S))
button_borrar_todo.grid(column=2, row=2, sticky=(W, N, E, S))
button_borrar.grid(column=3, row=2, sticky=(W, N, E, S))

button7.grid(column=0, row=3, sticky=(W, N, E, S))
button8.grid(column=1, row=3, sticky=(W, N, E, S))
button9.grid(column=2, row=3, sticky=(W, N, E, S))
button_division.grid(column=3, row=3, sticky=(W, N, E, S))

button4.grid(column=0, row=4, sticky=(W, N, E, S))
button5.grid(column=1, row=4, sticky=(W, N, E, S))
button6.grid(column=2, row=4, sticky=(W, N, E, S))
button_multiplicacion.grid(column=3, row=4, sticky=(W, N, E, S))

button1.grid(column=0, row=5, sticky=(W, N, E, S))
button2.grid(column=1, row=5, sticky=(W, N, E, S))
button3.grid(column=2, row=5, sticky=(W, N, E, S))
button_suma.grid(column=3, row=5, sticky=(W, N, E, S))

button0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
button_punto.grid(column=2, row=6, sticky=(W, N, E, S))
button_resta.grid(column=3, row=6, sticky=(W, N, E, S))

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S))
button_raiz.grid(column=3, row=7, sticky=(W, N, E, S))

#Configurar el espaciado interno de los botones
for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

#Configurar cambio entre los temas
root.bind('<KeyPress-o>', TemaOscuro)
root.bind('<KeyPress-c>', TemaClaro)
root.bind('<Key>', ingresarValoresTeclado)
root.bind('<KeyPress-b>', borrar)
root.bind('<KeyPress-q>', borrarTodo)

root.mainloop()