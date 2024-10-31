SELECT A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(SALES*PRICE) AS TOTAL_SALES
FROM BOOK_SALES S
JOIN BOOK B 
ON S.BOOK_ID = B.BOOK_ID -- SALES + 도서 정보
JOIN AUTHOR A
ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE YEAR(SALES_DATE) = '2022' AND MONTH(SALES_DATE) = '1'
GROUP BY B.AUTHOR_ID, B.CATEGORY
ORDER BY A.AUTHOR_ID ASC, B.CATEGORY DESC