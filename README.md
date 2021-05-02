# Transport Take Home Exercise

Code submission per the document Transport "Take Home Exercise (1).pdf"

Built, tested, and deployed using `python 3.8.9`.

Built and tested using `flask` and `pytest`.

Deployed using `zappa`:

https://github.com/zappa/Zappa

using `aws lambda`, `api gateway`, and `s3`:

https://rqzhkvrwdc.execute-api.us-east-1.amazonaws.com/dev/metric/ox/sum

## Example deployed calls:

[ ** deployed time limit set to 20 seconds instead of 1 hour in .env ]

[ ** using httpie ] 

```
% http -v POST https://rqzhkvrwdc.execute-api.us-east-1.amazonaws.com/dev/metric/ox <<< '{"value": 42}'
POST /dev/metric/ox HTTP/1.1
....

{
    "value": 42
}


HTTP/1.1 200 OK
....

{}
```

### Less than 20 seconds later:

```
% http -v https://rqzhkvrwdc.execute-api.us-east-1.amazonaws.com/dev/metric/ox/sum          
GET /dev/metric/ox/sum HTTP/1.1
....

HTTP/1.1 200 OK
....

{
    "value": 42
}
```

### More than 20 seconds later:

```
% http -v https://rqzhkvrwdc.execute-api.us-east-1.amazonaws.com/dev/metric/ox/sum
GET /dev/metric/ox/sum HTTP/1.1
....

HTTP/1.1 200 OK
....

{
    "value": 0
}
```
----

# Local Workspace

To setup your local workspace:

```
% git clone https://github.com/oxbits/example_transport_code.git

% pyenv install 3.8.9 # you may have to install this python version

% pyenv local 3.8.9

% pip install virtualenv # you may have to install virtualenv for this python version

% virtualenv -p python fenv

% source ./fenv/bin/activate

% cd example_transport_code

% pip install -r requirements.txt

% pytest

% flask run
```

### .env File Configuration:

```
CACHE_MICROSECONDS=360_000_000 # 1 hour in microseconds
USE_S3=false # when set to false uses local files
S3_BUCKET=YOUR_S3_BUCKET_NAME
```

## Example local workspace calls:

[ ** .env time limit in repo set to 1 hour ]

[ ** time limit set to 20 seconds instead of 1 hour for below examples ]

[ ** using httpie ]

```
% http -v POST http://127.0.0.1:5000/metric/ox <<< '{"value": 42}'
POST /metric/ox HTTP/1.1
....

{
    "value": 42
}


HTTP/1.0 200 OK
....

{}
```

### Less than .env microseconds limit:

```
% http -v http://127.0.0.1:5000/metric/ox/sum
GET /metric/ox/sum HTTP/1.1
....

HTTP/1.0 200 OK
....

{
    "value": 42
}
```

### More than .env microseconds limit:

```
% http -v http://127.0.0.1:5000/metric/ox/sum
GET /metric/ox/sum HTTP/1.1
....

HTTP/1.0 200 OK
....

{
    "value": 0
}
```
