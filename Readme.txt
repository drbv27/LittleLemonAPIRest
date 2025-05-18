# Endpoints de la API para Pruebas

## API de Menú
- **GET** `/restaurant/menu/`
  - **Descripción:** Recupera una lista de todos los ítems del menú.
  - **Petición Ejemplo:** `GET http://127.0.0.1:8000/restaurant/menu/`
  - **Respuesta Ejemplo:** 200 OK, Lista de ítems del menú en formato JSON.

- **POST** `/restaurant/menu/`
  - **Descripción:** Crea un nuevo ítem en el menú.
  - **Petición Ejemplo:**
    ```json
    {
      "Title": "Nuevo Plato",
      "Price": "12.99",
      "Inventory": 50
    }
    ```
  - **Respuesta Ejemplo:** 201 Created, Detalles del ítem del menú recién creado.

- **PUT** `/restaurant/menu/<id>/`
  - **Descripción:** Actualiza un ítem existente del menú.
  - **Petición Ejemplo:**
    ```json
    {
      "Title": "Plato Actualizado",
      "Price": "15.99",
      "Inventory": 40
    }
    ```
  - **Respuesta Ejemplo:** 200 OK, Detalles del ítem del menú actualizado.

- **DELETE** `/restaurant/menu/<id>/`
  - **Descripción:** Elimina un ítem del menú por su ID.
  - **Petición Ejemplo:** `DELETE http://127.0.0.1:8000/restaurant/menu/<id>/`
  - **Respuesta Ejemplo:** 204 No Content, Ítem eliminado exitosamente.

## API de Reservas
- **GET** `/restaurant/tables/`
  - **Descripción:** Recupera una lista de todas las reservas de mesas.
  - **Petición Ejemplo:** `GET http://127.0.0.1:8000/restaurant/tables/`
  - **Respuesta Ejemplo:** 200 OK, Lista de reservas de mesas en formato JSON.

- **POST** `/restaurant/tables/`
  - **Descripción:** Crea una nueva reserva de mesa.
  - **Petición Ejemplo:**
    ```json
    {
      "Name": "John Doe",
      "No_of_guests": 4,
      "BookingDate": "2024-09-10T18:00:00Z"
    }
    ```
  - **Respuesta Ejemplo:** 201 Created, Detalles de la reserva de mesa recién creada.

- **PUT** `/restaurant/tables/<id>/`
  - **Descripción:** Actualiza una reserva de mesa existente.
  - **Petición Ejemplo:**
    ```json
    {
      "Name": "Jane Doe",
      "No_of_guests": 5,
      "BookingDate": "2024-09-11T19:00:00Z"
    }
    ```
  - **Respuesta Ejemplo:** 200 OK, Detalles de la reserva de mesa actualizada.

- **DELETE** `/restaurant/tables/<id>/`
  - **Descripción:** Elimina una reserva de mesa por su ID.
  - **Petición Ejemplo:** `DELETE http://127.0.0.1:8000/restaurant/tables/<id>/`
  - **Respuesta Ejemplo:** 204 No Content, Reserva eliminada exitosamente.