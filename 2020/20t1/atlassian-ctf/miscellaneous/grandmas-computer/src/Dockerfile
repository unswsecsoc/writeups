FROM ubuntu:18.04

RUN apt update && \
apt install -y sudo

COPY sudoers /etc/sudoers

RUN useradd -m ctf && \
usermod -a -G sudo ctf

WORKDIR /home/ctf
RUN chown -R root:root .

COPY flag.txt .
RUN chmod o-r flag.txt

RUN chmod 0000 /bin/bash && \
	chmod 0000 /bin/bunzip* && \
	chmod 0000 /bin/bz* && \
	chmod 0000 /bin/cp && \
	chmod 0000 /bin/chown && \
    chmod 0000 /bin/chgrp && \
    chmod 0000 /bin/cat && \
    chmod 0000 /bin/dd && \
    chmod 0000 /bin/dmesg && \
    chmod 0000 /bin/echo && \
    chmod 0000 /bin/grep && \
    chmod 0000 /bin/gunzip && \
    chmod 0000 /bin/gzexe && \
    chmod 0000 /bin/gzip && \
    chmod 0000 /bin/egrep && \
    chmod 0000 /bin/fgrep && \
    chmod 0000 /bin/ln && \
    chmod 0000 /bin/lsblk && \
    chmod 0000 /bin/mknod && \
    chmod 0000 /bin/mv && \
    chmod 0000 /bin/readlink && \
    chmod 0000 /bin/run-parts && \
    chmod 0000 /bin/sed && \
    chmod 0000 /bin/su && \
    chmod 0000 /bin/tar && \
    chmod 0000 /bin/uncompress && \
    chmod 0000 /bin/vdir && \
    chmod 0000 /bin/wdctl && \
    chmod 0000 /bin/z* && \
    chmod 0000 /usr/bin/* && \
    chmod 4755 /usr/bin/id && \
    chmod 4755 /usr/bin/sudo && \
    chmod -R 0000 /usr/sbin && \
    chmod 0000 /bin/chmod

USER ctf
ENTRYPOINT /bin/sh -i 2>&1
