FROM node:slim
MAINTAINER ctf@unswsecurity.com

RUN apt-get update && apt-get install -y xinetd netcat
RUN update-rc.d xinetd disable

# Add the ctf dir
RUN mkdir /home/ctf
WORKDIR /home/ctf
RUN chmod 775 /home/ctf

# Add the ctf user
RUN useradd -M -U\
    -d /home/ctf \
    ctf

RUN chown ctf:ctf /home/ctf

# Add the content
COPY xinetd.conf /etc/xinetd.conf
COPY level_3.js .

# Expose the service port
EXPOSE 9091

# Clean up setup files
RUN ["chmod","775","level_3.js"]

CMD ["script", "-c", "xinetd -d -dontfork"]
