# Car selling platform project

### Business requirements: [BR](docs/BR.md)
### Technical Description: [TD](docs/TD.md)

Export to requirements.txt:
$`uv export --format requirements-txt > requirements.txt`

Get auth token:   
Please adjust host and port for local specifications

$`
curl -X 'POST' \
  'http://localhost:8010/api/login/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "admin",
  "password": "SuperUser"
}'
`   

Access endpoint with token:     
Please adjust host and port for local specifications    
PLease use the token acquired on previous step    

$`
curl -X 'GET' \
  'http://localhost:8010/api/cars/' \
  -H 'accept: application/json' \
  -H 'authorization: Token 543a1fe3f453d474d42979a01ce52579eee005f8'`    

Create a car:    
Please see notes above        
$`
curl -X 'POST' \
  'http://localhost:8010/api/car/create/' \
  -H 'accept: application/json' \
  -H 'authorization: Token 543a1fe3f453d474d42979a01ce52579eee005f8'\
  --json '{"owner": 1,"model": "Tesla 3","brand": "Tesla","year": 2001,"color": "Red","seats": 4,"type": "Sedan","price": 12000,"display":false,"publishing_date": "2024-12-05"}'
`   

--------------------
