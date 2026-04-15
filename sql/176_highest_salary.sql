SELECT
(SELECT Distinct salary as "SecondHighestSalary"
FROM Employee
ORDER BY salary DESC
OFFSET 1 LIMIT 1)