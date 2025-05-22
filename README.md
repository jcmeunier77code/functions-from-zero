# functions-from-zero
live demo to build et deploy functions

[![Python application test with Github Actions](https://github.com/jcmeunier77code/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/jcmeunier77code/functions-from-zero/actions/workflows/main.yml)


### To call Microservice

Something like this 
```zsh
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```
