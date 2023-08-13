/* E8
Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), 
e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd. */
select 
    vendas.cdvdd,  
    vendedor.nmvdd
    

from tbvendas as vendas
left join tbvendedor as vendedor
    on vendas.cdvdd = vendedor.cdvdd
where status = "Concluído"
group by vendas.cdvdd, vendedor.nmvdd
order by count(*) desc, vendas.cdvdd desc
limit 1