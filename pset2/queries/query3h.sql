/*CREATE VIEW doc_a AS
SELECT * FROM Frequency 
WHERE docid = '10080_txt_crude';

CREATE VIEW doc_b AS
SELECT * FROM Frequency
WHERE docid = '17035_txt_earn'; 

SELECT doc_a.term, doc_b.term, doc_a.count * doc_b.count AS product
FROM doc_a, doc_b
WHERE doc_a.term = doc_b.term AND doc_a.docid < doc_b.docid
GROUP BY doc_a.term, doc_b.term;
*/

SELECT doc_a.docid, doc_b.docid, SUM(doc_a.count * doc_b.count)
FROM doc_a
JOIN doc_b
ON doc_a.term=doc_b.term;



/*
1) Generate view of the two docs together
2) Generate the transform (TRIVIAL join on columns to columns rather than to rows
3) Compute overlap?




SELECT A.row_num, B.col_num, SUM(A.value * B.value)
FROM A, B
WHERE a.col_num = b.row_num
GROUP BY a.row_num, b.col_num;




need to find "similarity matrix" for the above views: can do this via join on column for term?s */
