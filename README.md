# Status Health

Prueba fork y pull
## Fase1

El objetivo de la primer fase es elaborar un pequeño script que haga algunas verificaciones de la salud del equipo local y si alguno de los criterios establecidos no se cumple mandar una alerta por mail.

Este ejercicio tiene como objectivo aprender:

1. Aprender a interactuar con el sistema operativo desde python.
2. Manipular strings para obtener la informacion que se desea.
3. Entender lo que son variables de entorno en un sistema operativo.
4. Utilizar el protocolo SMTP para envio de mails.
5. Interactuar con repositorio GIT. 

El ejercicio entonces se va a dividir en **dos partes**:

La primera es obtener la siguiente informacion del sistema operativo:
- Cuanto espacio libre hay en /var
- Cuanta memoria libre hay
- Total de procesos corriendos en el equipo.
- Cantidad de CPUS
- El load average mas inmediato

La segunda parte va a consistir en evaluar dichos parametros contra las condiciones
establecidas por un usuario y si alguno de los criterios no se cumple o ninguno, debera
mandarse un mail de alerta usando el protocolo SMTP.

Las condiciones deben poder establecerse mediante variables de entorno, ejemplo:
```
MONIT_MEM_LIMIT=80%
MONIT_DISK_SPACE=80%
```

**Nota 1**: Si se complica encontrando las variables de entorno dejarlo como variables globales al inicio del script del tipo:

```
_MEM_LIMIT=80
_DISK_SPACE_LIMIT=80
```

**Nota 2**: En caso del load average debe evaluarse como critico en el caso de que el total de load average supere el numero de CPUs de la pc. Ejemplo:

Si tengo 2 CPUs, y el load average es igual a **2.4** eso deberia ser una alerta.

Opcional:
- Dejar el script corriendo en crontab.

## Changelog
- Se agrega un ejemplo de como usar un pipe con subprocess.


## Referencias, guias, etc
- [Mandar mails con smtp](https://realpython.com/python-send-email/)
- [Load average](https://www.flopy.es/como-interpretar-correctamente-la-carga-de-la-cpu-load-average-en-equipos-linux/)
- [Crontab](https://en.wikipedia.org/wiki/Cron)
- [Pipe](https://security.openstack.org/guidelines/dg_avoid-shell-true.html)
