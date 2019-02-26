FROM python:3.6-alpine3.7

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories

RUN \
 echo "**** install build packages ****" && \
 apk add --no-cache --virtual=build-dependencies \
	autoconf \
	automake \
	freetype-dev \
	g++ \
	gcc \
	jpeg-dev \
	lcms2-dev \
	libffi-dev \
	libpng-dev \
	libwebp-dev \
	linux-headers \
	make \
	openjpeg-dev \
	openssl-dev \
	python3-dev \
	tiff-dev \ 
	zlib-dev && \
 echo "**** install runtime packages ****" && \
 apk add --no-cache \
	curl \
	freetype \
	git \
	lcms2 \
	libjpeg-turbo \
	libwebp \
	openjpeg \
	openssl \
	p7zip \
	py3-lxml \
	python3 \
	tar \
	tiff \
	unrar \
	unzip \
	vnstat \
	wget \
	xz \
	zlib && \
 echo "**** use ensure to check for pip and link /usr/bin/pip3 to /usr/bin/pip ****" && \
 python3 -m ensurepip && \
 rm -r /usr/lib/python*/ensurepip && \
 if \
	[ ! -e /usr/bin/pip ]; then \
	ln -s /usr/bin/pip3 /usr/bin/pip ; fi && \
 echo "**** install pip packages ****" && \
 pip install --no-cache-dir -U \
	pip \
	setuptools && \
 pip install --no-cache-dir -U \
	configparser \
    dumb-init \
	ndg-httpsclient \
	notify \
	paramiko \
	pillow \
	psutil \
	pyopenssl \
	requests \
	setuptools \
	urllib3 \
	virtualenv && \
 echo "**** clean up ****" && \
 apk del --purge \
	build-dependencies && \
 rm -rf \
	/root/.cache \
	/tmp/*

# install chromedriver
RUN apk update
RUN apk add --no-cache \
    uwsgi-python3

COPY uwsgi.ini /etc/uwsgi/uwsgi.ini

ENV UWSGI_INI /app/uwsgi.ini

EXPOSE 80

COPY app/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY app /app

ENV SENDER_EMAIL "password.recovery@unswsecurity.com"
ENV SENDER_PASSWORD "2dac52b2e22f23ed7543388441c286f8971bfcaeccf10e4a46f0858a4f8a4176"

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

CMD ["uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini", \
              "--die-on-term"]


