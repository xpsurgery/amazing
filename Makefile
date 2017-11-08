LANGUAGES := $(shell ls -d [a-z]* )

.PHONY: clean clobber run test $(LANGUAGES)

default: test

test: $(LANGUAGES)

$(LANGUAGES):
	$(MAKE) -C $@ test

run:
	-for d in $(LANGUAGES); do $(MAKE) -C $$d run; done

clean:
	-for d in $(LANGUAGES); do $(MAKE) -C $$d clean; done

clobber:
	-for d in $(LANGUAGES); do $(MAKE) -C $$d clobber; done

