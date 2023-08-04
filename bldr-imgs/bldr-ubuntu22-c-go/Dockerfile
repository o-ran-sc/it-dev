# O-RAN-SC
#
# Copyright (C) 2019-2020 AT&T Intellectual Property and Nokia
# Copyright (C) 2023 Abhijit Gadgil.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Builder image with superset of CI tools for RIC components

FROM nexus3.o-ran-sc.org:10001/ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    alien \
    autoconf \
    autoconf-archive \
    automake \
    autotools-dev \
    build-essential \
    cmake \
    g++  \
    gcc \
    git \
    ksh \
    libbz2-dev \
    libicu-dev \
    libsctp-dev \
    libtool \
    lksctp-tools \
    make \
    python3-dev \
    pkg-config \
    software-properties-common \
    sudo \
    wget \
    zlib1g \
    zlib1g-dev \
    zip \
    libboost-all-dev

WORKDIR /tmp

# Install go versions in /opt
RUN mkdir -p /opt/go


ARG g18="1.18.10"
RUN wget -nv https://dl.google.com/go/go${g18}.linux-amd64.tar.gz \
    && tar -xf go${g18}.linux-amd64.tar.gz \
    && mv go /opt/go/1.18 \
    && rm -f go*.gz

ARG g19="1.19.12"
RUN wget -nv https://dl.google.com/go/go${g19}.linux-amd64.tar.gz \
    && tar -xf go${g19}.linux-amd64.tar.gz \
    && mv go /opt/go/1.19 \
    && rm -f go*.gz

ARG g20="1.20.7"
RUN wget -nv https://dl.google.com/go/go${g20}.linux-amd64.tar.gz \
    && tar -xf go${g20}.linux-amd64.tar.gz \
    && mv go /opt/go/1.20 \
    && rm -f go*.gz

# Use /opt/go/1.18/bin for version 1.18.x (default)
ARG GOVERSION=1.18
ENV GOPATH=/root/go
ENV DEFAULTPATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV PATH=$DEFAULTPATH:/usr/local/go/bin:/opt/go/${GOVERSION}/bin:$GOPATH/bin

# This installs go-acc to GOPATH
RUN go version; \
    export GOBIN=/usr/local/bin/; export GO111MODULE=on;\
    go install github.com/ory/go-acc@master \
    && go-acc --help


# sonar-scanner is not available in ubuntu repo
ARG sv="4.8.0.2856"
RUN wget -nv https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${sv}-linux.zip \
    && unzip sonar-scanner-cli-${sv}-linux.zip \
    && mv sonar-scanner-${sv}-linux /usr/local/sonar-scanner \
    && rm -f sonar*.zip

# golangci-lint is not available in ubuntu repo
RUN wget -O- -nv https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $GOPATH/bin v1.53.3 \
    && rm -f install.sh
