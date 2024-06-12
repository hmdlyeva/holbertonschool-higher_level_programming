FROM alpine:latest

RUN apk add --no-cache curl

COPY config.txt /app/config.txt

VOLUME /data

CMD ["sh", "-c", "echo 'Container started. Use docker exec -it <container_id> /bin/sh to interact.'"]
