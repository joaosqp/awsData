/*E3
 Apresente a query para listar as 5 editoras com mais livros na biblioteca. 
 O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
 Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.*/

select 
    count(liv.editora) as quantidade,
    nome, 
    estado,
    cidade
    
from editora as edi
left join endereco as ende
    on edi.endereco = ende.codendereco
left join livro as liv
    on edi.codeditora = liv.editora
where liv.editora > 0
group by liv.editora
order by quantidade desc