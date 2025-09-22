-- Cambia a la base de datos "finanzas" para ejecutar las operaciones
USE finanzas;

-- =========================================================================
-- Carga de Datos en Tablas Dimensionales
-- =========================================================================

-- Extrae los valores únicos de texto de la tabla `finanzas` y los inserta en las
-- tablas dimensionales correspondientes.

-- Inserta los métodos de pago únicos.
INSERT INTO dim_metodo_pago (nombre)
SELECT DISTINCT metodo_pago
FROM finanzas.finanzas f;

-- Inserta los tipos únicos.
INSERT INTO dim_tipo (nombre)
SELECT DISTINCT tipo
FROM finanzas.finanzas f;

-- Inserta las categorías únicas.
INSERT INTO dim_categoria (nombre)
SELECT DISTINCT categoria
FROM finanzas.finanzas;

-- Inserta las entidades únicas.
INSERT INTO dim_entidad (nombre)
SELECT DISTINCT entidad
FROM finanzas.finanzas;
