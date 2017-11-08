PYTHON := python

.PHONY: test run clean clobber

test:
	$(PYTHON) -m unittest amazing_test

run: test
	$(PYTHON) amazing.py

clean:
	$(RM) *.pyc

clobber: clean

