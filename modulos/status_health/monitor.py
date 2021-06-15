#obtener espacio diponible en mi /var

import subprocess

hostname = subprocess.run(["hostname"], capture_output=True, encoding='utf-8')
var_space = subprocess.run(["df","-h","/var"], capture_output=True, encoding='utf-8')
mem_space = subprocess.run(["free","thm"], capture_output=True, encoding='utf-8')
cant_proc = subprocess.run(["ps","-ef"], capture_output=True, encoding='utf-8') #no se como poner el | wc -l
cant_cpu = subprocess.run(["getconf","_NPROCESSORS_ONLN"], capture_output=True, encoding='utf-8')
load_avg = subprocess.run(["uptime"], capture_output=True, encoding='utf-8')

print("******** Hostname *************")
print(hostname.stdout)
print("******** Espacio /var **************")
print(var_space.stdout)
print("******** memoria libre *************")
print(mem_space.stdout)
print("********* Procesos ************")
print(cant_proc)
print("********* CPUs ************")
print(cant_cpu.stdout)
print("********* Load Agerage ************")
print(load_avg.stdout)

#Consultar:
#Como contatenar comandos si tengo un |
#como llevarme el valor que quiero de la salida de un comando. 