

% http POST https://rqzhkvrwdc.execute-api.us-east-1.amazonaws.com/dev/metric/ox <<< '{"value": 42}'
HTTP/1.1 200 OK
Connection: keep-alive
Content-Encoding: gzip
Content-Length: 22
Content-Type: text/html; charset=utf-8
Date: Sat, 01 May 2021 22:59:40 GMT
Via: 1.1 542aa1c3fd7431ac31b596fde254f389.cloudfront.net (CloudFront)
X-Amz-Cf-Id: C3fM0fgTOdOgA6Fkt_eq03gY_Pfs79P5VRkB8Gv972E20PnBDE-6KQ==
X-Amz-Cf-Pop: EWR52-C1
X-Amzn-Trace-Id: Root=1-608ddd5c-19bd169b017eb5663b18bd0e;Sampled=0
X-Cache: Miss from cloudfront
x-amz-apigw-id: eq-GZFweoAMFjfA=
x-amzn-Remapped-Content-Length: 2
x-amzn-RequestId: 607ff54c-9a90-4b91-9158-cb50c3577b32

{}


% http https://rqzhkvrwdc.execute-api.us-east-1.amazonaws.com/dev/metric/ox/sum
HTTP/1.1 200 OK
Connection: keep-alive
Content-Encoding: gzip
Content-Length: 33
Content-Type: text/html; charset=utf-8
Date: Sat, 01 May 2021 22:59:46 GMT
Via: 1.1 d58537e312a32f11086af17e2a952efc.cloudfront.net (CloudFront)
X-Amz-Cf-Id: qJDsbaQ_v2Simfy5-Q76HUvwW_fOSknWlWEvJpXnufchQi3AzEk9Sg==
X-Amz-Cf-Pop: EWR52-C1
X-Amzn-Trace-Id: Root=1-608ddd62-1cd5bc153bc2c9b302736c52;Sampled=0
X-Cache: Miss from cloudfront
x-amz-apigw-id: eq-HVFBxoAMFsVA=
x-amzn-Remapped-Content-Length: 13
x-amzn-RequestId: cb84690d-42d9-487d-9480-a884e8322889

{
    "value": 42
}


% http https://rqzhkvrwdc.execute-api.us-east-1.amazonaws.com/dev/metric/ox/sum
HTTP/1.1 200 OK
Connection: keep-alive
Content-Encoding: gzip
Content-Length: 32
Content-Type: text/html; charset=utf-8
Date: Sat, 01 May 2021 23:00:02 GMT
Via: 1.1 30aeb6ef25a393db74fabfc78bbd79e3.cloudfront.net (CloudFront)
X-Amz-Cf-Id: 95JCUuEzWk1G26uL7SE8aXEcMrpDsKrYC-CCDQYkvoAprTJoY-FBTQ==
X-Amz-Cf-Pop: EWR52-C1
X-Amzn-Trace-Id: Root=1-608ddd72-79630209594adc657dabc7f4;Sampled=0
X-Cache: Miss from cloudfront
x-amz-apigw-id: eq-J1FIsIAMFZzA=
x-amzn-Remapped-Content-Length: 12
x-amzn-RequestId: 801b458f-13bd-4a32-a21f-926737b8f03f

{
    "value": 0
}


% http POST http://127.0.0.1:5000/metric/ox <<< '{"value": 42}'
HTTP/1.0 200 OK
Content-Length: 2
Content-Type: text/html; charset=utf-8
Date: Sat, 01 May 2021 23:01:07 GMT
Server: Werkzeug/0.16.1 Python/3.8.9

{}


% http http://127.0.0.1:5000/metric/ox/sum
HTTP/1.0 200 OK
Content-Length: 13
Content-Type: text/html; charset=utf-8
Date: Sat, 01 May 2021 23:01:14 GMT
Server: Werkzeug/0.16.1 Python/3.8.9

{
    "value": 42
}


% http http://127.0.0.1:5000/metric/ox/sum
HTTP/1.0 200 OK
Content-Length: 12
Content-Type: text/html; charset=utf-8
Date: Sat, 01 May 2021 23:01:40 GMT
Server: Werkzeug/0.16.1 Python/3.8.9

{
    "value": 0
}

