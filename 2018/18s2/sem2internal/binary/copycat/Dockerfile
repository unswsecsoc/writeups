# Basic Xinetd Docker Container
# Useful for anyting binary / requiring netcat

FROM debian
MAINTAINER ctf@unswsecurity.com

# Apt-get update
RUN apt-get update

# Install xinetd
RUN apt-get install -y xinetd gcc make
RUN update-rc.d xinetd disable

# Install nc for debugging
RUN apt-get install -y netcat

# Add the ctf dir
RUN mkdir /home/ctf

RUN chmod 775 /home/ctf

# Add the ctf user
RUN useradd -M -U\
    -d /home/ctf \
    ctf

RUN chown ctf:ctf /home/ctf
WORKDIR /home/ctf

# Add the content
COPY Makefile .
COPY copycat.c .
COPY xinetd.conf /etc/xinetd.conf
COPY flag /home/ctf

# Make the binary
WORKDIR /home/ctf
RUN make clean \
    && make

# Expose the service port
EXPOSE 9091

# Clean up setup files
RUN ["chmod","775","copycat"]

CMD ["script", "-c", "xinetd -d -dontfork"]
