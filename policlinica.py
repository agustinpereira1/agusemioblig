from especialidad import Especialidad
from socio import Socio
from medico import Medico
from datetime import datetime
import re
from consulta import Consulta


class Policlinica:              
    def __init__(self):
        self.__lista_especialidad = []
        self.__lista_socio = []
        self.__lista_medico= []
        self.__lista_consulta_medica = []

    @property 
    def lista_especialidad (self):
        return self.__lista_especialidad
    @property
    def lista_socio (self):
        return self.__lista_socio
    @property
    def lista_medico (self):
        return self.__lista_medico
    @property
    def lista_consulta_medica (self):
        return self.__lista_consulta_medica


    def dar_alta_especialidad(self):
        nombre_correcto = False ##verificar el nombre de la especialidad
        precio_correcto=False
        especialidad_nombre = (input("Ingrese el nombre de la especialidad: "))
        while nombre_correcto == False:
            if self.verificar_texto(especialidad_nombre) == True:
                nombre_correcto = True
            else:
                especialidad_nombre = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente: ")
                nombre_correcto = self.verificar_texto(especialidad_nombre) 
                
        while precio_correcto == False:
            try:
                precio = (int (input ("Ingrese el precio asociado:")))
            except ValueError:
                print("El precio asociado tiene que ser un numero, ingreselo nuevamente")
                precio_correcto=False
            else:
                especialidad = Especialidad(especialidad_nombre, precio)
                self.__lista_especialidad.append(especialidad)
                print ("La especialidad se ha creado con exito")
                precio_correcto=True
                en_pregunta=False

        for especialidad in self.__lista_especialidad:
            print (f"Nombre: {especialidad.especialidad_nombre} Precio: ${especialidad.precio}")
        return especialidad_nombre, precio
   
    def dar_alta_persona(self):
        en_pregunta_2 = True
        nombre_pers_correcto = False
        apellido_pers_correcto = False
        cedula_correcta = False
        celular_correcto= False
        nacimiento_correcto=False
        ingreso_correcto = False
        
        while en_pregunta_2==True:
                nombre = input("Ingrese el nombre: ") #error de espacios y tildes
                while nombre_pers_correcto == False:
                     
                    if self.verificar_texto(nombre) == True:
                        nombre_pers_correcto = True
                    else:
                        nombre = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente: ")
                        nombre_pers_correcto = self.verificar_texto(nombre) 
                        
                apellido = input("Ingrese el apellido: ") #error de espacios y tildes
                while apellido_pers_correcto == False:

                    if self.verificar_texto(apellido) == True:
                        apellido_pers_correcto = True
                    else:
                        apellido = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente: ")
                        apellido_pers_correcto = self.verificar_texto(apellido)

                while cedula_correcta == False:
                    try:
                        ci = int(input("Ingrese la cedula de identidad:"))
                    except ValueError:
                        ci = input ("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos")
                    else:
                        longitud_cedula= len(str(ci)) 
                        if (longitud_cedula!=8) == True:
                            print ("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos")
                        else: cedula_correcta =True
                from datetime import datetime        
                nacimiento = input("Ingrese su fecha de nacimiento en la forma aaaa-mm-dd")
                formato = "%Y-%m-%d"
                # nacimiento1 = str(nacimiento)
                while nacimiento_correcto == False:
                    try:
                        nacimiento_convert = datetime.strptime(nacimiento, formato)
                    except ValueError:
                        nacimiento= input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd")
                    else:nacimiento_correcto=True

                
                ingreso = input("Ingrese la fecha de ingreso a la institucion en la forma aaaa-mm-dd")
               
                while ingreso_correcto == False:
                    try:
                        ingreso_convert = datetime.strptime(ingreso,formato)
                    except ValueError:
                        ingreso = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd")
                    else: ingreso_correcto = True

                        
                while celular_correcto == False:
                    try:
                        celular= int(input("Ingrese su número de celular: "))
                    except ValueError:
                        print ("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
                    else:
                        longitud_celular = len(str(celular))
                        if (longitud_celular!= 8) == True:
                            print ("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
                        else: 
                            celular_correcto = True

                return nombre, apellido, ci, nacimiento, ingreso, celular

    def dar_alta_socio(self):
        nombre,apellido,ci, nacimiento, ingreso, celular=self.dar_alta_persona()
        tipo_correcto= False
        deuda = 0
        while tipo_correcto ==False:
                    try: 
                        tipo = int(input("Ingrese el tipo de socio: 1-Bonificado 2-No Bonificado"))
                    except ValueError:
                        print ("El valor ingresado no es correcto, elige la opción 1 o 2")
                    else:
                        if (tipo == 1 or tipo==2) == True:
                            tipo_correcto = True
                            socio = Socio(nombre, apellido, ci, nacimiento, ingreso, celular,tipo,deuda)
                            self.__lista_socio.append(socio)
                        else:
                            print ("El valor ingresado no es correcto, elige la opción 1 o 2")

        for socio in self.__lista_socio:
            print (f" \n Nombre:{socio.nombre} \n Apellido:{socio.apellido} \n Cedula de identidad:{socio.ci} \n Nacimiento: {socio.nacimiento} \n Ingreso: {socio.ingreso} \n Celular: {socio.celular} \n Tipo: {socio.tipo}")
    
        return ci
    
    def dar_alta_medico (self):
        
        nombre,apellido,ci, nacimiento, ingreso, celular=self.dar_alta_persona()
        especialidad_nombre2 = (input("Ingrese el nombre de la especialidad: ")) 
        nombre_esp_correcto = False

        while nombre_esp_correcto == False:
                if self.verificar_texto(especialidad_nombre2) == True:
                    nombre_esp_correcto = True
                else:
                    especialidad_nombre2 = input("La especialidad debe ser un string")
                    nombre_esp_correcto = self.verificar_texto(especialidad_nombre2)

        encontrado = False
        for especialidad in self.__lista_especialidad:
            if especialidad.especialidad_nombre == especialidad_nombre2:
                    medico = Medico(nombre, apellido, ci, nacimiento, ingreso, celular, especialidad_nombre2) 
                    self.__lista_medico.append(medico)
                    encontrado = True
        if(encontrado == False):
            print("Esta especialidad no esta dada de alta, elija una opcion: ")
            opcion_elegida= input("1- Volver a ingresar la especialidad. 2- Dar de alta esta especialidad")
        
            nombre_esp_correcto=False
            while opcion_elegida == "1":
                while nombre_esp_correcto == False:
                    if self.verificar_texto(especialidad_nombre2) == True:
                        nombre_esp_correcto = True
                    else:
                        especialidad_nombre2 = input("La especialidad debe ser un string")
                        nombre_esp_correcto = self.verificar_texto(especialidad_nombre2)

                encontrado = False
                for especialidad in self.__lista_especialidad:
                    if especialidad.especialidad_nombre == especialidad_nombre2:
                        medico = Medico(nombre, apellido, ci, nacimiento, ingreso, celular, especialidad_nombre2)
                        self.__lista_medico.append (medico)
                        encontrado = True
                        opcion_elegida="valor secreto"
                if(encontrado == False):
                    print("Esta especialidad no esta dada de alta, elija una opcion")
                    opcion_elegida= input("1- Volver a ingresar la especialidad. 2- Dar de alta esta especialidad")

            if opcion_elegida == "2":
                especialidad_nombre, precio = self.dar_alta_especialidad()

                medico = Medico(nombre, apellido, ci, nacimiento, ingreso, celular, especialidad_nombre)
                self.__lista_medico.append(medico)
                for medico in self.__lista_medico:
                    print (nombre,apellido,ci,nacimiento,ingreso,celular, especialidad_nombre)
                
        for medico in self.__lista_medico:
            print (f"\n Nombre:{medico.nombre} \n Apellido:{medico.apellido} \n Cedula de identidad:{medico.ci} \n Nacimiento: {medico.nacimiento} \n Ingreso: {medico.ingreso} \n Celular: {medico.celular} \n Especialidad: {medico.especialidad_nombre2} \n")


    def ingresar_especialidad (self):
        nombre_esp_correcto3 = False
        especialidad_nombre3 = (input("Ingrese el nombre de la especialidad: "))
        while nombre_esp_correcto3 == False:
            if self.verificar_texto(especialidad_nombre3) == True:
                nombre_esp_correcto3 = True
            else:
                especialidad_nombre3 = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente: ")
                nombre_esp_correcto3 = self.verificar_texto(especialidad_nombre3)

        encontrado = False
        for especialidad in self.__lista_especialidad:
            if especialidad.especialidad_nombre == especialidad_nombre3:
                    encontrado = True
        if(encontrado == False):
            print("Esta especialidad no esta dada de alta, elija una opcion: ")
            opcion_elegida= input("1- Volver a ingresar la especialidad. 2- Dar de alta esta especialidad")
        

            while opcion_elegida == "1":
                especialidad_nombre3 = (input("Ingrese el nombre de la especialidad: "))
                while nombre_esp_correcto3 == False:
                    if self.verificar_texto(especialidad_nombre3) == True:
                        nombre_esp_correcto3 = True
                    else:
                        especialidad_nombre3 = input("El nombre de la especialidad es incorrecto, ingréselo nuevamente: ")
                        nombre_esp_correcto3 = self.verificar_texto(especialidad_nombre3)
                encontrado = False
                for especialidad in self.__lista_especialidad:
                    if especialidad.especialidad_nombre == especialidad_nombre3:
                        encontrado = True
                        opcion_elegida="valor secreto"
                if(encontrado == False):
                    print("Esta especialidad no esta dada de alta, elija una opcion")
                    opcion_elegida= input("1- Volver a ingresar la especialidad. 2- Dar de alta esta especialidad")

            if opcion_elegida == "2":
                especialidad_nombre, precio = self.dar_alta_especialidad()

            for especialidad in self.__lista_especialidad:
                print (especialidad.especialidad_nombre,especialidad.precio)

        return especialidad_nombre3

        
    def dar_alta_consulta (self): 
        
        #hay que verificar que cuando me ponga una especialidad solo me deje ingresar los medicos que estan 
        #aosciados a dicha especialidad y que cuando ponga el medico solo me deje con la especialidad que tiene vinculada
        especialidad_nombre3 = self.ingresar_especialidad()
        corresponde_medico=False
        nombre_apellido_medico = input("Ingrese el nombre del medico") #nos pasan marta pino pero nosotros tenemos a marta - pino en dos variables diferentes
        try:
            nombre1, apellido1 = nombre_apellido_medico.split()
        except:
            nombre_apellido_medico
            corresponde_medico = False
        while corresponde_medico==False:
            for medico in self.__lista_medico:
                if nombre1== medico.nombre and apellido1==medico.apellido and especialidad_nombre3==medico.especialidad_nombre2:
                    encontrado = False
                    
                    for medico in self.__lista_medico:
                        if medico.nombre == nombre1 and medico.apellido== apellido1:
                            encontrado = True
                    if (encontrado ==False):
                        print ("Este medico no esta dado de alta, elija una opcion:")
                        opcion_elegida2= input ("1- Volver a ingresar el medico. 2- Dar de alta el medico")

                        while opcion_elegida2 =="1":
                            nombre_apellido_medico =input("Ingrese el nombre del medico")
                            encontrado = False
                            nombre, apellido = nombre_apellido_medico.split()
                            for medico in self.__lista_medico:
                                if medico.nombre == nombre and medico.apellido== apellido:
                                    encontrado = True
                                    opcion_elegida2="valor secreto"
                            if (encontrado ==False):
                                print ("Este medico no esta dado de alta, elija una opcion:")
                                opcion_elegida2= input ("1- Volver a ingresar el medico. 2- Dar de alta el medico")

                        if opcion_elegida2== "2":
                            self.dar_alta_medico()
                        
                        for medico in self.__lista_medico:
                            print ("Agende la especialidad y el nombre del medico", medico.nombre,medico.apellido)
                            print("llegue hasta aca")

                    fecha_consulta_correcta = False
                    fecha_consulta = input("Ingrese la fecha de consulta en la forma aaaa-mm-dd")
                    while fecha_consulta_correcta == False:
                        try:
                            fecha_convert = datetime.strptime(fecha_consulta,"%Y-%m-%d")
                            fecha_consulta_correcta = True
                        except ValueError:
                            fecha_consulta = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd")
                        else: 
                            fecha_consulta_correcta = True


                    pacientes_correctos = False
                    while pacientes_correctos == False:
                        try:
                            numero_pacientes=int(input("Ingrese la cantidad de pacientes que se atenderán: "))
                            pacientes_correctos = True
                        except ValueError:
                            numero_pacientes=int(input("Debe ser un numero"))
                        else: pacientes_correctos=True

                    consulta_registrada = Consulta(especialidad_nombre3,nombre_apellido_medico,fecha_consulta,numero_pacientes)
                    self.__lista_consulta_medica.append(consulta_registrada)

                    for consulta_registrada in self.__lista_consulta_medica:
                        print (consulta_registrada.especialidad_nombre3, consulta_registrada.nombre_apellido_medico, consulta_registrada.fecha_consulta, consulta_registrada.numero_pacientes)
                    corresponde_medico=True
                    break
                    
                else:
                    nombre_apellido_medico = input("Ingrese el nombre del medico") #nos pasan marta pino pero nosotros tenemos a marta - pino en dos variables diferentes
                    nombre1, apellido1 = nombre_apellido_medico.split()
                    corresponde_medico= False


    def emitir_ticket (self):
        especialidad_nombre3= self.ingresar_especialidad()
        
        contador = 1
        lista_medicos_especialidad=[]
        

        for consulta_registrada in self.__lista_consulta_medica:
            if consulta_registrada.especialidad_nombre3 == especialidad_nombre3:
                print (f"\n{contador} Doctor: {consulta_registrada.nombre_apellido_medico} Dia de la consulta: {consulta_registrada.fecha_consulta}")
                lista_medicos_especialidad.append(consulta_registrada.nombre_apellido_medico)   
                contador += 1 

        opcion = int(input("Seleccione la opcion deseada: ")) #eligiendo 1 o 2  dependiendo de que medico queres ver las horas disponibles

        opcion_correcta = False
        while opcion_correcta == False:
            if 1 <= opcion <= contador:
                try:
                    nombre_medico_queremos = lista_medicos_especialidad[opcion-1]
                except:
                    opcion= int(input ("Seleccione una opcion valida:"))
                    opcion_correcta=False
                else:
                    for consulta_registrada in self.__lista_consulta_medica:
                        if nombre_medico_queremos == consulta_registrada.nombre_apellido_medico:
                            print ("Los numeros que quedan disp para esta consulta son:") 
                    opcion_correcta = True
                
            else:
                opcion = int(input("Valor ingresado no es correcto, ingreselo nuevamente: "))
                opcion_correcta=False

        max = 0
        for consulta_registrada in self.__lista_consulta_medica:
            if nombre_medico_queremos == consulta_registrada.nombre_apellido_medico:
                for i in range(len(consulta_registrada.numero_pacientes)): 
                    if consulta_registrada.numero_pacientes[i]>max:
                        max = consulta_registrada.numero_pacientes[i]

        for consulta_registrada in self.__lista_consulta_medica:
            if nombre_medico_queremos == consulta_registrada.nombre_apellido_medico: #copie y pegue lo de arriba
                for i in range(len(consulta_registrada.numero_pacientes)):
                    if consulta_registrada.numero_pacientes[i]!="ocupado":
                        print(consulta_registrada.numero_pacientes[i])
                
        opcion2 = int(input("Seleccione el numero de atencion deseado: "))

        opcion2_correcta = False
        while opcion2_correcta==False:
            for consulta_registrada in self.__lista_consulta_medica:
                if nombre_medico_queremos == consulta_registrada.nombre_apellido_medico: #copie y pegue lo de arriba
                    print("Las consultas dispo son las siguientes")
                    if 1 <= opcion2 <= max and consulta_registrada.numero_pacientes[opcion2]!= "ocupado":
            
                        consulta_registrada.numero_pacientes[opcion2-1]= "ocupado" ##
                        valor_ocupado = opcion2-1
                        opcion2_correcta = True
                    else:
                        print("Las consultas disponibles son las siguientes:")
                        for i in range(len(consulta_registrada.numero_pacientes)):
                            if consulta_registrada.numero_pacientes[i]!="ocupado" and consulta_registrada.numero_pacientes[i]!= "ocupado boni":
                                print(consulta_registrada.numero_pacientes[i])
                        opcion = int(input("Valor ingresado no es correcto o ya esta ocupado, ingreselo nuevamente: "))


        cedula_correcta=False
        while cedula_correcta == False:
            try:
                ci = int(input("Ingrese la cedula de identidad:"))
            except ValueError:
                ci = input ("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos")
            else:
                longitud_cedula= len(str(ci)) 
                if (longitud_cedula!=8) == True:
                    print ("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos")
                else: cedula_correcta =True


        encontrado = False
        for socio in self.__lista_socio:
            if socio.ci == ci:
                    encontrado = True
        if(encontrado == False):
            print("Este socio no esta dado de no esta dad  de alta, elija una opcion: ")
            opcion_elegida= input("1- Volver a ingresar el socio. 2- Dar de alta este socio")

           
            while opcion_elegida == "1":
                ci= (input("Ingrese la cedula: "))
                while cedula_correcta == False:
                    try:
                        ci = int(input("Ingrese la cedula de identidad:"))
                    except ValueError:
                        ci = input ("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos")
                    else:
                        longitud_cedula= len(str(ci)) 
                    if (longitud_cedula!=8) == True:
                        print ("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos")
                    else: cedula_correcta =True

                encontrado = False
                for socio in self.__lista_socio:
                    if socio.ci == ci:
                        encontrado = True
                        opcion_elegida="valor secreto"
                if(encontrado == False):
                    print("Este socio no esta dado de alta, elija una opcion")
                    opcion_elegida= input("1- Volver a ingresar el socio. 2- Dar de alta al socio")

            if opcion_elegida == "2":
                ci = self.dar_alta_socio()
    # INTENTANDO HACER LA 6.5 (ULTIMA PREGUNTA DEL OBLIGATIORIO)       
            # bonificado = False
            # for socio in self.__lista_socio:
            #     if ci == socio.ci:
            #         if socio.tipo == 1: ## 1 es bonificado
            #             if consulta_registrada.
            #             consulta_registrada.numero_pacientes[valor_ocupado]= "ocupado" ##


            for socio in self.__lista_socio:
                print (socio.nombre,socio.ci)


        for especialidad in self.__lista_especialidad:
            if especialidad_nombre3==especialidad.especialidad_nombre:
                precio_aso= especialidad.precio

        for socio in self.__lista_socio:
            if socio.ci == ci:
                if socio.tipo == 1:
                    socio.deuda += self.descuento_boni(precio_aso)
                else:
                    socio.deuda += precio_aso
                    

        
    def realizar_consulta(self):
        try:
            opcion_elegida=int(input("Seleccione una opcion:"))
        except ValueError:
            opcion_elegida=int(input("Debe ser un numero:"))
        else:
            if opcion_elegida==1:
                especialidad_que_quiere= self.ingresar_especialidad()
                for medico in self.__lista_medico:
                    if medico.especialidad_nombre2 == especialidad_que_quiere:
                        print (f"Nombre: {medico.nombre} Apellido: {medico.apellido} \n")
            elif opcion_elegida==2:
                especialidad_que_quiere_precio = self.ingresar_especialidad()
                for especialidad in self.__lista_especialidad:
                    if especialidad.especialidad_nombre == especialidad_que_quiere_precio:
                        print (f"El precio de la consulta de {especialidad_que_quiere_precio} es {especialidad.precio} ")
            elif opcion_elegida==3:
                lista_socios_ordenada = sorted(self.__lista_socio, key=lambda socio: socio.deuda)
                for i in lista_socios_ordenada:
                    print (f"\n El socio con ci {i.ci} tiene una deuda de: {i.deuda}")
            elif opcion_elegida==4:
                
                fecha_inicial1 = input("Ingrese la fecha inicial en la forma aaaa-mm-dd") ##verificando primer fecha
                self.verificar_fecha(fecha_inicial1)
                fecha_final1=input("Ingrese la fecha limite donde verificar las consultas en la forma aaaa-mm-dd")
                self.verificar_fecha(fecha_final1)
                lista_fechas_ordenada = sorted(self.__lista_consulta_medica, key=lambda consulta_registrada: consulta_registrada.fecha_consulta)
                for i in lista_fechas_ordenada:
                    if(i.fecha_consulta >= fecha_inicial1 and i.fecha_consulta <= fecha_final1):
                        print(f" \nEspecialidad: {i.especialidad_nombre3} Medico: {i.nombre_apellido_medico} Fecha:{i.fecha_consulta}")
            elif opcion_elegida == 5:
                fecha_inicial2 = input("Ingrese la fecha inicial en la forma aaaa-mm-dd")
                self.verificar_fecha(fecha_inicial2)
                fecha_final2=input("Ingrese la fecha limite donde verificar las consultas en la forma aaaa-mm-dd")
                self.verificar_fecha(fecha_final2)
                lista_fechas_ordenada2 = sorted(self.__lista_consulta_medica, key=lambda consulta_registrada: consulta_registrada.fecha_consulta)
                for consulta in lista_fechas_ordenada2:
                    if(consulta.fecha_consulta >= fecha_inicial2 and consulta.fecha_consulta <= fecha_final2):
                        nombre_especialidad = consulta.especialidad_nombre3







                        print(f" \nEspecialidad: {i.especialidad_nombre3} Medico: {i.nombre_apellido_medico} Fecha:{i.fecha_consulta}")
                


                    


                    
                    
                


    def verificar_texto(self, palabra):
        frase = r'[^a-zA-Z\sáéíóúÁÉÍÓÚüÜñÑ]'
        coincidencias = re.search(frase, palabra)
        return coincidencias is None

            
    def descuento_boni (self,precio):
        precio_con_descuento = precio *0.80
        return precio_con_descuento
            
    def verificar_fecha(self, fecha):
        inicio_correcto = False
        while inicio_correcto == False:
            try:
                fecha_convert = datetime.strptime(fecha,"%Y-%m-%d")
                inicio_correcto = True
            except ValueError:
                fecha = input("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd")
            else: 
                inicio_correcto = True