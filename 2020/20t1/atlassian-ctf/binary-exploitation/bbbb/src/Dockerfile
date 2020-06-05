FROM ubuntu:18.04

RUN dpkg --add-architecture i386
RUN apt-get update && \
  apt-get install --allow-change-held-packages --allow-downgrades -y \
    libc6 libc-bin sudo socat libc6-i386 && \
  rm -rf /var/lib/apt/lists/*

RUN useradd -m ctf
WORKDIR /home/ctf/
COPY bbbb_actually_final flag /home/ctf/
RUN chown -R root:root . && chmod +x bbbb_actually_final

ENV TIMEOUT=300
EXPOSE 5555/tcp
USER ctf
ENTRYPOINT socat TCP-LISTEN:5555,reuseaddr,fork EXEC:"timeout $TIMEOUT ./bbbb_actually_final"