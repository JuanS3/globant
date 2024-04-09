-- Crear la tabla de empleados si no existe
CREATE TABLE IF NOT EXISTS employees (
    id              INTEGER PRIMARY KEY,
    name            VARCHAR(255) NOT NULL,
    hire_datetime   TIMESTAMP NOT NULL,
    department_id   INTEGER NOT NULL,
    job_id          INTEGER NOT NULL
);

-- Crear la tabla de departamentos si no existe
CREATE TABLE IF NOT EXISTS departments (
    id          INTEGER PRIMARY KEY,
    department  VARCHAR(255) NOT NULL
);

-- Crear la tabla de trabajos si no existe
CREATE TABLE IF NOT EXISTS jobs (
    id      INTEGER PRIMARY KEY,
    job     VARCHAR(255) NOT NULL
);