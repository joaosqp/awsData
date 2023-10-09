SELECT decada, nome, quantidade
FROM (
  SELECT
    nome,
    FLOOR(ano/10)*10 AS decada,
    SUM(total) AS quantidade,
    ROW_NUMBER() OVER (PARTITION BY FLOOR(ano/10)*10 ORDER BY SUM(total) DESC) as rank
  FROM meubanco.dados
  WHERE ano >= 1950
  GROUP BY nome, FLOOR(ano/10)*10
) AS subquery
WHERE rank <= 3
ORDER BY decada ASC, quantidade DESC;
