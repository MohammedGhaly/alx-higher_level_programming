# Network #0

# Learning Objectives

- What a URL is
- What HTTP is
- How to read a URL
- The scheme for a HTTP URL
- What a domain name is
- What a sub-domain is
- How to define a port number in a URL
- What a query string is
- What an HTTP request is
- What an HTTP response is
- What HTTP headers are
- What the HTTP message body is
- What an HTTP request method is
- What an HTTP response status code is
- What an HTTP Cookie is
- How to make a request with cURL
- What happens when you type google.com in your browser (Application level)

# Tasks

## cURL body size

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

- The size must be displayed in bytes
- You have to use `curl`

**Solution:** [0-body_size.sh](./0-body_size.sh)

```
$ ./0-body_size.sh 0.0.0.0:5000
10
$
```

## cURL to the end

Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

- Display only body of a 200 status code response
- You have to use `curl`

**Solution:** [1-body.sh](./1-body.sh)

```
$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
$
```

## cURL Method

Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

- You have to use `curl`

**Solution:** [2-delete.sh](./2-delete.sh)

```
$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
$
```

## cURL only methods

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

- You have to use `curl`

**Solution:** [3-methods.sh](./3-methods.sh)

```
$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
$
```

## cURL headers

Write a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response

- A header variable `X-HolbertonSchool-User-Id` must be sent with the value `98`
- You have to use `curl`

**Solution:** [4-header.sh](./4-header.sh)

```
$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello Holberton School!
$
```

## cURL POST parameters

Write a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response

- A variable `email` must be sent with the value `hr@holbertonschool.com`
- A variable `subject` must be sent with the value `I will always be here for PLD`
- You have to use `curl`

**Solution:** [5-post_params.sh](./5-post_params.sh)

```
$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: hr@holbertonschool.com
    subject: I will always be here for PLD
$
```
