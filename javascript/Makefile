NODE_MODULES := node_modules

.PHONY: test run clean clobber

test: $(NODE_MODULES)
	env | sort
	npm run test

run: test
	node amazing.js

$(NODE_MODULES):
	npm install

clean:

clobber: clean
	$(RM) -r $(NODE_MODULES)

