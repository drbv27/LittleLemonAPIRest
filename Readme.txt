# API Endpoints for Testing

## Menu API
- **GET** `/restaurant/menu/`
  - Description: Retrieve a list of all menu items.
  - Example Request: `GET http://127.0.0.1:8000/restaurant/menu/`
  - Example Response: 200 OK, List of menu items in JSON format.

- **POST** `/restaurant/menu/`
  - Description: Create a new menu item.
  - Example Request: 
    ```json
    {
      "Title": "New Dish",
      "Price": "12.99",
      "Inventory": 50
    }
    ```
  - Example Response: 201 Created, Details of the newly created menu item.

- **PUT** `/restaurant/menu/<id>/`
  - Description: Update an existing menu item.
  - Example Request: 
    ```json
    {
      "Title": "Updated Dish",
      "Price": "15.99",
      "Inventory": 40
    }
    ```
  - Example Response: 200 OK, Details of the updated menu item.

- **DELETE** `/restaurant/menu/<id>/`
  - Description: Delete a menu item by ID.
  - Example Request: `DELETE http://127.0.0.1:8000/restaurant/menu/<id>/`
  - Example Response: 204 No Content, Item deleted successfully.

## Booking API
- **GET** `/restaurant/tables/`
  - Description: Retrieve a list of all table bookings.
  - Example Request: `GET http://127.0.0.1:8000/restaurant/tables/`
  - Example Response: 200 OK, List of table bookings in JSON format.

- **POST** `/restaurant/tables/`
  - Description: Create a new table booking.
  - Example Request: 
    ```json
    {
      "Name": "John Doe",
      "No_of_guests": 4,
      "BookingDate": "2024-09-10T18:00:00Z"
    }
    ```
  - Example Response: 201 Created, Details of the newly created table booking.

- **PUT** `/restaurant/tables/<id>/`
  - Description: Update an existing table booking.
  - Example Request: 
    ```json
    {
      "Name": "Jane Doe",
      "No_of_guests": 5,
      "BookingDate": "2024-09-11T19:00:00Z"
    }
    ```
  - Example Response: 200 OK, Details of the updated table booking.

- **DELETE** `/restaurant/tables/<id>/`
  - Description: Delete a table booking by ID.
  - Example Request: `DELETE http://127.0.0.1:8000/restaurant/tables/<id>/`
  - Example Response: 204 No Content, Booking deleted successfully.
