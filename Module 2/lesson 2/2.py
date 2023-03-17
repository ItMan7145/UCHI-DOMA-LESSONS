import sys

sys.stdout = open("file1.txt", 'w')

import this

sys.stdout.close()
