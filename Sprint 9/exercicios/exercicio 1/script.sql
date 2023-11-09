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
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;


CREATE TABLE cliente (
    idCliente       int primary key,
    nomeCliente     varchar(150),
    cidadeCliente   varchar(50),
    estadoCliente   varchar(50),
    paisCliente     varchar(50)
);
INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;


CREATE TABLE carro (
    idCarro         int primary key,
    kmCarro         int,
    classiCarro     varchar(50),
    marcaCarro      varchar(50),
    modeloCarro     varchar(50),
    anoCarro        int,
    idCombustivel   int,
    FOREIGN KEY (idCombustivel) REFERENCES combustivel(idCombustivel)
);

INSERT OR IGNORE INTO carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel
FROM tb_locacao;



CREATE TABLE combustivel (
    idcombustivel   int primary key,
    tipoCombustivel varchar(15)
);
INSERT INTO combustivel(idcombustivel, tipoCombustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel
FROM tb_locacao;


CREATE TABLE vendedor (
    idVendedor       int primary key,
    nomeVendedor     varchar(100),
    sexoVendedor     int,
    estadoVendedor   varchar (50)
);
INSERT INTO vendedor(idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;