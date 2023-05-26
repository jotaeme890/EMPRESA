create table Cliente(
	id_Cliente serial PRIMARY KEY,
	nombre_Cliente varchar(50) not null,
	apellido_Cliente varchar(50) not null,
	fechaNac_Cliente date not null,
	dni_Cliente char(9) unique not null check(dni_Cliente ~* '[0-9]{8}[A-Z]'), 
	telefono_Cliente int unique not null,
	correo_Cliente varchar(50) not null check(correo_Cliente ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
	calle_Cliente varchar (50) not null
);

create table Cuenta(
	id_Cuenta int primary key not null,
	CCC_Cuenta int not null unique check(length(cast (CCC_Cuenta as text)) = 20),
	IBAN_Cuenta varchar(24) not null unique check(length(cast (IBAN_Cuenta as text)) = 25)
);

create table Cliente_Cuenta(
	id_Cliente int not null,
    id_Cuenta int not null,
    fecha_Creacion date not null,
    primary key (id_Cliente, id_Cuenta),
    foreign key (id_Cliente) REFERENCES Cliente(id_Cliente),
    foreign key (id_Cuenta) REFERENCES Cuenta(id_Cuenta)
);

create table Movimiento(
	id_Movimiento int primary key not null,
	id_CuentaEmisora int not null,
	id_CuentaReceptora int not null,
	tipo_Movimiento varchar(15) not null check(tipo_Movimiento in ('retiro','ingreso')),
	cantidad_Movimiento int not null,
	fecha_Movimiento date not null,
	foreign key (id_CuentaEmisora) references Cuenta(id_Cuenta),
	foreign key (id_CuentaReceptora) references Cuenta(id_Cuenta)
);
