CREATE VIEW dim_vendedor AS
SELECT 
    idVendedor    as id,      
    nomeVendedor  as nome,    
    sexoVendedor  as sexo,     
    estadoVendedor as estado
FROM vendedor


CREATE VIEW  dim_combustivel AS
SELECT
    combustivel     as combustivel,
    idcombustivel   as id,
    tipoCombustivel as tipo
FROM combustivel;


CREATE VIEW fato_locacao AS
SELECT
    idLocacao     as id,
    idCliente     as cliente,
    idCarro       as carro,
    idcombustivel as combustivel,
    dataLocacao   as locacao,
    horaLocacao   as horaLocacao,
    qtdDiaria     as dias,
    vlrDiaria     as valor,
    dataEntrega   as entrega,
    horaEntrega   as horaEntrega,
    idVendedor    as vendedor
FROM locacao


CREATE VIEW dim_cliente AS
SELECT
    idCliente       as id,
    nomeCliente     as nome, 
    cidadeCliente   as cidade,
    estadoCliente   as estado,
    paisCliente     as pais
FROM cliente


CREATE VIEW dim_carro AS
SELECT
     idCarro        as id,
     kmCarro        as km,
     classiCarro    as chassi,
     marcaCarro     as marca,
     modeloCarro    as modelo,
     anoCarro       as ano,
     idCombustivel  as combustivel
 FROM carro