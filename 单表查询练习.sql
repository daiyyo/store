
SELECT * FROM t_employees
WHERE deptno=30

所有销售员的姓名、编号和部门编号。
SELECT ename 姓名,empno 编号,deptno 部门编号 FROM t_employees
WHERE job="salesman"

找出奖金高于工资的员工
SELECT * FROM t_employees
WHERE comm>sal

找出奖金高于工资60%的员工
SELECT * FROM t_employees
WHERE comm>sal*0.6

找出部门编号为10中所有经理，和部门编号为30中所有销售员的详细资料。
SELECT * FROM t_employees
WHERE (deptno =10 AND job="manager") OR (deptno =30 AND job="salesman")


找出部门编号为10中所有经理，部门编号为20中所有销售员，还有即不是经理又不是销售员但其工资大或等于20000的所有员工详细资料。
SELECT * FROM t_employees
WHERE (deptno=10 AND job="manager") OR (deptno=30 AND job="salesman") OR (job NOT IN("manager","salesman") AND sal >=2000)

无奖金或奖金低于1000的员工
SELECT * FROM t_employees
WHERE comm IS NULL OR comm<1000

查询名字由三个字组成的员工
SELECT * FROM t_employees
WHERE ename LIKE"___"

查询2000年入职的员工
SELECT * FROM t_employees
WHERE hiredate LIKE"2000_%"

查询所有员工详细信息，用编号升序排序
SELECT * FROM t_employees
ORDER BY empno

查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
SELECT * FROM t_employees
ORDER BY sal DESC,hiredate ASC

查询每个部门的平均工资
SELECT AVG(sal) 部门平均工资 FROM t_employees
GROUP BY deptno

查询每个部门的雇员数量
SELECT COUNT(empno) FROM t_employees
GROUP BY deptno

查询每种工作的最高工资、最低工资、人数
SELECT job,MAX(sal) 最高工资,MIN(sal) 最低工资,COUNT(empno)人数 FROM t_employees
GROUP BY job
