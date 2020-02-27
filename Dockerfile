FROM       python:3
LABEL      maintainer="Szzaza>"

RUN        pip install wikipedia
RUN        pip install requests
RUN        pip install sys


WORKDIR    /app
COPY       linkextractor.py /app/
RUN        chmod a+x linkextractor.py

ENTRYPOINT ["./linkextractor.py"]
