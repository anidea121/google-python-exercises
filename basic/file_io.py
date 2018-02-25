#temporary file for handling file input/ output

import sys

def main():
    f = open('sample.txt', 'a')
    #k = f.readlines()
    #print k

    f.write("\nketan deshmukh\n")
    f.close()

    f = open('sample.txt', 'r')
    l = f.read()
    print l
    f.close()

if __name__ == '__main__':
  main()
