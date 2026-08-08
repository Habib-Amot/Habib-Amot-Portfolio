# this module has some functions that is used to deal with text and text manipulations

import string 


def simplify(text, whitespace=string.whitespace, delete=''):
    """
    Docstring for simplify
    simplify text by removing any excess whitespace and reducing it to one and if delete is given, it is a character that should be removed from the text
    
    :param text: The text to simplify
    :param whitespace: the character that is considered to be whitespace
    :param delete: an optional character that should be removed from the text

    Example:
    >>>simplify("this \n    and that \t     too")
    'this and that too'
    >>>simplify("just another     text with space   ", delete="ao")
    'just nther text with spce'

    """
    result = []
    word = ""
    for character in text:
        if character in whitespace and word:
            result.append(word)
            word = ""
        elif character not in whitespace and character not in delete:
            word += character
    if word:
        result.append(word)
    print(" ".join(result))


def is_balanced(text, brackets="()[]{}<>"):
    """
    Docstring for is_balanced
    given a string with brackets, it returns True or False if the brackets are balanced or not
    
    :param text: the text containing the text to check if their brackets are balanced or not
    :param brackets: the brackets that are checked against

    :Example
    >>>is_balanced("this should be balanced (i.e with equal(s) number of brackets)")
    True
    >>>is_balanced("2[12] - 3(34[10]")
    False
    """
    # already_encountered_bracket = False
    balanced = True
    left_brackets = "([{<"
    right_brackets = "".join([brackets[brackets.find(left_bracket)+1] for left_bracket in left_brackets])
    encountered_brackets = []

    for character in text:
        if character in brackets:
            if character in right_brackets:
                if not encountered_brackets:
                    balanced = False
                    break

                left_bracket_index = right_brackets.find(character)
                left_bracket = left_brackets[left_bracket_index]
                if encountered_brackets[-1] == left_bracket:
                    encountered_brackets.pop()
                else:
                    balanced = False
                    break
            else:
                encountered_brackets.append(character)
        else:
            continue
    if encountered_brackets:
        balanced = False
    print(True if balanced else False)
            

# print("({(".rstrip('('))


if __name__ == '__main__':
    simplify("this \n    and that \t     too")
    is_balanced('(((((((((((((((())))))))))))))')
    is_balanced('{"id": 101, "tags": ["email", "saas", "violet"]}')
    is_balanced("function test(a, b { console.log(a); }")
