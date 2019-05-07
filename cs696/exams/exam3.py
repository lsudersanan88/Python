"""
Exam 3

* You will receive a -10% Penalty if your exam cannot be imported and I must open your exam to test it
* Corrections can be done late for up to 75% of your earned score and
   must be completed before the final exam date (see syllabus).
* Grades will be posted on or before Friday (for exam 2 AND 3)
* Class is canceled on Wednesday (5/1)
* The final exam will not contain any extra material, but it is cumulative
* The final exam will (probably) be slightly longer than exam 2,
   but you will have an extra hour and some of the material will be easy (exam 1 material)
* Grading is described in the syllabus, if you have a question about your final grade,
   check there first. I will ignore emails with questions that are answered literally and directly in the syllabus



"""


def name_id():
    """
$   Please return your REDID followed by your first and last name as separate elements in a list.
    :return: a list of [redID, first_name, last_name]
    """
    return ['817000111', 'Kyle', 'Levi']


def write_no_files_AND_print_no_garbage():
    """
$   If your submission writes a file when imported, you will receive no points for this definition
    If your submission prints anything when imported, you will receive no points for this definition
    """
    return

# Uncomment these lines to write an example CSV file; re-comment it to NOT LOSE POINTS

# with open('example.csv', 'w') as outfile:
#     outfile.write('head1,head2,head3\nrow1,row1.1,row1.2\nrow2,row2.2,row2.2')




"""
Section 1 - Generator Functions and Args/Kwargs

 * MOST of the generators are INFINITE, be sure to read carefully
"""


def inf_gen_1():
    """
$   This generator should accept two strings and yield the first string argument 100 times followed by the second 1 time,
     and repeat this pattern INFINITE times.
    EX: ('abc', 'd') -> 'abc', 'abc', ... 98 more times ... 'd', 'abc', 'abc' ...
    """


def inf_gen_2():
    """
$   Yield the string "Yes" followed by the string "No"; repeat this pattern INFINITE times
    EX: yes_and_no() -> "Yes", "No", "Yes", "No", ...
    """


from random import randint
def inf_gen_3():
    """
$$  Using randint(0,2) to generate random ints 0, 1, or 2, yield "Yes", "No", or "Maybe" an infinite number of times.
    1/3 of all yields should be "Yes", "No", or "Maybe" each; (I know this doesn't guarantee a perfect 1/3 split, but as
     the sample size increases to infinity, this generator should approach a 1/3 frequency for each.)
    EX: () -> "Yes", "No", "Yes", "Maybe", "Maybe", "No", ... randomly generating each with 1/3 probability ...
    """

def return_generator_object():
    """
$$  This definition is not a generator, it is a normal def that returns a generator.
    This definition accepts a single string, and returns a generator object (most likely done with generator comp)
    The returned generator should yield each lower case character in the string
    EX: mygen = return_generator_object('HeLlo')  =>  for i in mygen:  ->  'e', 'l', 'o'
    """

def inf_args():
    """
$   This generator should accept unlimited arguments, and yield them in order. Once all arguments have been yielded,
     this generator should start over, yielding all arguments again, and repeat this pattern INFINITE times
    EX: (1, 4, 'yes', []) -> 1, 4, 'yes', [], 1, 4, 'yes', [], ...
    """


def stream_splitlines():
    """
    This generator contains multiple parts each worth an equal amount.
    This generator should accept a string and key-word arguments. The string will represent a path to a file.
    Yield each line in the file, removing any newline characters at the end of the line,
        and splitting the line into a list by commas ',' by default.
$   1) if the key-word argument 'tabs' is supplied, and its value is True,
        the lines should be split by tabs '\t' instead of by commas
$   2) if the key-word argument 'raw' is supplied, and the value is True,
        the line should be yielded without any modifications, exactly as it is in the file.
        This includes newline characters; additionally 'raw' should take priority above 'tabs'.
        For example, if 'raw' and 'tabs' are both True, the lines should be yielded without any splitting or trimming
$$  3) if any key-word arguments other than 'raw' or 'tabs' are supplied, this program should yield the string
        "Extra Kwargs" once and nothing else. This takes priority above every other case.
    EX: (fruits.csv)  ->  ['fruit', 'flavor', 'convenience', 'durability'] ... next line
    EX: (fruits.csv, tabs=True) -> ['fruit,flavor,convenience,durability'] ...
    EX: (fruits.csv, raw=True) -> ['fruit,flavor,convenience,durability\n'] ...
    EX: (fruits.csv, thing=0) -> "Extra Kwargs"
    """


def process_numbers():
    """
    This definition should accept args and kwargs. Args will always be ints.
    The return type will be a list of the arguments supplied in args (not kwargs)
$   1) if the key-word 'float' is used and it's value is True,
        the type for each item in the returned list should be float.
$   2) if the key-word 'multiply_by' is used (it's value will always be an int),
        each element in args should be multiplied by that number.
$$  3) if the key-word 'div_by' is used (it's value will always be an int),
        each element in args should be divided by that number. If 'div_by' is not supplied,
        each element in args should be divided by 2 by default.
    EX: (2, 2, 4, float=True) -> [1.0, 1.0, 2.0]    # remember, div_by defaults to 2 if not supplied
    EX: (2, 2, 4, multiply_by=10, div_by=1) -> [20, 20, 40]
    """




"""
Definitions as objects, Decorators, and Lambda functions
"""



def for_sorting():
    """
$$  When this def is used for sorting a list of strings it should sort them by
     the number of "K", or "C"s present in the string; lowest to highest.
    (it should accept a single string, and return a single int)
    All strings will have a unique number of "K" and "C"'s present.
    This definition will NOT be tested with reverse=True
    EX: sorted(['AAC', 'AAA', 'CKC', 'KK'], key=<this def here>) -> ['AAA', 'AAC', 'KK', 'CKC']
    """



def only_unique_decorator():
    """
$$  When this decorator is applied to a definition, it should force uniqueness
     in the return value of the definition it is applied to.
    This decorator will only be applied to definitions whose return type
     is a LIST.
    EX: [1, 'yes', 'yes', 1] -> [1, 'yes']
    """


def definition_maker():
    """
$$$ This definition accepts a single int and a type (only float, int, or str),
     and it returns a definition (a lambda function), here I will call that lambda function 'def2'.
    The returned definition (def2) should always accept a single int,
     and return that number added the int argument from definition_maker();
     def2 should also return that number as the type argument provided to definition_maker()
    EX: mydef = definition_maker(3, float)  =>  mydef(4)  ->  7.0
                                            =>  mydef(6)  ->  9.0
        mydef2 = definition_maker(100, str)  =>  mydef2(200)  -> '300'
                                             =>  mydef2(410)  -> '510'
    """


def backup_with_csv_decorator():
    """
$$ When this decorator is applied to a definition, it should write the
     return value of the definition to a CSV file.
    This decorator will only be applied to definitions whose return type
     is ALWAYS a 2d list (a list containing lists) EX: [[1, 2, 3], ['a', 'b', 'c']]
    The name of the file written should always be "backup.csv"
    EX: A regular CSV file (where newlines separate each inner list, and commas separate each value in each inner list)
    EX: [[1, 2, 3], ['a', 'b', 'c']]  ->  1,2,3\n
                                          a,b,c\n  <~ it wont matter if file ends with newline
    """







"""
Argument parsing from command line
"""

# Because there are no argparse or sys.argv questions on this exam, you should expect them on the final





