# Cumplo-BackEnd
BackEnd para el desafio de Cumplo


# Herramientas y Utilidades Requeridas

- [Docker](https://docs.docker.com/install/)
- [Docker-Compose](https://docs.docker.com/compose/)
- [Token de Banxico](https://www.banxico.org.mx/SieAPIRest/service/v1/token)

*Nota*
- Se proporcionara el archivo .env adjunto en el envio del proyecto al destinatario.


# Inicializar el proyecto

Correr el proyecto en local:

```bash
docker-compose up
```

Esperar en promedio 3 minutos y acceder en el navegador a la siguiente ruta:

```
http://localhost:8080/
```

El proyecto de manera local corre en ```localhost:8000/admin/```, a modo de [produccion](https://cumplo-back-test.herokuapp.com/) se visualiza en ```https://cumplo-back-test.herokuapp.com/```





**Documentacion de la API:**

# Requerimiento de Tipos de Cambio
Obtener data de tipos de cambio especifico, Los solicitados son: UDI's, USD y TIIE


## Informacion Obtenida

**Request**:

`POST` `/currencies`

Parametros:

Nombre           | Descripcion
-----------------|------------
currency         | valor de Cambio Soliitado: Pueden Ser USD(SF43718) , TIIE(SF331451,SF43783,SF43878) o UDI(SP68257)
init_date        | Fecha inicial para la busqueda.
end_date         | Fecha final para la busqueda.




**Ejemplo de Respuesta de la API con USD**:

```json
http://localhost:8000/currencies/
Content-Type application/json
200 Ok
{
    "average": 18.70206,
    "min": 18.6245,
    "max": 18.7763,
    "currency_values": [
        {
            "fecha": "04/02/2020",
            "dato": "18.6797"
        },
        {
            "fecha": "05/02/2020",
            "dato": "18.6245"
        },
        {
            "fecha": "06/02/2020",
            "dato": "18.6645"
        },
        {
            "fecha": "07/02/2020",
            "dato": "18.7763"
        },
        {
            "fecha": "10/02/2020",
            "dato": "18.7653"
        }
    ]
}
```

**Ejemplo de Respuesta de la API con UDI**:


```json
http://localhost:8000/currencies/
Content-Type application/json
200 Ok
{
    "average": 6.446652555555556,
    "min": 6.442361,
    "max": 6.450946,
    "currency_values": [
        {
            "fecha": "02/02/2020",
            "dato": "6.442361"
        },
        {
            "fecha": "03/02/2020",
            "dato": "6.443433"
        },
        {
            "fecha": "04/02/2020",
            "dato": "6.444506"
        },
        {
            "fecha": "05/02/2020",
            "dato": "6.445579"
        },
        {
            "fecha": "06/02/2020",
            "dato": "6.446652"
        },
        {
            "fecha": "07/02/2020",
            "dato": "6.447725"
        },
        {
            "fecha": "08/02/2020",
            "dato": "6.448799"
        },
        {
            "fecha": "09/02/2020",
            "dato": "6.449872"
        },
        {
            "fecha": "10/02/2020",
            "dato": "6.450946"
        }
    ]
}
```
**Ejemplo de Respuesta de la API con  4 TIIE's**:


```json
http://localhost:8000/currencies/
Content-Type application/json
200 Ok
{
    "T1": [
        {
            "fecha": "06/02/2020",
            "dato": "7.2780"
        }
    ],
    "T2": [
        {
            "fecha": "04/02/2020",
            "dato": "7.26"
        },
        {
            "fecha": "05/02/2020",
            "dato": "7.28"
        },
        {
            "fecha": "06/02/2020",
            "dato": "7.29"
        },
        {
            "fecha": "07/02/2020",
            "dato": "7.30"
        },
        {
            "fecha": "10/02/2020",
            "dato": "7.29"
        }
    ],
    "T3": [
        {
            "fecha": "04/02/2020",
            "dato": "7.3975"
        },
        {
            "fecha": "05/02/2020",
            "dato": "7.3925"
        },
        {
            "fecha": "06/02/2020",
            "dato": "7.3825"
        },
        {
            "fecha": "07/02/2020",
            "dato": "7.3815"
        },
        {
            "fecha": "10/02/2020",
            "dato": "7.3700"
        }
    ],
    "T4": [
        {
            "fecha": "04/02/2020",
            "dato": "7.4951"
        },
        {
            "fecha": "05/02/2020",
            "dato": "7.4937"
        },
        {
            "fecha": "06/02/2020",
            "dato": "7.4925"
        },
        {
            "fecha": "07/02/2020",
            "dato": "7.4915"
        },
        {
            "fecha": "10/02/2020",
            "dato": "7.4892"
        }
    ]
}
```


