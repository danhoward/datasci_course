SELECT A.row_num, B.col_num, SUM(A.value * B.value)
FROM A, B
WHERE a.col_num = b.row_num
GROUP BY a.row_num, b.col_num;
