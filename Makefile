ROOT=$(CURDIR)

DOCKER_PATH=$(ROOT)/ops/docker
BASE_PATH=$(DOCKER_PATH)/app-base
DEV_PATH=$(DOCKER_PATH)/app-dev

install-base:
	@./bin/install $(BASE_PATH)

install-dev: install-base
	@./bin/install $(DEV_PATH)

bash:
	@docker run -i -t --rm $(DOCKER_TAG) /bin/bash

.PONY: bash
