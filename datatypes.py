terminology
    modules - the .py File that you write.
    variables - its just holds some value
    constants - constant
    methods - function
    classes -

execution styles

cpython - a distruction of python among others(jython, )
IDE, shell, script, python interpreter.


python:
  python is a highlevel language.
  author: guido
  written in: c
  usage: data analytics, web, research, testing, cloud, graphics, robotics and electronics

  interpreted language:
    the control flow the program is done one step at a time.
  compile language:
    the program is compiled into an executable binary before execution

  python is both.

  when you run a python program:
  compiler creates a .pyc file(python compiled) - binary data + hash value
  when you modify the .py file - hash value of .py != hash value in .pyc -> new .pyc
  when no modifications & .pyc file exists -> just run the existing .pyc file.

  major syntactical differences:
    indentation: 4 , 8 spaces or 1 tab
    reduced use of {}
    : represents the start of a block.
  block:
    is a set of lines of code that executes at once.

    main(){
      jkahsdlfkasdf; ashdkjf;
    adksljfhas;df;
        asdfasdfsa;
    }

    def main():
        klsdfjsdf
        fasdfsdf
        sdfsdfgsd
        if sfs:



data types:

numbers - int, float, double
char
string - list of chars
boolean - True or False --
True:  12, 'asdf', [12,3,4], {12.3,123}
False: 0, None, [], {}
NoneType


int i;
i =0;

i = 0
flo = 1.0

name = "John"
name[0] == 'J'
name = 'John' # 'John is  in  "theGraves"'
names = '''
            John
            Mike
            Ron
            '''
name = """John"""

all indices start with 0


assignment:
    work on the builtin methods for stringsself.
    perform operations like:
            convert a string '123' into an integer
            check if a '123' is an numbers
            convert 123 into a string
            convert "anusha, madhavi, Priyanka" into a list
            join the list generated above seperated by '^'

agenda tomorrow:
    review assignments
    lists:
        declaration,
        usage,
        iteration
        possible errors and handling
