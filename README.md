# ITBA
Repositorio con el contenido de las clases de Computer Vision.

Durante la clase utilizaremos varias herramientas y módulos que deberás tener instalados para poder ejecutar el código en tu computadora.

Para no interferir con otros proyectos o instalaciones que tengas previamente, es recomendable crear un entorno virtual para instalar los requerimientos de estas clases y asegurarte de que no van a generar conflictos en tu sistema. 

## Instrucciones para crear un entorno virtual de Python

### Requisitos previos
Asegurate de tener instalado Python en tu sistema antes de comenzar. Podés verificar la instalación ejecutando el siguiente comando en la terminal o en PowerShell:

```shell
python --version
```

Si Python está instalado, se va a imprimir la versión correspondiente. Si no tenés Python instalado, andá al sitio web oficial de Python (https://www.python.org) y descarga una **versión anterior a la 3.10** (esto es por problemas de compatibilidad con una biblioteca que usaremos en la primera clase)

### Crear un entorno virtual con `pip`

1. Abrí la terminal. 
2. Navegá hasta el directorio raíz del repositorio.
3. Ejecuta el siguiente comando para crear un nuevo entorno virtual:

   ```shell
   python -m venv nombre_entorno
   ```

   Reemplaza `nombre_entorno` con el nombre que desees para tu entorno virtual.

4. Activa el entorno virtual ejecutando el siguiente comando:

   **Ubuntu:**

   ```shell
   source nombre_entorno/bin/activate
   ```

   **Windows:**

   ```shell
   nombre_entorno\Scripts\activate
   ```

5. Una vez que el entorno virtual esté activo, ejecutá el siguiente comando para instalar las dependencias desde el archivo `requirements.txt`:

   ```shell
   pip install -r requirements.txt
   ```

   El archivo `requirements.txt` está presente en el directorio raíz del repo.

6. ¡Listo! Ahora podés trabajar con el material de clase dentro del entorno virtual.

7. Para desactivar el entorno virtual cuando hayas terminado, ejecuta el siguiente comando:

   ```shell
   deactivate
   ```

### Crear un entorno virtual con `conda`

1. Abrí la terminal o el Anaconda Prompt (si tienes Anaconda instalado).
2. Navegá hasta el directorio raíz del repositorio.
3. Ejecutá el siguiente comando para crear un nuevo entorno virtual:

   ```shell
   conda create --name nombre_entorno
   ```

   Reemplaza `nombre_entorno` con el nombre que desees para tu entorno virtual.

4. Activá el entorno virtual ejecutando el siguiente comando:

   ```shell
   conda activate nombre_entorno
   ```

5. Una vez que el entorno virtual esté activo, ejecutá el siguiente comando para instalar las dependencias desde el archivo `requirements.txt`:

   ```shell
   conda install --file requirements.txt
   ```

   El archivo `requirements.txt` está presente en el directorio raíz del repo.

6. ¡Listo! Ahora podés trabajar con el material de clase dentro del entorno virtual.

7. Para desactivar el entorno virtual cuando hayas terminado, ejecutá el siguiente comando:

   ```shell
   conda deactivate
   ```

## Material de clase

Cada carpeta tiene los recursos que utilizaremos durante la clase, con exepción de las diapositivas y los datasets, que los podrás ver o descargar en esta sección

### Clase 1

**[Diapositivas](https://docs.google.com/presentation/d/e/2PACX-1vQ4gKwn4zCEuaLozUmLpcBTPn0qT6CqALiOC2uH96MG1uxu3xN2-_LqkzG4b4mp87fBf4PnBOQAU4xt/pub?start=false&loop=false&delayms=3000)** 

**[Dataset](https://www.kaggle.com/datasets/734b7bcb7ef13a045cbdd007a3c19874c2586ed0b02b4afc86126e89d00af8d2?resource=download)**

### Clase 2

**[Diapositivas](https://docs.google.com/presentation/d/e/2PACX-1vQO-NWil3OAbJUgY7C7TlnEnEgknPwVnJjEHM_uuVP1sO_8e6Zs2AZamCs0cXbWOKQxdXy0664EZGkJ/pub?start=false&loop=false&delayms=3000)**

**[Dataset](http://host.robots.ox.ac.uk/pascal/VOC/)**

### Clase 3
