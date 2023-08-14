/* E12
Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor 
com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser 
cddep, nmdep, dtnasc e valor_total_vendas.


Observação: Apenas vendas com status concluído. */

select 
    cdcli,
    nmcli,
    sum(qtd * vrunt) as gasto

from tbvendas
group by nmcli
order by gasto desc
limit 1