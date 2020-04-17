'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#I will  get word but if it has a length of one I cannot compre it to my two 
# my string "th" I need to start at the begging and take in the first and second 
# elments and compare them to my string if it matches then count as one and move o

def count_th(word):
#    base case:
    s = "th"
    w = len(word)
    l = len(s)
    if w == 0 or w < l:
        return 0
#if length is zero)
#return 0;
# if it matches, increment occurrences
    if word[0 : l] == s:
        return count_th(word[l - 1:]) +1
    return count_th(word[l - 1:])



        
 
        
    
    
        
    
    
   
