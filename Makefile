ifdef CIRCLECI
	RUN := pipenv run
else ifdef HEROKU_APP_NAME
	SKIP_INSTALL := true
else
	RUN := pipenv run
endif

.PHONY: all
all: install

.PHONY: ci
ci: check test ## CI | Run all validation targets

.PHONY: watch
watch: install ## CI | Rerun all validation targests in a loop
	@ rm -rf $(FAILURES)
	@ pipenv run pip install MacFSEvents > /dev/null
	$(RUN) sniffer

# SYSTEM DEPENDENCIES #########################################################

.PHONY: doctor
doctor: ## Check for required system dependencies
	bin/verchew

.envrc:
	echo export SECRET_KEY=local >> $@
	echo export DATABASE_URL=postgresql://localhost/artsinmotion_dev >> $@
	echo >> $@
	echo export TEST_EMAILS=you@yourdomain.com >> $@
	direnv allow

# PROJECT DEPENDENCIES ########################################################

BACKEND_DEPENDENCIES := tmp/.pipenv-$(shell bin/checksum Pipfile.lock)

.PHONY: install
ifndef SKIP_INSTALL
install: $(BACKEND_DEPENDENCIES) ## Install project dependencies
endif

$(BACKEND_DEPENDENCIES): Pipfile
	mkdir -p tmp
	pipenv install --dev
	@ touch $@

.PHONY: clean
clean:
	rm -rf staticfiles
	rm -rf .coverage htmlcov
	pipenv --rm

# RUNTIME DEPENDENCIES ########################################################

.PHONY: migrations
migrations: install  ## Database | Generate database migrations
	$(RUN) python manage.py makemigrations

.PHONY: migrate
migrate: install ## Database | Run database migrations
	$(RUN) python manage.py migrate

.PHONY: data
data: install migrate ## Database | Seed data for manual testing
	$(RUN) python manage.py gendata $(TEST_EMAILS)
	# TODO: Load test data and fixtures
	# $(RUN) python manage.py loaddata content

.PHONY: reset
reset: install ## Database | Create a new database, migrate, and seed it
	- dropdb artsinmotion_dev
	- createdb artsinmotion_dev
	make data

# VALIDATION TARGETS ##########################################################

PYTHON_PACKAGES := config portal

FAILURES := .cache/v/cache/lastfailed

ifdef DISABLE_COVERAGE
PYTEST_OPTIONS := --no-cov
endif

.PHONY: check
check: install ## Run static analysis
	$(RUN) pylint $(PYTHON_PACKAGES) tests --rcfile=.pylint.ini
	$(RUN) pycodestyle $(PYTHON_PACKAGES) tests --config=.pycodestyle.ini

.PHONY: test
test: test-all ## Run all tests

.PHONY: test-unit
test-unit: install
	@- mv $(FAILURES) $(FAILURES).bak
	$(RUN) py.test portal $(PYTEST_OPTIONS)
	@- mv $(FAILURES).bak $(FAILURES)
	$(RUN) coverage.space arts-in-motion/arts-in-motion unit

.PHONY: test-integration
test-integration: install
	@ if test -e $(FAILURES); then $(RUN) py.test tests/integration; fi
	@ rm -rf $(FAILURES)
	$(RUN) py.test tests/integration $(PYTEST_OPTIONS)
	$(RUN) coverage.space arts-in-motion/arts-in-motion integration

.PHONY: test-all
test-all: install
	@ if test -e $(FAILURES); then $(RUN) py.test $(PYTHON_PACKAGES) tests/integration; fi
	@ rm -rf $(FAILURES)
	$(RUN) py.test $(PYTHON_PACKAGES) tests/integration $(PYTEST_OPTIONS)
	$(RUN) coverage.space arts-in-motion/arts-in-motion overall

.PHONY: test-system
test-system: install
	$(RUN) honcho start --procfile=tests/system/Procfile --env=tests/system/.env

# SERVER TARGETS ##############################################################

.PHONY: run
run: install ## Run the applicaiton
	$(RUN) python manage.py runserver

.PHONY: run-prod
run-prod: .envrc install ## Run the application (simulate production)
	pipenv shell -c "bin/pre_compile; exit \$$?"
	pipenv shell -c "bin/post_compile; exit \$$?"
	pipenv shell -c "heroku local release; exit \$$?"
	pipenv shell -c "heroku local web; exit \$$?"

# RELEASE TARGETS #############################################################

.PHONY: promote
promote: install
	SITE=https://staging.portal.com $(RUN) pytest tests/system
	heroku pipelines:promote --app portal-staging --to portal
	# TODO: Update system tests so they can run against production
	# Should have a specific test user name?
	SITE=https://portal.com $(RUN) pytest tests/system

# HELP ########################################################################

.PHONY: help
help: all
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
