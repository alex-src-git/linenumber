## What is this?
A Python script for prepending line numbers to text - written as a Python learning exercise.

## Tests
Tests reside in `linenumber_tests.py`; they use [unittest](https://docs.python.org/3/library/unittest.html).
### How to run tests from the command line
1. `cd` to the root `linenumber` directory.
2. `python linenumber_tests.py`.

## Example Usage
Input some indented string that lacks line numbers.
<pre>
Get starting directory from user  
If directory does not exist:  
    Log an error and try again  
For each file in directory  
    Read file name  
    If file name ends with "*.py"  
        Add file to collection  
        Log file name  
For each file name in file name collection  
    Log file name  
</pre>
Outputted string now has line numbers :open_mouth:
<pre>
1. Get starting directory from user
2. If directory does not exist:
    2.1. Log an error and try again
3. For each file in directory
    3.1. Read file name
    3.2. If file name ends with "*.py"
        3.2.1. Add file name to collection
        3.2.2. Log file name
4. For each file name in file name collection
    4.1. Log file name
</pre>
