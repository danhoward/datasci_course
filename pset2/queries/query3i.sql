/*


*/

CREATE VIEW query AS
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

CREATE VIEW data AS
SELECT * FROM Frequency;

SELECT data.docid, query.count * data.count
FROM data, query
WHERE data.term = query.term
ORDER BY data.count DESC
LIMIT 1;


/*
SELECT doc_a.term, doc_b.term, doc_a.count * doc_b.count AS product
FROM doc_a, doc_b
WHERE doc_a.term = doc_b.term AND doc_a.docid < doc_b.docid
GROUP BY doc_a.term, doc_b.term;

SELECT doc_a.docid, doc_b.docid, SUM(doc_a.count * doc_b.count)
FROM doc_a
JOIN doc_b
ON doc_a.term=doc_b.term;




SELECT A.row_num, B.col_num, SUM(A.value * B.value)
FROM A, B
WHERE a.col_num = b.row_num
GROUP BY a.row_num, b.col_num;

*/
