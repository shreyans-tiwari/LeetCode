/*
Write an SQL query to find the employees who earn more than their managers.
Return the result table in any order.
*/

# Solution
SELECT a.name AS Employee
FROM Employee AS a, Employee AS b
WHERE a.managerId = b.id AND a.salary > b.salary;
