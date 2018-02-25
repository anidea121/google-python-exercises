#temporary file for sorting algorithms

import sys

def main():
    list2 = ['aa', 'xx', 'zz']
    list1 = ['bb', 'cc']
    list3 = []

    i=0
    j=0

    while(i<len(list1) and j<len(list2)):
        if (list1[i]<=list2[j]):
            list3.append(list1[i])
            i = i + 1
        else:
            list3.append(list2[j])
            j = j + 1
    if (i==len(list1)):
        list3 = list3 + list2[j:]
    elif (j==len(list2)):
        list3 = list3 + list1[i:]
    else:
        return list3

    print 'list1= ', list1
    print 'list2= ', list2
    print 'list3= ', list3

if __name__ == '__main__':
  main()
            
            
        










if __name__ == '__main__':
  main()
