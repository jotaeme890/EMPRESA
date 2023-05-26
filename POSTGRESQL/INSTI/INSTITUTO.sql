create table Profesor(
	id_Profesor int primary key not null,
	nombre_Profesor varchar(50) not null,
	apellidos_Profesor varchar(50) not null,
	dni_Profesor char(9) unique not null check(dni_Profesor like '[0-9]{8}[A-Z]')
);

create table Asignatura(
	id_Asignatura int primary key not null,
	nombre_Asignatura varchar(50) not null,
	id_Profesor int not null,
	foreign key (id_Profesor) references Profesor(id_Profesor)
);

create table Alumno(
	id_Alumno int primary key not null,
	nombre_Alumno varchar(50) not null,
	apellidos_Alumno varchar(50) not null,
	dni_Alumno char(9) unique not null check(dni_Alumno like '[0-9]{8}[A-Z]')
);

create table Alumno_Clase(
	id_Alumno int not null,
	id_Asignatura int not null,
	primary key (id_Alumno, id_Asignatura),
	foreign key (id_Alumno) references Alumno(id_Alumno),
	foreign key (id_Asignatura) references Asignatura(id_Asignatura)
);