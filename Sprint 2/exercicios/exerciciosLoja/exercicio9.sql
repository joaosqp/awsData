/*E9
Apresente a query para listar o código e nome do produto mais vendido entre 
as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída.
As colunas presentes no resultado devem ser cdpro e nmpro.*/

select     
    cdpro,
    nmpro
from tbvendas
where dtven between '2014-02-03 00:00:00' and '2018-02-02 00:00:00'
group by cdpro, nmpro
order by count (*) desc, nmpro desc
limit 1