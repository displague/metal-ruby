.PHONY: all gen patch fetch

SPEC_URL:=https://api.equinix.com/metal/v1/api-docs
SPEC_FETCHED_FILE:=fetched.openapi.yaml
SPEC_PATCHED_FILE:=patched.openapi.yaml
IMAGE=openapitools/openapi-generator-cli
GIT_ORG=displague
GIT_REPO=metal-python
PACKAGE_NAME=metal
# python-flask python-legacy python python-aiohttp python-blueplanet
GENERATOR=python

SWAGGER=docker run --rm -v $(CURDIR):/local ${IMAGE}

all: pull fetch patch gen

pull:
	docker pull ${IMAGE}

fetch:
	curl -o ${SPEC_FETCHED_FILE} ${SPEC_URL}

patch:
	# patch is idempotent, always starting with the fetched
	# fetched file to create the patched file.
	ARGS="-o ${SPEC_PATCHED_FILE} ${SPEC_FETCHED_FILE}"; \
	for diff in $(shell find patches/*.patch | sort -n); do \
		patch --no-backup-if-mismatch -N -t $$ARGS $$diff; \
		ARGS=${SPEC_PATCHED_FILE}; \
	done

gen:
	${SWAGGER} generate -g ${GENERATOR} \
		--package-name ${PACKAGE_NAME} \
		--model-package types \
		--api-package models \
		--git-user-id ${GIT_ORG} \
		--git-repo-id ${GIT_REPO} \
		-o /local/${PACKAGE_NAME} \
		-i /local/${SPEC_PATCHED_FILE}
