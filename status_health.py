#status_health
#1) Saber espacio libre en el /var 
#2) saber memoria free.
#3) Total de procesos corriendo
#4) Cantidad de CPU
#5) Load Average mas inmediato.

import subprocess, os
#funcion que utilizare para obterner el memory space, y la cant de cpu, que me devuelve como resultados una lista
def get_data(com1, com2):
    data_temp = subprocess.run([com1,com2], capture_output=True, encoding='utf-8')
    data = data_temp.stdout.split()
    #print(data)
    return data

#funcion para correr comandos simples (sin flags)que devuelven una lista. 
def single_command(com1):
    command_result = subprocess.run([com1], capture_output=True, encoding='utf-8')
    command = command_result.stdout.split()
    return  command  
    
#funcion que utilizare para saber el espacio en un filesistem determinado *paso tres parametros.  me devuelve una lista
def get_space(com1, com2, com3):
    space_temp = subprocess.run([com1,com2,com3], capture_output=True, encoding='utf-8')
    space = space_temp.stdout.split()
    return space

# funcion que me cuenta la cant de procesos corriendo. Me lo devuelve tipo int.
def get_num_proc(com1,com2):
    cant_proc = subprocess.run([com1,com2], capture_output=True, encoding='utf-8') #no se como poner el | wc -l splitline es una opcion para saber el numero de lineas.
    procesos_temp = len(cant_proc.stdout.splitlines())
    return procesos_temp

#defino variables de entorno
os.environ['MONIT_MEM_LIMIT']='10'
os.environ['MONIT_DISK_SPACE']='80'
#Calculo la memoria
memory=get_data(com1="free",com2="-t")
#calculo de CPU
cpu=get_data(com1="getconf",com2="_NPROCESSORS_ONLN")
#Nombre de host
host=single_command(com1="hostname")
#Uptime
load_avg=single_command(com1="uptime")
#Calculo del /var
space=get_space(com1="df",com2="-h",com3="/var")
procesos=get_num_proc(com1="ps",com2="-ef")

print("Nombre de Host:", host[0])
print("Memoria Disponible en el Sistema =", memory[9]) 
#print(type(memory[9]))
print("CPUs =", cpu[0]) ##--> pero ese es un string! Debere pasarlo a int?
print("Load Average: ", load_avg[8])
print("Estado /var: Usado :", space[9], "Disponible: ", space[10])
print("Procesos corriendo actualimente:", procesos)

#Calculo el % de Memoria utilizado.
memory =int(int(memory[8]) *100 / int(memory[7]))
print("Porcentaje de Memoria en utlizacion:", memory, "%")

#Comparo la Memoria en uso y si super el 80% lanzo una alerta
if memory > int(os.environ.get("MONIT_MEM_LIMIT")):
   print("Alerta Memoria supera el 80%!!)")
else:
    print("estamos bien de Memoria!!")