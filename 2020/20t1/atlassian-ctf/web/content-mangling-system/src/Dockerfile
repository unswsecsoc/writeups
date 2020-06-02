FROM python:3.7-alpine as base


FROM base as build

RUN apk update && apk add --no-cache sqlite python3-dev libffi-dev gcc musl-dev make

RUN mkdir /build
WORKDIR /build

COPY requirements.txt /tmp/requirements.txt
RUN pip install --prefix=/build -r /tmp/requirements.txt

COPY meta/cms.sql /tmp/cms.sql
RUN sqlite3 /cms.db < /tmp/cms.sql


FROM base as dist

COPY ./src/ /app/
COPY ./meta/flag /flag
COPY ./entrypoint.sh /entrypoint.sh

COPY --from=build /build /usr/local
COPY --from=build /cms.db /app/cms.db

RUN addgroup -S ctf && adduser -S ctf -G ctf
RUN chmod 005 -R /app /entrypoint.sh && chmod 700 /app/cms.db /app && chown ctf.ctf /app /app/cms.db

USER ctf
WORKDIR /app
EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
CMD ["webapp"]
