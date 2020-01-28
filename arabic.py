#!/home/ece-student/anaconda3/bin/python
#chmod 755 splitargs
# -*- coding: utf-8 -*-


# Created by: Pat Rick Ntwari
# Homework 1, EC500


# Converting numbers from arabic to roman numerals

# Number to be converted

def arab_to_roman(given):
    arab = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    roma = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')

    result = []

    for i in range(0,len(arab)):
      intconv = int(given / arab[i])
      result.append(roma[i] * intconv)
      given -= arab[i] * intconv
    result = "".join(result)
    return result

#def main():
#  given = 535
#  print(arab_to_roman(given))



#if __name__ == "__main__":
#  main()
