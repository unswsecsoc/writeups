# Basic Xinetd Docker Container
# Useful for anyting binary / requiring netcat

FROM debian
MAINTAINER ctf@unswsecurity.com

# Apt-get update
RUN apt-get update

# Install xinetd
RUN apt-get install -y xinetd
RUN update-rc.d xinetd disable

# Add the ctf dir
RUN mkdir /home/ctf

RUN chmod 775 /home/ctf

# Add the ctf user
RUN useradd -M -U\
    -d /home/ctf \
    ctf

RUN chown ctf:ctf /home/ctf

# Add the content
#ADD content/* /home/ctf/
COPY xinetd.conf /etc/xinetd.conf

# Make the binary
#WORKDIR /home/ctf
#RUN make clean && make

# Copy the binary over
COPY nethackers /home/ctf

ENV FLAG=flag{muahaha_not_the_real_amulet}

# Expose the service port
EXPOSE 9091

# Clean up setup files
#RUN ["rm","/home/ctf/Makefile", "/home/ctf/whropper.c"]
#RUN ["chmod","775","/flag"]
RUN ["chmod","775","/home/ctf/nethackers"]

CMD ["script", "-c", "xinetd -d -dontfork"]
