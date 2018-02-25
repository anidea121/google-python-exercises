#temporary file for sorting algorithms

import sys

def main():
    list2 = ['aa', 'xx', 'zz']
    list1 = ['bb', 'cc']
    list3 = []

    while(len(list1) and len(list2)):
        if (list1[0]<=list2[0]):
            list3.append(list1.pop(0))
        else:
            list3.append(list2.pop(0))
    list3 = list3 + list1
    list3 = list3 + list2

    print 'list1= ', list1
    print 'list2= ', list2
    print 'list3= ', list3

if __name__ == '__main__':
  main()
