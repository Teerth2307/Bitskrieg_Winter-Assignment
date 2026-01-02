FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat gcc libc6-dbg gdb libseccomp-dev

WORKDIR /app

COPY noteapp.c .
COPY flag.txt .


RUN gcc -g -no-pie -o noteapp noteapp.c -lseccomp

RUN chmod +x noteapp

EXPOSE 1337

CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:./noteapp"]
