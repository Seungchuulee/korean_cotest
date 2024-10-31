SELECT
    CASE
        WHEN price then FLOOR(price/10000) * 10000
    END as PRICE_GROUP,
    count(*) as PRODUCTS
FROM
    product
GROUP BY
    1
ORDER BY
    1