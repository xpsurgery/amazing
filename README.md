# The Amazing Maze Refactoring Challenge

This source code provides a refactoring challenge. It contains several versions of the same program, converted into a
variety of different languages.

1. Pick one of the languages and ensure you can get the tests passing.  (You can also run the program from the command line via the Makefile, to get an idea of the kind of mazes it generates.)
2. Refactor the code until you can find a good name for the variable `q`. Be careful to keep the tests passing at all times!
3. The code contains at least one bug. Did you spot it while refactoring? Can you fix it (test-first, of course)?
4. Think about your refactoring strategy. Do you use particular moves at certain times in the process?  Looking back over the whole process, could you describe a refactoring plan for this code to someone else?
5. Can you describe the maze-building algorithm used? Can you refactor the code so that some part of it expresses this algorithm? Could you use most of this code to implement one or more alternative algorithms without too much rewriting?

## Makefiles

Several `make` targets are provided in the top level and also in each language directory:

* `make test`\
  Run the tests for all language variants.  Build whatever is necessary first.
* `make run`\
  Run all language variants. By default these generate mazes with 10 rows and 10 columns; this can be overridden by passing envinoment variables as follows:
  ```
  cols=4 rows=5 make run
  ```
* `make clean`\
  Remove intermediate compilation targets, if any.
* `make clobber`\
  Remove all built artefacts, if any.

## Credits

* The original program is by Jack Hauber, and the source is "Basic Computer Games." Used with permission of [David Ahl](www.SwapMeetDave.com)
* This exercise was inspired by Alan Hensel's use of [Amazing as a refactoring challenge](https://web.archive.org/web/20080513210558/http://www.mindspring.com/~alanh/refactoring/challenge.html)
* The transliteration to Java is based on one created by [Bill Wake](http://xp123.com).

