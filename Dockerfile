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

# define entrypoint
ENTRYPOINT ["/sbin/tini", "--"]

# run gunicorn-skeleton
CMD ["gunicorn", "--config", "configs/gunicorn.py", "gunicornskeleton"]
