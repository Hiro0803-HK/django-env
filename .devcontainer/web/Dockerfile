FROM python:3.11

#to install pakages

RUN apt-get update -qq \
&&  apt-get install -y --no-install-recommends \
    tzdata sudo\
&&  rm -rf /var/lib/apt/lists/*


#to installing modules

WORKDIR /tmp/work

COPY requirements.txt ${PWD}

RUN pip install -U pip \
 && pip install -r requirements.txt

#Definition of environments

ENV TZ="Asia/Tokyo"

#Definition of local variables

ARG USERNAME=user1
ARG PASSWORD=user1
ARG GROUPNAME=user1
ARG UID=1000
ARG GID=1000

#add general auth user

RUN groupadd -g ${GID} ${GROUPNAME} \
 && useradd -u ${UID} -g ${GID} -G sudo -m -s /bin/bash ${USERNAME} \
 && echo ${USERNAME}:${PASSWORD} | chpasswd \
 && echo "%${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers


#changing user

USER ${USERNAME}