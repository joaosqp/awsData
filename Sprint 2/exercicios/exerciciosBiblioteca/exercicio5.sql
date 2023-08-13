/* E5
Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil.
 Ordene o resultado pela coluna nome, em ordem crescente. 
Não podem haver nomes repetidos em seu retorno.*/

select 
    distinct aut.nome
    
from autor as aut
left join livro as liv
    on aut.codautor = liv.autor
left join editora as edi
    on liv.editora = edi.codeditora
left join endereco as ende
    on edi.endereco = ende.codendereco
where estado != "PARANÁ" and estado != "RIO GRANDE DO SUL"