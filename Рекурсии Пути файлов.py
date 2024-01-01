F = {
    'C:': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcome.html', 'java.exe']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    }
}


def get_files(path, depth=0):
    for f in path:
        print(' ' * depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth + 1)
        else:
            print(' ' * (depth + 1), ' '.join(path[f]))


get_files(F)


# RESULT:

# C:
#   Python39
#     python.exe python.ini
#   Program Files
#     Java
#        README.txt Welcome.html java.exe
#   Windows
#     System32
#        acledit.dll aclui.dll zipfldr.dll


# Additional info:
# https://www.youtube.com/watch?v=dtzoBXL11oo&list=PLA0M1Bcd0w8yWHh2V70bTtbVxJICrnJHd&index=41
