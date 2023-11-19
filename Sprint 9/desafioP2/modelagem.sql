CREATE TABLE filmes (
    id                  varchar(20) PRIMARY KEY,
    titulopincipal      varchar(50),
    anolancamento       int,
    tempominutos        int,
    notamedia           float,
    numerovotos         int,
    receita             int,
    orcamento           int
);

CREATE TABLE artista (
    generoartista       varchar(20),
    nomeartista         varchar(30),
    id_filme            varchar(20),
    FOREIGN KEY (id_filme) REFERENCES filmes(id)
);
