JFLAGS = -g
JAVAC = javac

.SUFFIXES: .java .class

.java.class:
	$(JAVAC) $(JFLAGS) $*.java

.PHONY: test run

test: Amazing.class TestAmazing.class

run: test
	java Amazing 10 10

clean:
	$(RM) *.class

