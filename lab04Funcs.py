# lab04Funcs.py     Functions that work on lists
# P. Conrad for CS8, 04/15/2014

from lab02Funcs import isList
from lab02Funcs import isSimpleNumeric

def notStringContainingE(word):
   """
   return True when word is a string that contains no letter 'e' (or 'E')
   It should work both for lower and upper case.
   When word isn't a string, return True (because it is not a string contaning an E)

   >>> notStringContainingE('Fred')    
   False
   >>> notStringContainingE('Jane')
   False
   >>> notStringContainingE('Santa')
   True
   >>> notStringContainingE('Barbara')
   True
   >>> notStringContainingE('Edward')
   False
   >>> notStringContainingE('Ice Cream')
   False
   >>> notStringContainingE(23)
   True
   >>> notStringContainingE(['e'])
   True
   >>>
   """
   if not(type(word)==str):
      return True
   for letter in word:
     if letter == 'e' or letter=='E':   
       return False
   return True

def hasNoX(word):
   """
   return True when word is a string that contains no letter 'x' (and no letter 'X')
   It should work both for lower and upper case.
   When word isn't a string, return True (because it is not a string with an  x in that case!)

   >>> hasNoX('Fred')
   True
   >>> hasNoX('Xerox')
   False
   >>> hasNoX('Box')
   False
   >>> hasNoX('Xbox')
   False
   >>> hasNoX(23)
   True
   >>> hasNoX(['x'])
   True
   >>> hasNoX('x')
   False
   >>>
   """
   if(type(word)!=str):
      return True
   for letter in word:
     result=True
     if (letter != 'x') and (letter != 'X'):
        result=result and True
     else:
        result=False 
   return result

# The following function is provided for you as an example
# of how to write a Python function that checks if EVERY element
# of a list has some property.

def isListOfSimpleNumeric(theList):
   """
   indicates whether value of argument is a list of only simple numerics (int or float)
   Note: empty list should return True---it doesn't contain anything that ISN'T simple numeric
   theList can be anything, and it will return either True or False.

   >>> isListOfSimpleNumeric('Fred')
   False
   >>> isListOfSimpleNumeric(3)
   False
   >>> isListOfSimpleNumeric([3])
   True
   >>> isListOfSimpleNumeric([3.4])
   True
   >>> isListOfSimpleNumeric([2,3,4,5.6,7])
   True
   >>> isListOfSimpleNumeric([2,3,'oops',5])
   False
   >>> isListOfSimpleNumeric([2,3,[4]])
   False
   >>> isListOfSimpleNumeric([])
   True
   """
   if (not isList(theList)):
      return False  # it isn't really a list!

   # Now we can assume that theList really is a list
   # But is it a list of all numerics?
   # If we find even a single item that isn't numeric, we can
   # immediately return false.  
   
   for item in theList:
     if not isSimpleNumeric(item):
       return False

   # If we get here and didn't return yet, then we know everything
   # in the list is a simple numeric!
   # (i.e. there isn't anything in the list that is NOT simple numeric)
   
   return True

def isListOfIntegers(theList):
   """
   indicates whether value of argument is a list of only int 
   Note: empty list should return True---it doesn't contain anything that ISN'T int
   theList can be anything, and it will return either True or False.

   >>> isListOfIntegers('Fred')
   False
   >>> isListOfIntegers(3)
   False
   >>> isListOfIntegers([3])
   True
   >>> isListOfIntegers([3.4])
   False
   >>> isListOfIntegers([2,3,4,5.6,7])
   False
   >>> isListOfIntegers([2,3,'oops',5])
   False
   >>> isListOfIntegers([2,3,4,5,6,7])
   True
   >>> isListOfIntegers([2,3,[4]])
   False
   >>> isListOfIntegers([])
   True
   """
   if (not isList(theList)):
      return False  
   
   for item in theList:
     if type(item) != int:
       return False

   return True

def isListOfEvenIntegers(theList):
   """
   indicates whether value of argument is a list of only even integers
   Note: empty list should return True---it doesn't contain anything that ISN'T an even integer
   theList can be anything, and it will return either True or False.

   >>> isListOfEvenIntegers('Fred')
   False
   >>> isListOfEvenIntegers(3)
   False
   >>> isListOfEvenIntegers([3])
   False
   >>> isListOfEvenIntegers([4])
   True
   >>> isListOfEvenIntegers([3.4])
   False
   >>> isListOfEvenIntegers([2,3,4,5.6,7])
   False
   >>> isListOfEvenIntegers([2,3,'oops',5])
   False
   >>> isListOfEvenIntegers([2,3,4,5,6,7])
   False
   >>> isListOfEvenIntegers([2,4,6])
   True
   >>> isListOfEvenIntegers([2,3,[4]])
   False
   >>> isListOfIntegers([])
   True
   >>>
   """
   if (not isListOfIntegers(theList)):
      return False  
   
   for item in theList:
     if item % 2 != 0:
       return False

   return True     

def totalLength(listOfStrings):
    """
    returns total length of all the strings in a list of strings, False if argument not a list, 0 for empty list
    >>> totalLength('1')
    False
    >>> totalLength(['a','b'])
    2
    >>> totalLength([])
    0
    >>> totalLength(['Go','Gauchos'])
    9
    >>> totalLength(['x','xxx','xxxx'])
    8
    """
    if (not isList(listOfStrings)):
       return False  

    result=0   

    for item in listOfStrings:
       if type(item)==str:
          result= result + len(item)
      
    return result

def lengthOfEach(listOfStrings):
    """
    given list of strings, returns list of ints correponding to length of each string, otherwise False.

    empty list yields empty list.

    >>> lengthOfEach('1')
    False
    >>> lengthOfEach(['a','b'])
    [1, 1]
    >>> lengthOfEach([])
    []
    >>> lengthOfEach(['Go','Gauchos'])
    [2, 7]
    >>> lengthOfEach(['x','xxx','xxxx'])
    [1, 3, 4]
    >>>
    """
    if (not isList(listOfStrings)):
       return False  

    result=[]   

    for item in listOfStrings:
       if type(item)==str:
          result= result + [len(item)]
      
    return result

def countEvens(listOfInts):
    """
    given a list of ints, counts even ints in list.  Otherwise, returns False.
 
    yields 0 for empty list, or list of ints with no evens in it.

    >>> countEvens('1')
    False
    >>> countEvens(['a','b'])
    False
    >>> countEvens([])
    0
    >>> countEvens([1,2,3,4,5])
    2
    >>> countEvens([1])
    0
    >>> countEvens([3,2])
    1
    >>> countEvens([2,3,4])
    2
    >>>
    """
    if (not isList(listOfInts)):
       return False  

    result=0   

    for item in listOfInts:
       if type(item)==int:
          if item % 2 == 0:
             result= result + 1
      
    return result

def onlyEvens(listOfInts):
   """
    given a list of ints, return new list with only the even ones.  Otherwise, return false.

    empty list yields empty list

    >>> onlyEvens('1')
    False
    >>> onlyEvens(['a','b'])
    False
    >>> onlyEvens([])
    []
    >>> onlyEvens([1,2,3,4,5])
    [2, 4]
    >>> onlyEvens([1])
    []
    >>> onlyEvens([1,3])
    []
    >>> onlyEvens([3,2])
    [2]
    >>> onlyEvens([2,3,4])
    [2, 4]
    >>>
   """
   if (not isListOfIntegers(listOfInts)):
      return False
   result=[]   

   for item in listOfInts:
      if item % 2 == 0:
         result= result + [item]
   return result
