from persona import Persona
from medico import Medico
from policlinica import Policlinica
from socio import Socio
from especialidad import Especialidad
from consulta import Consulta
import datetime as dt



def menu():
    print ("Seleccione una opcion del menu:")
    print ("1. Dar de alta una especialidad")
    print ("2. Dar de alta un socio")
    print ("3. Dar de alta un medico")
    print ("4. Dar de alta una consulta medica")
    print ("5. Emitir un ticket de consulta")
    print ("6. Realizar consultas")
    print ("7. Salir del programa")

if __name__ == "__main__":
    policlinica = Policlinica()
    pregunta = True
    menu()

    while pregunta == True:
        
        opcion = int(input("que opcion quiere?"))

        if opcion == 7:
            pregunta = False
            
    
        if opcion == 1: ## dar de alta una especialidad
            policlinica.dar_alta_especialidad()
            en_pregunta = True
            nombre_correcto = False
            print("")
            menu()



        en_pregunta_2 = True

        if opcion == 2:    
            policlinica.dar_alta_socio()
            en_pregunta_2 = True
            nombre_pers_correcto = False
            apellido_pers_correcto = False
            cedula_correcta = False
            celular_correcto= False
            tipo_correcto= False
            nacimiento_correcto=False
            ingreso_correcto = False
            print("")
            menu()

        

        if opcion == 3:
            policlinica.dar_alta_medico()
            en_pregunta_2 = True
            nombre_pers_correcto = False
            apellido_pers_correcto = False
            cedula_correcta = False
            celular_correcto= False
            nacimiento_correcto=False
            ingreso_correcto = False
            print("")
            menu()


        if opcion == 4:
            policlinica.dar_alta_consulta()
            en_pregunta_2 = True
            nombre_pers_correcto = False
            apellido_pers_correcto = False
            cedula_correcta = False
            celular_correcto= False
            nacimiento_correcto=False
            ingreso_correcto = False
            print("")
            menu()

        if opcion == 5:
            policlinica.emitir_ticket()
            print("")
            menu()


        if opcion == 6:
            policlinica.realizar_consulta()
            print("")
            menu()