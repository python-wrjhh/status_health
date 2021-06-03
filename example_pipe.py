import subprocess
# Reference:
# https://security.openstack.org/guidelines/dg_avoid-shell-true.html

def how_many_files():
    args1 = ["ls", "-l"]
    args2 = ["wc", "-l"]
    cmd_ls = subprocess.Popen(args1, stdout=subprocess.PIPE, shell=False)
    cmd_wc = subprocess.Popen(args2, stdin=cmd_ls.stdout,
                              stdout=subprocess.PIPE, shell=False)
    cmd_ls.stdout.close()
    return cmd_wc.communicate()[0]


result = how_many_files()
# respuesta es en bytes, no en string:
print(result)
print(type(result))
# para pasar a string necesito
# "decodificar" de bytes a string
# y finalmente aplico el .strip() para eliminar
# el \n de la nueva linea:
result_str = result.decode().strip()
print(result_str)
print(type(result_str))
