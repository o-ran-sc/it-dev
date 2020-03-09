################################################################################
#   Copyright (c) 2020 AT&T Intellectual Property.                             #
#                                                                              #
#   Licensed under the Apache License, Version 2.0 (the "License");            #
#   you may not use this file except in compliance with the License.           #
#   You may obtain a copy of the License at                                    #
#                                                                              #
#       http://www.apache.org/licenses/LICENSE-2.0                             #
#                                                                              #
#   Unless required by applicable law or agreed to in writing, software        #
#   distributed under the License is distributed on an "AS IS" BASIS,          #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
#   See the License for the specific language governing permissions and        #
#   limitations under the License.                                             #
################################################################################

FROM frolvlad/alpine-python3:latest as builder

LABEL name="Helm Manager"

ADD ./HelmManager /opt/HelmManager

RUN cd /opt/HelmManager && python3 setup.py sdist bdist_wheel


FROM frolvlad/alpine-python3:latest

ARG HELM_VERSION="2.12.3"

COPY --from=builder /opt/HelmManager/dist/*.gz .

RUN pip3 install *.gz && rm *.gz && ln -s $(pip show HelmManager | grep Location | awk '{printf  $2 "/HelmManager/HelmManager"}') /usr/local/bin/HelmManager && ln -s $(pip show HelmManager | grep Location | awk '{printf  $2 "/HelmManager/cli"}') /usr/local/bin/cli

RUN wget https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz && tar -xvf helm-v${HELM_VERSION}-linux-amd64.tar.gz && mv linux-amd64/helm /usr/local/bin/helm && rm -r linux-amd64 && rm helm-v${HELM_VERSION}-linux-amd64.tar.gz

ENTRYPOINT ["HelmManager"]
