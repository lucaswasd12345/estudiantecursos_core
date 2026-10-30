CREATE DATABASE IF NOT EXISTS esquema_estudiantes_cursos;
USE esquema_estudiantes_cursos;

CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    curso_id INT NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

INSERT INTO cursos (nombre) VALUES
('Python'),
('JavaScript'),
('Base de Datos');

INSERT INTO estudiantes (nombre, apellido, correo, curso_id) VALUES
('Ana', 'Perez', 'ana@correo.com', 1),
('Luis', 'Gomez', 'luis@correo.com', 2),
('Marta', 'Diaz', 'marta@correo.com', 1);
