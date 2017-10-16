.PHONY: test run

test:
	cd ruby && $(MAKE) test
	cd java && $(MAKE) test

run:
	cd ruby && $(MAKE) run
	cd java && $(MAKE) run

