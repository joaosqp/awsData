--
-- Arquivo gerado com SQLiteStudio v3.4.4 em qua nov 8 20:02:07 2023
--
-- Codificação de texto usada: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabela: carro
CREATE TABLE IF NOT EXISTS carro (
    idCarro         int primary key,
    kmCarro         int,
    classiCarro     varchar(50),
    marcaCarro      varchar(50),
    modeloCarro     varchar(50),
    anoCarro        int,
    idCombustivel   int,
    FOREIGN KEY (idCombustivel) REFERENCES combustivel(idCombustivel)
);
INSERT INTO carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (98, 25412, 'AKJHKN98JY76539', 'Fiat', 'Fiat Uno', 2000, 1);
INSERT INTO carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (99, 20000, 'IKJHKN98JY76539', 'Fiat', 'Fiat Palio', 2010, 1);
INSERT INTO carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (3, 121700, 'DKSHKNS8JS76S39', 'VW', 'Fusca 78', 1978, 1);
INSERT INTO carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (10, 211800, 'LKIUNS8JS76S39', 'Fiat', 'Fiat 147', 1996, 1);
INSERT INTO carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (7, 212800, 'SSIUNS8JS76S39', 'Fiat', 'Fiat 147', 1996, 1);
INSERT INTO carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (6, 21800, 'SKIUNS8JS76S39', 'Nissan', 'Versa', 2019, 1);
INSERT INTO carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (2, 10000, 'AKIUNS1JS76S39', 'Nissan', 'Versa', 2019, 2);
INSERT INTO carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (4, 55000, 'LLLUNS1JS76S39', 'Nissan', 'Versa', 2020, 2);
INSERT INTO carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (1, 1800, 'AAAKNS8JS76S39', 'Toyota', 'Corolla XEI', 2023, 3);
INSERT INTO carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel) VALUES (5, 28000, 'MSLUNS1JS76S39', 'Nissan', 'Frontier', 2022, 4);

-- Tabela: cliente
CREATE TABLE IF NOT EXISTS cliente (
    idCliente       int primary key,
    nomeCliente     varchar(150),
    cidadeCliente   varchar(50),
    estadoCliente   varchar(50),
    paisCliente     varchar(50)
);
INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) VALUES (2, 'Cliente dois', 'São Paulo', 'São Paulo', 'Brasil');
INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) VALUES (3, 'Cliente tres', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil');
INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) VALUES (4, 'Cliente quatro', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil');
INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) VALUES (6, 'Cliente seis', 'Belo Horizonte', 'Minas Gerais', 'Brasil');
INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) VALUES (10, 'Cliente dez', 'Rio Branco', 'Acre', 'Brasil');
INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) VALUES (20, 'Cliente vinte', 'Macapá', 'Amapá', 'Brasil');
INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) VALUES (22, 'Cliente vinte e dois', 'Porto Alegre', 'Rio Grande do Sul', 'Brasil');
INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) VALUES (23, 'Cliente vinte e tres', 'Eusébio', 'Ceará', 'Brasil');
INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) VALUES (5, 'Cliente cinco', 'Manaus', 'Amazonas', 'Brasil');
INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente) VALUES (26, 'Cliente vinte e seis', 'Campo Grande', 'Mato Grosso do Sul', 'Brasil');

-- Tabela: combustivel
CREATE TABLE IF NOT EXISTS combustivel (
    idcombustivel   int primary key,
    tipoCombustivel varchar(15)
);
INSERT INTO combustivel (idcombustivel, tipoCombustivel) VALUES (1, 'Gasolina');
INSERT INTO combustivel (idcombustivel, tipoCombustivel) VALUES (2, 'Etanol');
INSERT INTO combustivel (idcombustivel, tipoCombustivel) VALUES (3, 'Flex');
INSERT INTO combustivel (idcombustivel, tipoCombustivel) VALUES (4, 'Diesel');

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
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (1, 2, 98, 1, 20150110, '10:00', 2, 100, 20150112, '10:00', 5);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (2, 2, 98, 1, 20150210, '12:00', 2, 100, 20150212, '12:00', 5);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (3, 3, 99, 1, 20150213, '12:00', 2, 150, 20150215, '12:00', 6);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (4, 4, 99, 1, 20150215, '13:00', 5, 150, 20150220, '13:00', 6);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (5, 4, 99, 1, 20150302, '14:00', 5, 150, 20150307, '14:00', 7);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (6, 6, 3, 1, 20160302, '14:00', 10, 250, 20160312, '14:00', 8);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (7, 6, 3, 1, 20160802, '14:00', 10, 250, 20160812, '14:00', 8);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (8, 4, 3, 1, 20170102, '18:00', 10, 250, 20170112, '18:00', 6);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (9, 4, 3, 1, 20180102, '18:00', 10, 280, 20180112, '18:00', 6);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (10, 10, 10, 1, 20180302, '18:00', 10, 50, 20180312, '18:00', 16);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (11, 20, 7, 1, 20180401, '11:00', 10, 50, 20180411, '11:00', 16);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (12, 20, 6, 1, 20200401, '11:00', 10, 150, 20200411, '11:00', 16);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (13, 22, 2, 2, 20220501, '8:00', 20, 150, 20220521, '18:00', 30);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (14, 22, 2, 2, 20220601, '8:00', 20, 150, 20220621, '18:00', 30);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (15, 22, 2, 2, 20220701, '8:00', 20, 150, 20220721, '18:00', 30);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (16, 22, 2, 2, 20220801, '8:00', 20, 150, 20220721, '18:00', 30);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (17, 23, 4, 2, 20220901, '8:00', 20, 150, 20220921, '18:00', 31);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (18, 23, 4, 2, 20221001, '8:00', 20, 150, 20221021, '18:00', 31);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (19, 23, 4, 2, 20221101, '8:00', 20, 150, 20221121, '18:00', 31);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (20, 5, 1, 3, 20230102, '18:00', 10, 880, 20230112, '18:00', 16);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (21, 5, 1, 3, 20230115, '18:00', 10, 880, 20230125, '18:00', 16);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (22, 26, 5, 4, 20230125, '8:00', 5, 600, 20230130, '18:00', 32);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (23, 26, 5, 4, 20230131, '8:00', 5, 600, 20230205, '18:00', 32);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (24, 26, 5, 4, 20230206, '8:00', 5, 600, 20230211, '18:00', 32);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (25, 26, 5, 4, 20230212, '8:00', 5, 600, 20230217, '18:00', 32);
INSERT INTO locacao (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor) VALUES (26, 26, 5, 4, 20230218, '8:00', 1, 600, 20230219, '18:00', 32);

-- Tabela: vendedor
CREATE TABLE IF NOT EXISTS vendedor (
    idVendedor       int primary key,
    nomeVendedor     varchar(100),
    sexoVendedor     int,
    estadoVendedor   varchar (50)
);
INSERT INTO vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (5, 'Vendedor cinco', 0, 'São Paulo');
INSERT INTO vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (6, 'Vendedora seis', 1, 'São Paulo');
INSERT INTO vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (7, 'Vendedora sete', 1, 'Rio de Janeiro');
INSERT INTO vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (8, 'Vendedora oito', 1, 'Minas Gerais');
INSERT INTO vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (16, 'Vendedor dezesseis', 0, 'Amazonas');
INSERT INTO vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (30, 'Vendedor trinta', 0, 'Rio Grande do Sul');
INSERT INTO vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (31, 'Vendedor trinta e um', 0, 'Ceará');
INSERT INTO vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor) VALUES (32, 'Vendedora trinta e dois', 1, 'Mato Grosso do Sul');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
