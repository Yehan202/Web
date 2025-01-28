create table articulo(
       idarticulo int primary key,
       codigo varchar(50) null,
       nombre varchar(100) not null unique,
       precio_venta float not null, 
       stock int not null,
       descripcion varchar(256) null
);
create table persona(
       idpersona int primary key ,
       nombre varchar(100) not null,
       dni varchar(9) null,
       direccion varchar(70) null,
       telefono varchar(20) null,
       email varchar(50) null
);
create table sospechosos_de_error(
       idarticulo int primary key,
       codigo varchar(50) null,
       nombre varchar(100) not null unique,
       precio_venta float not null, 
       descripcion varchar(256) null
);
create table dinero_total(
       total float );
       
insert into persona values(1, "Pablo", "12345678L", "calle falsa 123","915555556", "p@g.com");
insert into persona values(2, "Cristina", "12365678L", "calle otra 12","915565556", "c@g.com");
insert into persona values(3, "Titi", "12345378L", "calle dos 13","915535556", "t@g.com");
insert into persona values(4, "Irene", "12345278L", "calle tres 23","915535556", "i@g.com");
insert into persona values(5, "Miguel", "12645678L", "calle m 153","915255556", "m@g.com");
insert into persona values(6, "Tomás", "12745678L", "calle do 53","915555556", "t@g.com");
insert into persona values(7, "Álvaro", "12945678L", "calle re 63","915555856", "al@g.com");
insert into persona values(8, "Ana", "12349678L", "calle mi 127","915556856", "a@g.com");
insert into persona values(9, "Inés", "12336678L", "calle fa 138","915455556", "ine@g.com");
insert into persona values(10, "Diego", "12445678L", "calle sol 132","915556556", "dg@g.com");