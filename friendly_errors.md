# Errors Are Our Friends
- It's okay if you don't understand an error message at first. What's important is to read them completely first, and then attempt to piece together what you can. Skipping the error message reading step is giving up a huge gift from your program.
- What line does the compiler think the error is on? Does anything look out of place, missing, or extra on that line, or the line before it?
- What does the error message say? Are there any words that don't make sense? Try looking up those words online.

Let's look at the common error types in Python:
- syntax
- name
- type
- attribute

Some of these errors are shy and rarely appear. Others are pretty common. Here are the ones I was able to summon with a simple `print()` command:

| editor | terminal | what's going on? |
| ------------ | ------------- | ------------- |
| print("hi") | hi | No error message :) |
| print("hi) | `SyntaxError: EOL while scanning string literal` | The **missing closing quote** *after hi* caused our compiler to trip up, and never recover. EOL stands for "end of line".  |
| print(hi) | `NameError: name 'hi' is not defined` | The compiler interprets hi as a variable because it doesn't have quotes around it. |
| print "hi" | `SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hi")?` | Since print is a built-in function in Python, the compiler knows to expect parentheses after the print keyword. It kindly reminds the programmer here to put the parenthesis after print ;)  |
| Print("hi") | `NameError: name 'Print' is not defined` | Take a close look at the case (capitalization) of print. In Python, case matters. In the case of Python's built-in functions, they tend to be lower-case. |
| print(%) | `SyntaxError: invalid syntax` | Printing of raw symbols is not valid code. Wrapping the symbol with quotes resolves this issue. |

To have more errors appear, I may need to use something else besides just a simple `print()` to draw them out.

| editor | terminal | what's going on? |
| ------------ | ------------- | ------------- |
| print(len("hello")) | 5 | No errors here :) |
| print(len(100)) | `TypeError: object of type'int' has no len()` | Raw numbers do not have a length property, so the Python compiler says there is an issue with the variable type. |
| print("Com" + "pound") | Compound | Error free. Strings can be "added" to each other in Python, no problem. The technical term for putting strings together is "concatenation". |
| print("Sub" - "traction") | `TypeError: unsupported operand type(s) for -: 'str'and 'str'` | Strings cannot be subtracted from each other using the subtraction operator (hyphen symbol). There is, however, a built-in replace() that is quite useful... |
| print(sum([5,2])) | 7 | Yay, no errors! The sum function works on number lists just fine it seems... |
| print(sum(5, 2)) | `TypeError: 'int' object is not iterable` | ... The sum function cannot handle raw numbers (that aren't in a list) though. |
| print("7".isdigit()) | True | This is error-free because isdigit() works on strings to determine whether they are completely numeric or not. |
| print([7].isdigit()) | `AttributeError: 'list' object has no attribute 'isdigit'` | The (so-far elusive) attribute error appears when we try to use functions not defined for a data structure. |

Not enough error types for you? Me neither :P

**code:**
```python
things = []
print(things[0])
```
**error:** `IndexError: list index out of range`
**what's going on:** "things" is an empty list. Trying to access the zeroeth index (the first item) of an empty list doesn't make sense, and the compiler catches this.
