#!/bin/bash

docker image rm -f emergyyy:latest
docker build --no-cache -t emergyyy:latest .
docker run -it --env-file src/.env --rm --network anymus-mail-net emergyyy:latest