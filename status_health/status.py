import  subprocess

def get_data(com1, com2):
# funcion que utilizare para obterner el memory space, y la cant de cpu, que me devuelve como resultados una lista
    data_temp = subprocess.run([com1,com2], capture_output=True, encoding='utf-8')
    data = data_temp.stdout.split()
    #print(data)
    return data