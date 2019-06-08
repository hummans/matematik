# Matematik Documentation

Table of Contents:

- [Usage](#usage)
- [Reference](#reference)
- [FAQ](#faq)

<br>

## Usage

Firstly install this pacakage using pip:
```
$ pip install matematik
```
After that you can easily get the math formulas with their respective level of difficulty. For example if you want to get the algebra 2 formulas you need to do :
```py
from matematik.formula.algebra2 import *
```
And this is basiaclly it. At the moment the following modules are included inside the `formula`:
  - arithmetic
  - algebra 1
  - algebra 2
  - geometry
  - trigonometry
  - precalculus

<br>
<br>

## Reference

In this seciton headers are named after sub package names of the package 'matematik'. You can find all of the necessary information and usage of the code in their body content.

### formulas

At the moment there is only one sub pacakage of the matematik and that is: `formula`. It is a sub package that provides you quick solutions for basic formulas and returns you the answer.

Lets view the modules inside this sub package:

#### Arithmetic.py

This module provides you various functions to do arithmetic operations on different kind of data structures and objects. Lets see an example:
```py
from matematik.formula.arithmetic import *

# add(a, b) fucntion returns you a + b
add(6, 6)  # --> 12
```


<br>
<br>

## FAQ
