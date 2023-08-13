/* E7
Apresente a query para listar o nome dos autores com nenhuma publicação. ]
Apresentá-los em ordem crescente. */

select 
     nome

from autor as aut
left join livro as live
    on aut.codautor = live.autor
group by codautor
having count(live.titulo) = 0
order by nome