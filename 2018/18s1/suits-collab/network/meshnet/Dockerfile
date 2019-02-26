FROM debian
MAINTAINER ctf@unswsecurity.com

RUN apt-get update

# Install xinetd
RUN apt-get install -y xinetd
RUN update-rc.d xinetd disable

# Install nc for debugging
RUN apt-get install -y netcat

# Install cjdns build deps
RUN apt-get install -y build-essential wget python

# Download cjdns
RUN \
  mkdir -p /usr/src && \
  cd /usr/src && \
  wget https://github.com/cjdelisle/cjdns/archive/cjdns-v20.1.tar.gz && \
  tar xzf cjdns-v20.1.tar.gz

# Build cjdns
RUN cd /usr/src/cjdns-cjdns-v20.1 && ./do

# Install cjdns
RUN install -m755 /usr/src/cjdns-cjdns-v20.1/cjdroute /usr/bin/cjdroute
RUN mkdir -p /etc/cjdns

# Clean up
RUN { \
  rm -rf /usr/src; \
  apt-get remove -y build-essential wget python; \
  apt-get autoremove; \
  apt-get clean; \
}

# Add the content
COPY entry.sh /entry.sh
COPY xinetd.conf /etc/xinetd.conf
COPY flag /flag

VOLUME /etc/cjdns

ENTRYPOINT [ "/bin/bash", "/entry.sh" ]
