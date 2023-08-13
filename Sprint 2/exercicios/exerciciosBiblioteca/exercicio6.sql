/* E6
Apresente a query para listar o autor com maior número de livros publicados.
O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes. */

select
    codautor,
    nome,
    count(live.titulo) as quantidade_publicacoes

from autor as aut
    left join livro as live
    on aut.codautor = live.autor
group by codautor
order by quantidade_publicacoes desc
limit 1