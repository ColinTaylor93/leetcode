SELECT name as "Employee"
FROM Employee as e1
WHERE (SELECT salary FROM Employee as e2 WHERE e1.managerId = e2.id) < e1.salary