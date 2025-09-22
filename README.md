# proyecto_finanzas
Este proyecto contiene un script SQL diseñado para transformar y limpiar una base de datos de finanzas, convirtiéndola a un esquema de estrella optimizado para el análisis de datos.
```
proyecto_finanzas/
├── sql/
│   ├── 01_ddl/
│   │   └── crear_tablas_dimensiones.sql
│   ├── 02_dml/
│   │   └── cargar_datos_dimensiones.sql
│   └── 03_transformaciones/
│       └── normalizacion_tabla_finanzas.sql
├── app_tkinter/
│   ├── conexion.py                 # Script para la conexión a la base de datos
│   ├── Form_Gastos_y_Ingresos.pyw  # app principal de Tkinter
│   └── __pycache__/                # Carpeta de caché, que debes ignorar en Git
└── README.md
```
