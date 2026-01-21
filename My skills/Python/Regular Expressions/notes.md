# **Python’s Regular Expression Language**
---
## Regular Expressions (Regex)

A **regular expression** is a compact notation for representing a collection of strings. A single regex can represent an **unlimited number of strings**, as long as they meet its rules.

Regexes are defined using a **mini-language different from Python**, but Python provides the **`re` module** to create and use them seamlessly.

### Main Uses of Regex
Regexes are commonly used for five purposes:

- **Parsing**: Identifying and extracting text that matches specific patterns (used in ad-hoc parsers and traditional parsing tools).
- **Searching**: Finding substrings with multiple possible forms  
  *(e.g., `pet.png`, `pet.jpg`, `pet.jpeg`, `pet.svg` while excluding `carpet.png`)*.
- **Search & Replace**: Replacing matched text  
  *(e.g., replacing `bicycle` or `human powered vehicle` with `bike`)*.
- **Splitting Strings**: Splitting text where a pattern occurs  
  *(e.g., at `: ` or `=`)*.
- **Validation**: Checking if text meets criteria  
  *(e.g., a currency symbol followed by digits)*.

** Regular expression in python comprises of one or combination of these tokens**

## Characters and Character Classes
The simplest expressions are just literal characters, such as a or 5, and if no quantifier is explicitly given it is taken to be “match one occurrence”. For example, the regex tune consists of four expressions, each implicitly quantified to match once, so it matches one t followed by one u followed by one n followed by one e, and hence matches the strings tune and attuned.

A character class in regex matches one character from a specified set, written inside square brackets ([]). It is not related to Python classes—it's simply a set of allowed characters.
It matches exactly one character unless quantified.
Example: r[ea]d matches red and rad, but not read.
Digits can be matched with [0123456789] or more compactly [0-9].
A caret (^) negates the class: [^0-9] matches any non-digit character.

## Quantifiers
A quantifier has the form `{m,n}` where m and n are the minimum and maximum times the expression the quantifier applies to must match. For example, both `e{1,1}e{1,1}` and `e{2,2}` match `feel`, but neither matches `felt`.

Having a different minimum and maximum is often convenient. For example, to match travelled and traveled (both legitimate spellings),we could use either * `travel{1,2}ed`* or *`travell{0,1}ed`*. The *{0,1}* quantification is so often used that it has its own shorthand form, ?, so another way of writing the regex (and the one most likely to be used in practice) is travell?ed.

If we use the regex `\d+` it will match 136. But why does it match all the digits, rather than just the first one? By default, all quantifiers are greedy—they match as many charactersas they can. We can make any quantifier nongreedy (also called minimal by following it with a ? symbol. (The question mark has two different meanings—on its own it is a shorthand for the {0,1} quantifier, and when it follows a quantifier it tells the quantifier to be nongreedy.

## Grouping and Capturing
In practical applications we often need regexes that can match any one of two or more alternatives, and we often need to capture the match or some part of the match for further processing. Also, we sometimes want a quantifier to apply to several expressions. All of these can be achieved by grouping with (), and in the case of alternatives using alternation with |.

Alternation is especially useful when we want to match any one of several quite different alternatives. For example, the regex `aircraft|airplane|jet` will match any text that contains “aircraft” or “airplane” or “jet”. The same thing can be achieved using the regex `air(craft|plane)|jet`. Here, the parentheses are used to group expressions, so we have two outer expressions, `air(craft|plane) and jet`

- To name a capture we follow the opening parenthesis with ?P<name>. captures can also be numbers and this is the default naming behavior for captures
- To reference a capture using the id, we use \i where inis the capture number or index. 
- To capture without naming the capture, the syntax (?:) is used 
- To tell if the string after a match is a particular string the syntax (?=e) positve look ahead is used
- To tell if the string after a match is not a particular string, the syntax (?!=e) negative look ahead is used
- To tell if the string before a match is not a particular string, the syntax (?!<e) negative look behind is 
- To tell is the string before a match is a particular string, the syntax (?<e) positive look behind is used 

## Assertions and Flags

An assertion does not match any text, but instead says something about the text at the point where the assertion occurs.
**Assertions** made it possible to determine if a match is valid or not before continuing with the Search
*Some Assertions are*
1. $ - matches end of an expression
2. ^ - matches start of an expression
3. A - same as ^
4. Z - same as $
