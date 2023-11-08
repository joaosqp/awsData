' Verificar o banco de dados para analizar quais tabelas criar e seus respectivos tipos de dados'

CREATE TABLE locacao (
    idLocacao     int primary key,
    idCliente     int,
    idCarro       int,
    idcombustivel int,
    dataLocacao   int,
    horaLocacao   TIME,
    qtdDiaria     int,
    vlrDiaria     int,
    dataEntrega   int,
    horaEntrega   TIME,
    idVendedor    int,
    FOREIGN KEY(idCliente) REFERENCES cliente(idCliente),
    FOREIGN KEY(idCarro) REFERENCES carro(idCarro),
    FOREIGN KEY(idcombustivel) REFERENCES combustivel(idcombustivel),
    FOREIGN KEY(idVendedor) REFERENCES vendedor(idVendedor)
);

CREATE TABLE cliente (
    idCliente       int primary key,
    nomeCliente     varchar(150),
    cidadeCliente   varchar(50),
    estadoCliente   varchar(50),
    paisCliente     varchar(50)
);

CREATE TABLE carro (
    idCarro         int primary key,
    kmCarro         int,
    chassiCarro     varchar(50),
    marcaCarro      varchar(50),
    modeloCarro     varchar(50),
    anoCarro        int,
    idCombustivel   int,
    FOREIGN KEY (idCombustivel) REFERENCES combustivel(idCombustivel)
);

CREATE TABLE combustivel (
    idCombustivel   int primary key,
    tipoCombustivel varchar(15)
);

CREATE TABLE vendedor (
    idVendedor       int primary key,
    nomeVendedor     varchar(150),
    sexoVendedor     int,
    estadoVendedor   varchar (50)
);