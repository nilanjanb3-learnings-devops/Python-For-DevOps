import re
text = "python2. is old now python3 is popular."
pattern = 'python[23]'
res = re.findall(pattern, text)

'''
i[st] --> is and it
[a-d] --> a or b or c or d
[a-zA-Z0-9] 
\w includes all case characters, digits and '_' as well

\w\w --> aa, ab, ac ... like that

\W --> mathes everything which doesn't contains under \w
\d --> matches digits only
.  --> matches any single character
\. --> matches only dot(.)
^  --> mathches start of line
$  --> matches end of line
\b --> checks for an empty space at right or left side
\B --> checks for an match where space not present at right or left
\t, \n, \r --> matches escape sequences
a{4} --> matches a for 4 times like aaaa
a{2,3,4} --> 2, 3 or 4 times
a{2,} --> matches a 2 or more time
xa* --> matches 0 or more times like x, xa, xaaa
xa+ --> matches one or more time xa,xaa like that
xa? --> only zero or one time like x and xa

================= flags ===================
re.I --> ignore case
re.M --> multiline

to use multiple flags use pipeline symbol like re.I | re.M


'''
text = 'thIs is good and THIS is bad'
pattern = r'this'
res = re.findall(pattern, text, re.I)
print(res)