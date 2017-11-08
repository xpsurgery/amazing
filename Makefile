LANGUAGES := $(shell ls -d [a-z]* )

.PHONY: clean test $(LANGUAGES)

default: test

test: $(LANGUAGES)

$(LANGUAGES):
	$(MAKE) -C $@ test

clean:
	-for d in $(LANGUAGES); do $(MAKE) -C $$d clean; done

