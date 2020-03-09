FROM alpine:latest as builder
MAINTAINER "Zhe Huang <zhehuang@research.att.com>"

LABEL name="Helm Manager"

RUN apk update && apk add --no-cache python3 && pip3 install --upgrade pip setuptools wheel

ADD ./ /opt/HelmManager

RUN cd /opt/HelmManager && python3 setup.py sdist bdist_wheel


FROM alpine:latest

ARG HELM_VERSION="2.12.3"

RUN apk update && apk add --no-cache python3 && pip3 install --upgrade pip

COPY --from=builder /opt/HelmManager/dist/*.gz .

RUN pip3 install *.gz && rm *.gz && ln -s $(pip show HelmManager | grep Location | awk '{printf  $2 "/HelmManager/HelmManager"}') /usr/local/bin/HelmManager && ln -s $(pip show HelmManager | grep Location | awk '{printf  $2 "/HelmManager/cli"}') /usr/local/bin/cli

RUN wget https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz && tar -xvf helm-v${HELM_VERSION}-linux-amd64.tar.gz && mv linux-amd64/helm /usr/local/bin/helm && rm -r linux-amd64 && rm helm-v${HELM_VERSION}-linux-amd64.tar.gz

ENTRYPOINT ["HelmManager"]
