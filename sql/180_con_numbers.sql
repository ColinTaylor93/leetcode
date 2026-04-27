SELECT DISTINCT num AS ConsecutiveNums
FROM (
    -- subqery to get num followed by next 2
    SELECT 
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS nextNum,
        LEAD(num, 2) OVER (ORDER BY id) AS NextNextNum
    FROM Logs
) AS Subquery
WHERE num = nextNum AND num = NextNextNum;