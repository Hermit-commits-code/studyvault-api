# Conditional Statements With Booleans

## Summary

Let's come back a moment to the Boolean data type.In this lesson, I'm going to show you how you canmake some tests and get a Boolean as a result. Andthis Boolean will be the foundation for usingconditions and loops. And for this lesson, I'mgoing to just use the Python Shell here to keepthings very simple. So first, we have the Booleandata type, with True and False as a value. Okay,only two values, then what I can do, let's say Iwant to test the equality between two values, Iwant to test so let's make a very simple test. Iwant to test if one is equal to one. And this isTrue. And as you can see to test the equality I usetwo equal signs, okay, just one equal sign is toassign a value on the right to a variable on theleft. With two equal signs, this is important tomake the difference, this is going to compare thevalue on the left and the value on the right andreturn a Boolean. Is this True, or is this False?Now if I want to test, let's say one is equal totwo, well, this is False. Okay, so that kind ofconditional statements, we are going to use thatin the conditions and in the loops. Now let's seewhat we can do here. So we can use integers. Okay,we can compare two integers, we can also compare,let's see two is equal to two. So 2.0 is equal to2.0. We can also compare float numbers. We cancompare strings. Okay, hello is equal to hello.Now if I do the same, but let's say I put anuppercase here, this is False, and then well, wehave just seen the equal equal operator. Okay,this is just one comparison operator, and you havedifferent operators for different stuff you wantto test. Now let's say want to test not to beequality, the inequality. I want to test if oneis different than two. In this case, I'm going touse exclamation mark equal. And this is Truebecause one is different than two. If I test ifone is different than one, this is False. Okay, sothat's it for the equality. And now what you cantest is you can test if a value is for example,lower than another value. Let's test if one islower than two with this angle bracket here. Andthis is True. Now let's test if one is lower thanone, this is False, because just one angle bracketmeans that it is strictly lower than this, okay.So one is not strictly lower than one. So this isFalse. Now I can also test with the angle bracketand equal and this means lower or equal than one.So if I press Enter, we have True because one islower or equal than one. And I can make theopposite also, I can test if it is greater. So ifone is greater than two, this is False. One isgreater or equal than two, so this is still False.Let's put one and this is True because one isgreater or equal than one. Okay, now, two isgreater than one. In this case, that works. Okay,so basically, you have six comparison operator,the equal equal, the difference, then, andthen the strictly lower, lower or equal, strictlygreater, and greater or equal. Okay. And just onelast thing I'm going to show you, which is veryspecific to Python, is let's say you have a list,number_list. I'm going to create a list with justsome numbers, okay, one, two, and four. What I cando is I can check if a value is inside that list,very simply. I can do for example, to in number_list,and this is True. So you put first thevalue, and then the keyword in and then the nameof the list. So here we test if two is inside thatlist, yes, because it's here. If I try with threein number list, this is False because there is noelement that correspond to three in the list. Sothat is very specific to Python. And that'ssomething that you are going to use also a lot in the future.


---

## Key Concepts

- Main concept from transcript
- Supporting concept
- Important programming idea

---

## Code Example

```python
# Replace with transcript-related example

is_logged_in = True

if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in.")
```

---

## Important Terms

### Boolean
A value that is either True or False.

### Conditional Statement
Logic that controls code execution using conditions.

---

## Common Mistakes

- Incorrect indentation
- Confusing `=` with `==`
- Forgetting colons after conditions

---

## Practice Tasks

- Write 3 if/else statements
- Create a boolean variable
- Practice comparison operators

---

## Tags

- python
- conditionals
- booleans
- beginner
