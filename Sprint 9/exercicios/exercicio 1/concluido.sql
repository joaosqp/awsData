--
-- Arquivo gerado com SQLiteStudio v3.4.4 em qua nov 8 09:47:22 2023
--
-- Codificação de texto usada: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabela: carro
CREATE TABLE IF NOT EXISTS carro (
    idCarro         int primary key,
    kmCarro         int,
    chassiCarro     varchar(50),
    marcaCarro      varchar(50),
    modeloCarro     varchar(50),
    anoCarro        int,
    idCombustivel   int,
    FOREIGN KEY (idCombustivel) REFERENCES combustivel(idCombustivel)
);

-- Tabela: cliente
CREATE TABLE IF NOT EXISTS cliente (
    idCliente       int primary key,
    nomeCliente     varchar(150),
    cidadeCliente   varchar(50),
    estadoCliente   varchar(50),
    paisCliente     varchar(50)
);

-- Tabela: combustivel
CREATE TABLE IF NOT EXISTS combustivel (
    idCombustivel   int primary key,
    tipoCombustivel varchar(15)
);

-- Tabela: locacao
CREATE TABLE IF NOT EXISTS locacao (
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

-- Tabela: vendedor
CREATE TABLE IF NOT EXISTS vendedor (
    idVendedor       int primary key,
    nomeVendedor     varchar(150),
    sexoVendedor     int,
    estadoVendedor   varchar (50)
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
