# PSYC161 Homework #1

This homework is a part of the
[PSYC161 Introduction to Programming for Psychologists & Neuroscientists](https://github.com/dartmouth-pbs/psyc161)
course work.

## Ultimate goal

On the example of a simple Python script/function establish
practice of

- interaction with [Git](http://git-scm.com) and [GitHub](http://github.com)
- automated testing using [nose](https://nose.readthedocs.org)
- code syntax conventions validation using [flake8](http://bitbucket.org/tarek/flake8)

## Problem to solve

We are creating a new design for an fMRI experiment, for which we will
have a single trial per each of `n` different independent conditions per
run.

**Question**: *how many possible trial orders there could possibly be?*

**Approach**: estimate the factorial of `n`

**Solution**:

1. Write recursive `factorial_recursive` to estimate factorial of an
   integer n.
   See [wikipedia](http://en.wikipedia.org/wiki/Factorial) if not sure
   about what factorial is

### "Extra credit"

2. Write non-recursive version of a `factorial` function

3. Investigate difference (well - ratio) in time of execution between
   the two.  Use `time` module to track time.

## HOWTO

- "Fork" (which is really just a GitHub term for "clone" on GitHub
  site, no "git clone" to be done to local drive), this repository on
  GitHub

- In the terminal now run

        git clone https://github.com/YOURLOGIN/psyc161-hw1

    to "clone" your remote fork/clone to your local drive

- Edit file `factorial.py` which provides a skeleton for your work

- You are welcome to use any editor to edit the file, but we recommend
  starting to work with [PyCharm](https://www.jetbrains.com/pycharm)

- Function `factorial_recursive` definition provides a skeleton for
  you to fill in (docstring + implementation)

- Test `test_factorial()` implements basic checks already which you
  need to expand to degree you feel necessary to state with assurance
  that your implementation.  You can run all `tests_` present in the
  file using `nosetests -s -v factorial.py` (run `man nosetests` in a
  terminal to check what options -s and -v are for.  Do you need them
  both really ATM?)

- `git commit -m "Description of your changes" -a` your work.  Could
be done multiple times

- Make sure that your code passes tests, and also conforms to
  [PEP8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
  by running `flake8 factorial.py` and addressing noted issues.

- Whenever you are ready to submit your homework, run `git push` to
  push your changes back to **your** clone on GitHub

- Visit your GitHub page (http://github.com/YOURLOGIN/psyc161-hw1) and
  find your changes being present among Commits, and "Send a pull
  request" option present.

- Send a "Pull request" against my original repository for review of
  the changes etc.

- Review status of the pull request in a few minutes -- it should
  report successful pass through travis CI run which runs again
  nosetests and flake8 on my behalf.  If not -- inspect travis's logs,
  commit fixes locally, push them to github again so that PR gets
  updated, and travis gets another run.

