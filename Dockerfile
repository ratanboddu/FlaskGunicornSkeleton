FROM python:3.6

# copy source code
ADD . /gunicorn-skeleton

# configure pip
ENV PIP_CONFIG_FILE /gunicorn-skeleton/pip.conf

# create symlink to /usr/local/opt/gunicorn-skeleton
RUN mkdir -p /usr/local/opt
RUN ln -s /gunicorn-skeleton /usr/local/opt/

# install backend
RUN pip install /gunicorn-skeleton

# define volumes
VOLUME /gunicorn-skeleton/configs

# define working directory
WORKDIR /gunicorn-skeleton

# install tini
ADD https://github.com/krallin/tini/releases/download/v0.18.0/tini /usr/local/bin/tini
RUN chmod +x /usr/local/bin/tini

# define entrypoint
ENTRYPOINT ["tini", "--"]

# run gunicorn-skeleton
CMD ["gunicorn", "--config", "configs/gunicorn.py", "gunicornskeleton"]
