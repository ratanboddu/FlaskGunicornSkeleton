.PHONY: clean pip db bucket install lint run test celery-worker minio-server keycloak-gatekeeper swagger-ui gunicorn

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ -delete
	rm -rf *.egg-info

pip:
	PIP_CONFIG_FILE=$(PWD)/pip.conf \
	pip install -e .
	PIP_CONFIG_FILE=$(PWD)/pip.conf \
	pip install pytest pytest-cov black importanize pre-commit


install: pip
	pre-commit install

run:
	CONFIG_SETTINGS=$(PWD)/configs/local.ini FLASK_APP=gunicornskeleton \
	FLASK_DEBUG=0 \
	flask run

docker:
	docker build -t  myrepo/myapplication .
	docker push myrepo/myapplication
