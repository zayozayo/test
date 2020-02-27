FROM       python:3
LABEL      maintainer="Zahier <24963>"

RUN        pip install wikipedia


WORKDIR    /app
COPY       wikicrawler.py /app/
RUN        chmod a+x wikicrawler.py

ENTRYPOINT ["./wikicrawler.py"]
