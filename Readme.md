# Little Lemon Restaurant - API Backend con Django

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.16.0-A30000?logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Djoser](https://img.shields.io/badge/Djoser-2.3.1-lightgrey?logo=django&logoColor=black)](https://djoser.readthedocs.io/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)

## Descripción general

Este proyecto de el restaurante ficticio Little Lemon, representa el trabajo Final del `Certificado Profesional BackEnd de META`. Desarrollado con Django y Django REST framework, proporciona endpoints para gestionar el menú del restaurante, un sistema robusto para la gestión de reservas, autenticación de usuarios (incluyendo JWT) y la conexión con una base de datos MySQL. Este backend está diseñado para ser consumido por una aplicación frontend (no incluida en este repositorio).

**Muy importante** el `render` de la pagina está en [http://127.0.0.1:8000/home/](http://127.0.0.1:8000/home/)

## Plan de estudios del curso

Aquí un breve resumen de cómo abordé este proyecto a través de los módulos del curso:

### Módulo 1: Iniciando el Proyecto

- **Configuración Inicial:** Comencé estableciendo mi entorno de desarrollo y familiarizándome con Django.
- **Objetivos:**
  - Desarrollé una aplicación backend utilizando Django.
  - Serví contenido HTML estático.
  - Consolidé el proyecto en un repositorio Git.

### Módulo 2: Funcionalidad del Proyecto

- **Modelos de Base de Datos:** Me conecté a MySQL y creé los modelos necesarios para la aplicación.
- **APIs:** Desarrollé e implementé APIs para la gestión de menús y reservas de mesas utilizando Django REST Framework.

### Módulo 3: Seguridad y Pruebas

- **Autenticación:** Añadí funcionalidades de registro de usuarios, inicio y cierre de sesión para asegurar la aplicación.
- **Seguridad:** Implementé medidas para proteger la API de reserva de mesas y asegurar la integridad de los datos.
- **Pruebas:** Realicé pruebas unitarias y probé los endpoints de la API con el cliente REST Insomnia.
- **GitHub:** Subí todos mis commits de código a GitHub.

### Módulo 4: Evaluación Calificada

- **Evaluación:** Comparé mi código y diseño con el de mis compañeros, abordé algunas de las partes más desafiantes del proyecto y completé una evaluación calificada.

## 📸 Screenshots del API

Aquí puedes ver algunas capturas de pantalla de la API navegable de Django REST Framework y el panel de administración:

<table>
  <tr>
    <td align="center">
      API Root<br>
      <img src="https://raw.githubusercontent.com/drbv27/LittleLemonAPIRest/main/restaurant/static/img/APIRoot.jpeg" alt="API Root" width="400"/>
    </td>
    <td align="center">
      Booking List (Autenticado)<br>
      <img src="https://raw.githubusercontent.com/drbv27/LittleLemonAPIRest/main/restaurant/static/img/BookingList.jpeg" alt="Booking List (Autenticado)" width="400"/>
    </td>
  </tr>
  <tr>
    <td align="center">
      Djoser Auth Endpoints<br>
      <img src="https://raw.githubusercontent.com/drbv27/LittleLemonAPIRest/main/restaurant/static/img/DjoserRoot.jpeg" alt="Djoser Auth Endpoints" width="400"/>
    </td>
    <td align="center">
      Django Admin Panel<br>
      <img src="https://raw.githubusercontent.com/drbv27/LittleLemonAPIRest/main/restaurant/static/img/DjangoAdmin.jpeg" alt="Django Admin Panel" width="400"/>
    </td>
  </tr>
  </table>

## 🚀 Cómo Ejecutar el Proyecto Localmente

Sigue estos pasos para poner en marcha el proyecto en tu máquina local. Estas instrucciones asumen que tienes Python 3.x (preferiblemente 3.13 o compatible) y Git instalados, y que estás usando una terminal tipo Bash (como Git Bash en Windows).

**1. Clonar el Repositorio**

Primero, clona este repositorio en tu máquina local:

```bash
git clone [URL_DE_TU_REPOSITORIO_GITHUB_AQUI]
cd LittleLemon-main/littlelemonfinal  # O la ruta correcta a la carpeta que contiene manage.py
```

_(Nota: El nombre de la carpeta principal después de clonar podría ser `LittleLemon-main` o el nombre de tu repositorio. Asegúrate de que la ruta `cd` te lleve al directorio que contiene `manage.py` y donde crearás la carpeta `venv`)_.

**2. Instalar y Configurar el Servidor MySQL**

Este proyecto requiere una base de datos MySQL.

- Asegúrate de que tu servidor MySQL esté en ejecución.
- Necesitarás crear una base de datos para el proyecto. Para este proyecto, el nombre de la base de datos es `littlelemon`.
- Asegúrate de que el usuario de MySQL que configurarás en Django (en `settings.py`) tenga los permisos necesarios sobre esta base de datos.

Puedes crear la base de datos ejecutando en tu cliente MySQL:

```sql
CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Guías para la instalación de MySQL:

- **Windows:** MySQL Community Server desde [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/).
- **macOS:** Homebrew: `brew install mysql`, `brew services start mysql`. O el instalador oficial desde [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/).
- **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install mysql-server`. Luego `sudo mysql_secure_installation`.

**3. Configurar `settings.py` (Importante)**

Abre el archivo de configuración de Django (generalmente ubicado en `nombre_de_tu_proyecto_django/settings.py`, que en tu caso podría ser `littlelemonfinal/settings.py` dentro de la carpeta donde está `manage.py`). Verifica la sección `DATABASES`:

```python
# En tu archivo settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'USER': 'tu_usuario_mysql',    # Ej. 'root' o un usuario dedicado
        'PASSWORD': 'tu_contraseña_mysql',
        'HOST': 'localhost',           # O '127.0.0.1'
        'PORT': '3306',
    }
}
```

_(**Importante**: No subas contraseñas a repositorios públicos. Usa variables de entorno para datos sensibles)._

**4. Crear y Activar un Entorno Virtual**

Dentro de la carpeta del proyecto (donde está `manage.py`):

```bash
   python -m venv venv
```

**Activar:**

- Windows (Git Bash): `source venv/Scripts/activate`
- macOS/Linux: `source venv/bin/activate`

_(Verás `(venv)` en tu prompt)._

**5. Instalar Dependencias**

Con el entorno virtual activado:

```bash
   pip install -r requirements.txt
```

**6. Aplicar Migraciones de Base de Datos**

```bash
   python manage.py migrate
```

**7. Crear un Superusuario**

Para acceder al admin y autenticarte en la API navegable:

```bash
   python manage.py createsuperuser
```

**8. Ejecutar el Servidor de Desarrollo**

```bash
   python manage.py runserver
```

**9. Abrir en el Navegador**

Servidor en `http://127.0.0.1:8000/`:

- **API Root:** [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)
- **Admin Panel:** [`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/)

## ✨ Características Principales

- **Gestión de Menú:** Endpoints para gestionar los menús del restaurante.
- **Reserva de Mesas:** Endpoints para reservar mesas.
- **Autenticación de Usuarios:** Incluye funcionalidades de registro, inicio de sesión y cierre de sesión.
- **Pruebas:** Incluye pruebas unitarias y pruebas de endpoints de API con Insomnia.

## 🔑 Documentación de Endpoints de la API

Inicia sesión en la API navegable (a través de `/admin/` o los endpoints de Djoser) para interactuar con los endpoints protegidos.

### Menu API

_(Verifica en tus `urls.py` si la ruta `/restaurant/menu/` está activa y correctamente configurada en este proyecto)._

- **GET** `/restaurant/menu/`

  - **Descripción:** Recupera una lista de todos los ítems del menú.
  - **Respuesta Ejemplo:** 200 OK, Lista de ítems del menú en formato JSON.

- **POST** `/restaurant/menu/`

  - **Descripción:** Crea un nuevo ítem en el menú. (Requiere autenticación y permisos adecuados).
  - **Cuerpo Ejemplo:**
    ```json
    {
      "Title": "New Dish",
      "Price": "12.99",
      "Inventory": 50
    }
    ```
  - **Respuesta Ejemplo:** 201 Created, Detalles del ítem del menú creado.

- **GET** `/restaurant/menu/{id}/`

  - **Descripción:** Recupera un ítem específico del menú por su ID.
  - **Respuesta Ejemplo:** 200 OK, Detalles del ítem del menú.

- **PUT** `/restaurant/menu/{id}/`

  - **Descripción:** Actualiza un ítem existente del menú por su ID. (Requiere autenticación y permisos adecuados).
  - **Cuerpo Ejemplo:**
    ```json
    {
      "Title": "Updated Dish",
      "Price": "15.99",
      "Inventory": 40
    }
    ```
  - **Respuesta Ejemplo:** 200 OK, Detalles del ítem del menú actualizado.

- **DELETE** `/restaurant/menu/{id}/`
  - **Descripción:** Elimina un ítem del menú por su ID. (Requiere autenticación y permisos adecuados).
  - **Respuesta Ejemplo:** 204 No Content, Ítem eliminado exitosamente.

### Booking API

_(La ruta principal podría ser `/restaurant/tables/` o `/restaurant/booking/tables/`. Verifica tus `urls.py`)_.

- **GET** `/restaurant/tables/`

  - **Descripción:** Recupera una lista de todas las reservas de mesas. (Requiere autenticación).
  - **Respuesta Ejemplo:** 200 OK, Lista de reservas en formato JSON.

- **POST** `/restaurant/tables/`

  - **Descripción:** Crea una nueva reserva de mesa. (Requiere autenticación).
  - **Cuerpo Ejemplo:**
    ```json
    {
      "Name": "John Doe",
      "No_of_guests": 4,
      "BookingDate": "2024-09-10T18:00:00Z"
    }
    ```
  - **Respuesta Ejemplo:** 201 Created, Detalles de la reserva creada.

- **GET** `/restaurant/tables/{id}/`

  - **Descripción:** Recupera una reserva específica por su ID. (Requiere autenticación).
  - **Respuesta Ejemplo:** 200 OK, Detalles de la reserva.

- **PUT** `/restaurant/tables/{id}/`

  - **Descripción:** Actualiza una reserva existente por su ID. (Requiere autenticación).
  - **Cuerpo Ejemplo:**
    ```json
    {
      "Name": "Jane Doe",
      "No_of_guests": 5,
      "BookingDate": "2024-09-11T19:00:00Z"
    }
    ```
  - **Respuesta Ejemplo:** 200 OK, Detalles de la reserva actualizada.

- **DELETE** `/restaurant/tables/{id}/`
  - **Descripción:** Elimina una reserva por su ID. (Requiere autenticación).
  - **Respuesta Ejemplo:** 204 No Content, Reserva eliminada exitosamente.

### Autenticación (Djoser Endpoints)

Explora `http://127.0.0.1:8000/auth/` para:

- `users/` (registro, listado de usuarios)
- `users/me/` (ver/editar perfil del usuario autenticado)
- `jwt/create/` (para obtener tokens JWT)
- `jwt/refresh/` (para refrescar un token JWT)
- `jwt/verify/` (para verificar un token JWT)
- Y otros según la configuración de Djoser en `urls.py`.

## 📫 Contacto

[![GitHub](https://img.shields.io/badge/GitHub-drbv27-181717?logo=github)](https://github.com/drbv27)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-DiegoBonilla-0A66C2?logo=linkedin)](https://www.linkedin.com/in/diego-ricardo-bonilla-villa-7179254a/)
[![Email](https://img.shields.io/badge/Email-DiegoBonilla-D14836?logo=gmail)](mailto:drbv27@gmail.com)
