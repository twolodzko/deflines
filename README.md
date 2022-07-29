

![Dolphins](img/dolphins.jpg)

**deflines**, pronounced like *dolphins*, is a simple command-line tool that counts the number of lines per each
function and method as a rough estimate of code complexity. It is build on top of the [Python's ast module].

## Examples

Create report for this repository, sort the results by the number of lines per function:

```shell
$ deflines | sort -k1
   2  1 deflines/deflines.py:55:4 __str__
   3  1 deflines/deflines.py:43:4 lines
   3  1 deflines/deflines.py:60:4 __init__
   3  1 deflines/deflines.py:6:4 __init__
   4  1 deflines/deflines.py:10:4 visit
   6  2 deflines/deflines.py:15:4 line_counter
   6  3 deflines/cli.py:22:0 main
   8  2 deflines/deflines.py:65:4 process
  10  5 deflines/deflines.py:24:4 cc_counter
  11  1 deflines/cli.py:7:0 parse_args
  13  2 deflines/deflines.py:75:4 visit
  20  2 deflines/test_deflines.py:51:0 test_Analyzer
  29  2 deflines/test_deflines.py:120:0 test_Analyzer_cc
```

The first column shows the number of lines and the second column [cyclomatic complexity].

Look only for the python files with "test" in the path:

```shell
$ deflines "**/*test*.py"           
  20  2 deflines/test_deflines.py:51:0 test_Analyzer
  29  2 deflines/test_deflines.py:120:0 test_Analyzer_cc
```

## Installation

To install the package using pip run the following command:

```shell
pip install git+https://github.com/twolodzko/deflines.git#egg=deflines
```

or clone the repository and run

```shell
make install
```

*Image source: <https://en.wikipedia.org/wiki/Persian_Gulf#/media/File:Dolphins_Oman.JPG>*


 [cyclomatic complexity]: https://radon.readthedocs.io/en/latest/intro.html
 [Python's ast module]: https://sadh.life/post/ast/
