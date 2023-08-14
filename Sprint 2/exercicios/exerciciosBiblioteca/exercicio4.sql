/* E4
Apresente a query para listar a quantidade de livros publicada por cada autor. 
Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).*/

select 
    aut.nome,
    aut.codautor,
    aut.nascimento,
    count(*) as quantidade 
    

from autor as aut
left join livro as liv
    on aut.codautor = liv.autor
group by aut.nome
