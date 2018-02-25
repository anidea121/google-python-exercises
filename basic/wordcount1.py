

import sys

d = {}
def print_words(file1name):
  f=open(filename,'rU')
  for line in f:
    for word in line.split():#line.split() splits by white space
      word1=word.lower()
      if word1 in d:#find word in dict, if yes add1, else introduce the word
        d[word1]=d[word1]+1
      else:
        d[word1]=1

  for keys in sorted(d.keys()):#printing by sorted words followed by their counts
    print keys, d[keys]
   
  f.close()



def main():
  print_words(sys.argv[1])


if __name__ == '__main__':
  main()
