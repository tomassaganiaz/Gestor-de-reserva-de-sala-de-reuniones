# Gestor-de-reserva-de-sala-de-reuniones
Desarrollar una aplicación orientada a objetos que permita gestionar reservas de salas de reunión en una oficina. Se debe aplicar POO, utilizar al menos un patrón de diseño y estructurar el proyecto en carpetas.

## 🧠 Tecnologías y conceptos aplicados

- ✅ Programación Orientada a Objetos (POO)
- ✅ Patrones de diseño: Singleton, Factory, Repository
- ✅ Separación por capas
- ✅ Docker 

## ▶️ Cómo correr el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/meeting-room-booking.git
cd meeting-room-booking
```

### 2. Ejecutar con Docker 

```bash
docker build -t gestor-reservas .
docker run gestor-reservas
```

## 📁 Estructura del proyecto

meeting-room-booking/
├── src/
│   ├── models/
│   ├── services/
│   ├── repositories/
│   ├── patterns/
│   └── main.py
├── tests/
├── Dockerfile
├── README.md
└── requirements.txt


## Requerimientos Funcionales
-- CRUD de salas y usuarios
Clases como USER y ROOM estan definidas en la carpeta MODELS, y sus operaciones CRUD se gestionan en REPOSITORIES.

-- Reserva con validacion de horarios
BOOKINGSERVICES valida disponibilidad antes de confirmar reservas.

-- Consultas de reservas por usuarios y sala
El servicio permite filtrar reservas por distintos criterios.

-- Al menos 1 patron de diseño
Se aplicaron varios: REPOSITORY, FACTORY, y SINGLETON.

-- Logica basada en Programacion Orientada a Objetos 
El diseño usa Clases, Metodos, Encapsulacion y Separacion por responsabilidades.

-- Estructura clara del proyecto en carpetas
Carpetas organizadas: MODELS, SERVICES, REPOSITORIES, PATTERNS Y MAIN.PY en la raiz.

-- Ejecutable desde un unico comando 
Inicia con MAIN.PY, lo que simplifica el arranque.

-- Plus: Dockerizacion con Dockerfile 
Incluye un DOCKERFILE para levantar todo en contenedor.

-- README.md con instrucciones claras
El archivo README.md explica tecnologias usadas y como ejecutar el proyecto, tanto local como via docker 
