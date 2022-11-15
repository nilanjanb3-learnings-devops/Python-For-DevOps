import re
# by default search is for multi line
text = "this is python tutorial, there are two major versions python2 and python3 in future python4 will come"

pattern = r"\bpython[23]?\b"

# math_obj = re.search(pattern, text)

# if math_obj:
#     # print(math_obj)
#     print(math_obj.group())
#     print(f'starting index {math_obj.start()}')
#     print(f'ending index {math_obj.end()-1}')
#     print(f'length is {math_obj.end()-math_obj.start()}')

# else:
#     print('no match found')


# match will only look for 0th index, it'll not fetch more or even same line

text = "python this is python tutorial, there are two major versions python2 and python3 in future python4 will come"
match_obj = re.match(pattern, text)

if match_obj:
    print(match_obj.group())