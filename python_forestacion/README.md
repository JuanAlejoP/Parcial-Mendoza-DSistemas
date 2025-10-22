# Sistema de Gestión Forestal

Proyecto de examen parcial implementando un sistema de gestión forestal con múltiples patrones de diseño.

## Patrones Implementados

### 1. Singleton - CultivoServiceRegistry
- Registro único de servicios para cultivos
- Thread-safe usando double-checked locking
- Lazy initialization
- Dispatch polimórfico sin `isinstance()`

### 2. Factory - CultivoFactory
- Creación de diferentes tipos de cultivos
- Diccionario de factories en lugar de if/else
- Encapsula lógica de creación
- Soporte para: Pino, Olivo, Lechuga, Zanahoria

### 3. Observer - Sistema de Riego
- Sensores observables de temperatura y humedad
- ControlRiego como observador de sensores
- Genéricos tipo-seguros (`Observable[T]`, `Observer[T]`)
- Threads daemon para lecturas en background

### 4. Strategy - Absorción de Agua
- Estrategias intercambiables de absorción
- AbsorcionSeasonalStrategy para árboles
- AbsorcionConstanteStrategy para hortalizas
- Inyección de dependencias en constructores

## Estructura del Proyecto

```
python_forestacion/
├── src/
│   ├── entidades/
│   │   ├── cultivos/       # Clases de cultivos (árboles y hortalizas)
│   │   ├── personal/       # Clases de personal y tareas
│   │   └── terrenos/       # Clases de terrenos y plantaciones
│   ├── excepciones/        # Excepciones personalizadas
│   ├── patrones/
│   │   ├── factory/        # Factory Method para cultivos
│   │   ├── observer/       # Observer para sensores
│   │   └── strategy/       # Strategy para absorción
│   ├── riego/
│   │   ├── control/        # Control de riego automático
│   │   └── sensores/       # Sensores de temperatura y humedad
│   └── servicios/
│       ├── cultivos/       # Servicios específicos por cultivo
│       ├── personal/       # Servicios de gestión de personal
│       └── terrenos/       # Servicios de terrenos y plantaciones
└── data/                   # Directorio para persistencia de registros