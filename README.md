# SinestesiaRCB

Este proyecto es una aplicación práctica de una idea de Rocío Corbacho Barriga para su Trabajo Final de Grado (TFG).

Objetivo
---

El objetivo de este proyecto es la elaboración de un programa que simule la ***sinestesia sonido-color***. Esto se realizará empleando el lenguaje de programación Python. El **esquema** es el que sigue:

1. El usuario pulsa la tecla que desee en el teclado de su ordenador. Cada **tecla** estará asociada a una **nota musical**.
2. La nota musical, que se caracteriza por tener una **frecuencia constante**, estará relacionada con color (asociación sinestésica).
3. El programa representará en pantalla un **trazo aleatorio de dicho color**. **Al mismo tiempo**, la nota será reproducida en el equipo.
4. El trazo representado se desvanecerá pasado un breve lapso de tiempo.

Uso
---

Una vez en funcionamiento, el programa reconocerá en la pantalla las diferentes teclas:

1. Teclas del 0 al 9: corresponden a las notas de más grave a más agudas respectivamente.

2. Tecla escape (ESC): termina la ejecución de los dos programas en ejecución (sonido.py y SinestesiaRCB.py)

Cómo ejecutar el programa
---

0. Antes de comenzar, lo primero que debe hacer es ejecutar el programa sonido.py con python2 (nunca python3.x). En linux seguramente necesite ser administrador (sudo).

`sudo python sonido.py`

1. Tanto en Linux como en Windows, debe ejecutar el programa SinestesiaRCB.py con python3 (o superior).

`python3 SinestesiaRCB.py`

2. En caso de usar Linux, seguramente necesite ejecutar el programa como administrador:

`sudo -E python3 SinestesiaRCB.py`

3. En caso de recibir el error que abajo se cita o similar, puede cambiar temporalmente la pertenencia de la carpeta del usuario para que pertenezca al administrador y evitar así el error, y poder ejecutar el programa. Se recomienda deshacer este cambio una vez terminado de ejecutar el programa.

QStandardPaths: wrong ownership on runtime directory /run/user/1000, 1000 instead of 0

`sudo chown root:SU_USUARIO_LINUX /run/user/1000`

Deshacer con:

`sudo chown SU_USUARIO_LINUX:SU_USUARIO_LINUX /run/user/1000`

4. En caso de que el programa no reproduzca sonido, pese a ejecutarse sin errores, compruebe que no existe un proceso llamado `pulseaudio` en su equipo, y si es así elimínelo para permitir la ejecución de nuestro programa (debe iniciarlo de nuevo).

```
top
# si ve el proceso pulseaudio en la lista, apunte su PID
# salga de este comando pulsando la letra Q(uit) en su teclado
kill -9 PID_del_proceso
# Ahora puede volver a ejecutar SinestesiaRCB.py y sonido.py
```

Librerías Utilizadas
---

1. PyQt5
2. [mingus](http://bspaans.github.io/python-mingus/index.html)
3. [fluidsynth](https://code.google.com/p/mingus/wiki/tutorialFluidsynth)