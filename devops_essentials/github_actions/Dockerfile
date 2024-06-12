FROM alpine:latest

RUN apk add --no-cache curl

COPY config.txt /app/config.txt

CMD ["echo", "Container setup complete. Use 'docker run <image> <command>' to execute additional commands."]
