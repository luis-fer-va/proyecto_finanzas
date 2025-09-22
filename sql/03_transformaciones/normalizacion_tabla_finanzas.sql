-- Cambia a la base de datos "finanzas" para ejecutar las operaciones
USE finanzas;

-- =========================================================================
-- Transformación de la Tabla de Hechos (`finanzas`)
-- =========================================================================

-- PASO 1: Agrega las columnas para las nuevas claves foráneas (IDs).
ALTER TABLE finanzas.finanzas
ADD COLUMN entidad_id INT,
ADD COLUMN metodo_pago_id INT,
ADD COLUMN tipo_id INT,
ADD COLUMN categoria_id INT;

-- PASO 2: Actualiza la tabla principal con los IDs numéricos, haciendo un JOIN
-- con las tablas dimensionales.

UPDATE finanzas.finanzas f
JOIN dim_entidad e ON f.entidad = e.nombre
SET f.entidad_id = e.entidad_id;

UPDATE finanzas.finanzas f
JOIN dim_categoria c ON f.categoria = c.nombre
SET f.categoria_id = c.categoria_id;

UPDATE finanzas.finanzas f
JOIN dim_metodo_pago m ON f.metodo_pago = m.nombre
SET f.metodo_pago_id = m.metodo_pago_id;

UPDATE finanzas.finanzas f
JOIN dim_tipo t ON f.tipo = t.nombre
SET f.tipo_id = t.tipo_id;

-- PASO 3: Verifica que no haya valores nulos después de la actualización.
-- Si el resultado es 0, la transformación fue exitosa.
SELECT COUNT(*)
FROM finanzas.finanzas
WHERE entidad_id IS NULL 
    OR metodo_pago_id IS NULL 
    OR categoria_id IS NULL 
    OR tipo_id IS NULL;

-- PASO 4: Elimina las columnas de texto originales para optimizar la tabla.
ALTER TABLE finanzas.finanzas
DROP COLUMN entidad,
DROP COLUMN metodo_pago,
DROP COLUMN categoria,
DROP COLUMN tipo;

-- PASO 5: Establece las relaciones formales de clave foránea.
-- ON DELETE CASCADE asegura la integridad de los datos.
ALTER TABLE finanzas.finanzas
ADD CONSTRAINT fk_entidad
FOREIGN KEY (entidad_id) REFERENCES dim_entidad(entidad_id)
ON DELETE CASCADE;

ALTER TABLE finanzas.finanzas
ADD CONSTRAINT fk_metodo_pago
FOREIGN KEY (metodo_pago_id) REFERENCES dim_metodo_pago(metodo_pago_id)
ON DELETE CASCADE;

ALTER TABLE finanzas.finanzas
ADD CONSTRAINT fk_categoria
FOREIGN KEY (categoria_id) REFERENCES dim_categoria(categoria_id)
ON DELETE CASCADE;

ALTER TABLE finanzas.finanzas
ADD CONSTRAINT fk_tipo
FOREIGN KEY (tipo_id) REFERENCES dim_tipo(tipo_id)
ON DELETE CASCADE;

-- PASO 6: Corrige los formatos de fecha inconsistentes en la columna `fecha`.
UPDATE finanzas.finanzas
SET fecha = CASE
    WHEN LENGTH(fecha) = 10 AND SUBSTRING(fecha, 3, 1) = '/' THEN STR_TO_DATE(fecha, '%d/%m/%Y')
    WHEN LENGTH(fecha) = 9 AND SUBSTRING(fecha, 2, 1) = '/' THEN STR_TO_DATE(fecha, '%d/%m/%Y')
    WHEN LENGTH(fecha) = 10 AND SUBSTRING(fecha, 5, 1) = '/' THEN STR_TO_DATE(fecha, '%Y/%m/%d')
    ELSE fecha
END;
