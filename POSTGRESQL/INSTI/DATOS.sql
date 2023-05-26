INSERT INTO public.alumno
(id_alumno, nombre_alumno, apellidos_alumno, dni_alumno)
VALUES(1, 'Pedro', 'Viyuela', '12345678A');

INSERT INTO public.alumno
(id_alumno, nombre_alumno, apellidos_alumno, dni_alumno)
VALUES(2, 'José', 'María', '12345678B');

select * from alumno;
select nombre_alumno from alumno where dni_alumno like '%B';

INSERT INTO public.profesor
(id_profesor, nombre_profesor, apellidos_profesor, dni_profesor)
VALUES(1, 'José', 'Pérez Pérez', '12345679A'),(2, 'Pepe', 'Vituela', '12345679B');

INSERT INTO public.asignatura
(id_asignatura, nombre_asignatura, id_profesor)
VALUES(1, 'Matemáticas', 1),(2, 'Lengua', 1),(3, 'Ciencias', 2);

select * from profesor p inner join asignatura a ON (p.id_profesor = a.id_profesor) where p.nombre_profesor like 'José';

INSERT INTO public.alumno_clase(id_alumno, id_asignatura)
VALUES(1, 2),(2,3);

select nombre_alumno from alumno a inner join alumno_clase ac on (a.id_alumno = ac.id_alumno) inner join asignatura a2 on (ac.id_asignatura = a2.id_asignatura) where a2.nombre_asignatura like 'Lengua'
