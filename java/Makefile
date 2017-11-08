JFLAGS    := -g
JAVA      := java
JAVAC     := javac
CLASSPATH := -classpath .:junit-4.12.jar:hamcrest-core-1.3.jar

.SUFFIXES: .java .class

.java.class:
	$(JAVAC) $(JFLAGS) $(CLASSPATH) $*.java

.PHONY: test run clean clobber

test: Amazing.class TestAmazing.class
	$(JAVA) $(CLASSPATH) org.junit.runner.JUnitCore TestAmazing

run: test
	java Amazing 10 10

clean:
	$(RM) *.class

clobber: clean

