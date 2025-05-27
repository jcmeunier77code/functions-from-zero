# functions-from-zero
live demo to build et deploy functions

[![Python application test with Github Actions](https://github.com/jcmeunier77code/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/jcmeunier77code/functions-from-zero/actions/workflows/main.yml)


## To call Microservice

Something like this 
```zsh
curl -X 'POST' \
  'http://localhost:8080/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

## Containerize project 

### Build container 

```zsh
docker build .  # alternatively with image image name and version : docker build -t ffz-app:v1.0 .
docker image ls
```

### Run container 

```zsh
docker run -p 127.0.0.1:8080:8080 ffz-app:v1.0
```

### Invoke 

run 'invoke.sh'


