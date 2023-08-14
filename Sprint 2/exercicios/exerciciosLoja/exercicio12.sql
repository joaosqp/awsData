/*E12
Apresente a query para listar código, nome e data de nascimento dos 
dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). 
As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
Observação: Apenas vendas com status concluído.*/

select 
    dependente.cddep,
    dependente.nmdep, 
    dependente.dtnasc,
    sum(qtd * vrunt) as valor_total_vendas
    
    
from tbdependente as dependente
left join tbvendas as vendas
    on dependente.cdvdd = vendas.cdvdd
where status = "Concluído"
group by dependente.cddep
order by dependente.cddep desc
limit 1