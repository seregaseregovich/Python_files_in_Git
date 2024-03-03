"""COUNT THE SMILEY FACES"""

'''Given an array (arr) as an argument complete the function 
countSmileys that should return the total number of smiling faces.

Rules for a smiling face:
Each smiley face must contain a valid pair of eyes. 
Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. 
Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that 
should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
Note
In case of an empty array return 0. You will not be tested 
with invalid input (input will always be an array). 
Order of the face (eyes, nose, mouth) elements will always be 
the same.'''

import re


# ВАРИАНТ 1 (мой):
# ==============================================.

def count_smileys1(arr):
    return sum([1 for i in arr if re.match(r'[:;][-~]?[)D]', i)])


print('Вариант 1')
print(count_smileys1([':)', ';(', ';}', ':-D']))
print(count_smileys1([';D', ':-(', ':-)', ';~)']))
print(count_smileys1([';]', ':[', ';*', ':$', ';-D']))
print()
print('Вариант 2')


# ВАРИАНТ 2 (на мой взгляд - интересный):
# ==============================================.

def count_smileys2(_):
    return re.subn('[:;][~-]?[D)]', '', ' '.join(_))[1]


print(count_smileys2([':)', ';(', ';}', ':-D']))
print(count_smileys2([';D', ':-(', ':-)', ';~)']))
print(count_smileys2([';]', ':[', ';*', ':$', ';-D']))
