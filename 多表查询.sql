CREATE DATABASE IF NOT EXISTS  sanguo CHARACTER SET utf8;
CREATE TABLE `t_dept` (
  `deptno` INT(11) NOT NULL,
  `dname` VARCHAR(20) DEFAULT NULL,
  `loc` VARCHAR(40) DEFAULT NULL,
  PRIMARY KEY (`deptno`),
  KEY `index_dept` (`deptno`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

INSERT INTO `t_dept` VALUES (10,'董事部','江东'),(20,'公关部','四川'),(30,'武统部','咸阳'),(40,'财务部','洛阳');

CREATE TABLE `t_employees` (
  `empno` INT(11) NOT NULL,
  `ename` VARCHAR(20) DEFAULT NULL,
  `job` VARCHAR(40) DEFAULT NULL,
  `MGR` INT(11) DEFAULT NULL,
  `hiredate` DATE DEFAULT NULL,
  `sal` DOUBLE(10,2) DEFAULT NULL,
  `comm` DOUBLE(10,2) DEFAULT NULL,
  `deptno` INT(11) DEFAULT NULL,
  PRIMARY KEY (`empno`),
  KEY `fk_deptno` (`deptno`),
  CONSTRAINT `fk_deptno` FOREIGN KEY (`deptno`) REFERENCES `t_dept` (`deptno`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

INSERT INTO `t_employees` VALUES (7369,'周瑜','高级公关',7566,'1981-03-21',2800.00,NULL,20),
(7499,'张飞','武装教习',7698,'1982-03-21',3600.00,300.00,30),
(7521,'关二爷','武装副司令',7698,'1983-03-21',3250.00,500.00,30),
(7566,'孙权','经理',7839,'1981-03-21',4975.00,NULL,10),
(7654,'黄忠','武装司令',7698,'1981-03-21',3250.00,1400.00,30),
(7698,'刘备','经理',7839,'1984-03-21',4850.00,NULL,10),
(7782,'曹操','经理',7839,'1985-03-21',4450.00,NULL,10),
(7788,'许褚','武装上将',7782,'1981-03-21',5000.00,NULL,30),
(7839,'汉献帝','董事长',NULL,'1981-03-21',7000.00,NULL,10),
(7844,'魏延','武装上将',7698,'1989-03-21',3500.00,0.00,30),
(7876,'黄盖','人事专员',7566,'1998-03-21',3100.00,NULL,20),
(7902,'荀彧','分析员',7782,'2005-03-12',5000.00,NULL,20),
(7934,'甘宁','中级公关',7782,'1981-03-21',3300.00,NULL,20),
(7952,'马超','武装大校',7698,'2001-03-21',3750.00,0.00,30),
(7953,'吕布','武装教习',7698,'2001-03-21',3750.00,0.00,30);



-- 10部门的地址和部门名称
SELECT dname,loc
FROM t_dept
-- 查询周瑜的部门编号
SELECT deptno 
FROM t_employees
WHERE ename ="周瑜"

-- 工作与吕布一样的其他人
SELECT job,ename
FROM t_employees
	WHERE job=(SELECT job
	FROM t_employees
	WHERE ename="吕布")

-- 工资超过2000的都查出来
SELECT *
FROM t_employees
WHERE sal>2000



-- 所有的员工跟上级姓名查出来
SELECT t1.ename,t2.ename
FROM t_employees t1,t_employees t2
WHERE t1.MGR=t2.empno

-- 1、查出至少有一个员工的部门。显示部门编号、部门名称、部门位置、部门人数。

SELECT t1.*,t2.部门人数
FROM t_dept t1,(SELECT deptno, COUNT(*) 部门人数 FROM t_employees GROUP BY deptno) t2
WHERE t1.deptno=t2.deptno


-- 2、列出所有员工的姓名及其直接上级的姓名。
SELECT t1.ename,t2.ename
FROM t_employees t1,t_employees t2
WHERE t1.MGR=t2.empno
/*
3. 列出受雇日期早于直接上级的所有员工的编号、姓名、部门名称。
列：e.empno, e.ename, d.dname
表：emp e, emp m, dept d
条件：e.hiredate<m.hiredate
思路：
1. 先不查部门名称，只查部门编号!
列：e.empno, e.ename, e.deptno
表：emp e, emp m
条件：e.mgr=m.empno, e.hiredate<m.hireadate
*/
SELECT t2.empno,t2.ename,t2.deptno
FROM t_employees t2,t_employees t3
WHERE t2.MGR=t3.empno AND t2.hiredate<t3.hiredate

SELECT t2.empno,t2.ename,t1.dname
FROM t_employees t2,t_employees t3,t_dept t1
WHERE t2.MGR=t3.empno AND t2.hiredate<t3.hiredate AND t2.deptno=t1.deptno



-- 4、列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门

SELECT *
FROM t_employees e RIGHT OUTER JOIN t_dept d
ON e.deptno=d.deptno

-- 5、列出最低薪金大于15000的各种工作及从事此工作的员工人数
SELECT job, COUNT(*)
FROM t_employees e
GROUP BY job
HAVING MIN(sal) > 15000

-- 6、列出在公关部工作的员工的姓名，假定不知道公关部的部门编号。

SELECT *
FROM t_employees t1
WHERE t1.deptno=(SELECT deptno FROM t_dept WHERE dname="公关部")



-- 7、列出薪金高于公司平均薪金的所有员工信息，所在部门名称，上级领导，         工资等级。

SELECT t1.*,t3.dname,t2.ename
FROM t_employees t1,t_employees t2,t_dept t3
WHERE t1.sal>(SELECT AVG(sal) FROM t_employees) AND t1.MGR=t2.empno AND t1.deptno=t3.deptno


-- 8、列出与张飞从事相同工作的所有员工及部门名称。
SELECT t1.*,t2.dname
FROM t_employees t1,t_dept t2
WHERE job=(SELECT job FROM t_employees WHERE ename="张飞") AND t1.deptno=t2.deptno


-- 9、列出薪金高于在部门30工作的所有员工的薪金的  员工姓名和薪金、部门名称
SELECT t1.ename,t1.sal,t2.dname
FROM t_employees t1,t_dept t2
WHERE sal > ALL (SELECT sal FROM t_employees WHERE deptno=30) AND t1.deptno=t2.deptno











