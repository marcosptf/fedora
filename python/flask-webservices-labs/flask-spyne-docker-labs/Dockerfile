FROM fedora:latest
#MAINTAINER marcosptf "marcosptf@yahoo.com.br"
RUN dnf install -y git python2 vim gcc libxml libxml2 python2 python2-virtualenv redhat-rpm-config elinks htop
COPY . /app
WORKDIR /app
RUN pip install -r requirements-spyne.txt
ENTRYPOINT ["python"]
CMD ["server.py"]
