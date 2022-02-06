# Pythonify

Turn your C++/Java code into a Python-like format for extra style points and to make everyone hates you.

For example, Java fans would do something like this:

```java
public class Example {
    private static void permute(int n, char[] a) {
        if (n == 0) {
            System.out.println(String.valueOf(a));
        }
        else {
            for (int i = 0; i <=n; i++) {
                permute(n - 1, a);
                swap(a, n % 2 == 0 ? i : 0, n);
            }
        }
    }

    private static void swap(char[] a, int i, int j) {
        char saved = a[i];
        a[i] = a[j];
        a[j] = saved;
    }

    public static void main() {
        char[] a = "Hello world".toCharArray();
        permute(5, a);
    }
}
```

While Pythonify enjoyers do this:

```java
public class Example                                   {
    private static void permute(int n, char[] a)       {
        if (n == 0)                                    {
            System.out.println(String.valueOf(a))      ;}
        else                                           {
            for (int i = 0; i <=n; i++)                {
                permute(n - 1, a)                      ;
                swap(a, n % 2 == 0 ? i : 0, n)         ;}}}
    
    private static void swap(char[] a, int i, int j)   {
        char saved = a[i]                              ;
        a[i] = a[j]                                    ;
        a[j] = saved                                   ;}
    
    public static void main()                          {
        char[] a = "Hello world".toCharArray()         ;
        permute(5, a)                                  ;}}

```

## Installation

Clone this repository:

```shell
git clone https://github.com/20toduc01/pythonify.git
cd pythonify
```

To run Pythonify, you need Python (obviously). Windows users can download Python from [the official download site](https://www.python.org/downloads/windows/). Pick any version you want.

## Usage

### CLI

```
python pythonify.py [-h] -i INPUT -o OUTPUT [-s INDENT_SIZE] [-e EOL_SPACE] 
```

Whereas:

- INPUT and OUTPUT are the input and output file paths.

- INDENT_SIZE is the prefered number of indentation spaces (default to 4).

- EOL_SPACE is the spacing between the code and semicolons and/or brackets at the end of the line (default to 1).

### As a module

The API is similar to CLI version. Just do something like:

```python
from pythonify import pythonify

pythonify('example.cpp', 'output.cpp', indent_size=4, eol_spacing=1)
```

## Known issues

For now, Pythonify treats every pair of curly braces as a code block wrapper thus in cases where curly braces are used differently (e.g. array definitions), the code would not look so pretty.

## Why?

- I thought [this](assets/meme.png) looks funny.

- I was bored.

- No one tried to stop me.
