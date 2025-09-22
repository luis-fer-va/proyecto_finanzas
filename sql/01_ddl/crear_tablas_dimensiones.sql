-- Cambia a la base de datos "finanzas" para ejecutar las operaciones
USE finanzas;

-- =========================================================================
-- Definición de Tablas Dimensionales
-- =========================================================================

-- Las siguientes tablas almacenarán valores únicos de texto (entidad, categoría, etc.)
-- para eliminar la redundancia en la tabla principal `finanzas`.

-- Elimina las tablas si ya existen para permitir una ejecución limpia del script.
DROP TABLE IF EXISTS dim_entidad;
DROP TABLE IF EXISTS dim_categoria;
DROP TABLE IF EXISTS dim_metodo_pago;
DROP TABLE IF EXISTS dim_tipo;

-- Crea la tabla para las entidades. `entidad_id` será la clave primaria.
CREATE TABLE dim_entidad (
    entidad_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) UNIQUE
);

-- Crea la tabla para las categorías.
CREATE TABLE dim_categoria (
    categoria_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) UNIQUE
);

-- Crea la tabla para los métodos de pago.
CREATE TABLE dim_metodo_pago (
    metodo_pago_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE
);

-- Crea la tabla para los tipos (ingreso, gasto, etc.).
CREATE TABLE dim_tipo (
    tipo_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE
);
