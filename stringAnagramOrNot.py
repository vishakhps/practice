def anagram(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) == len(s2):
        sortedString=sorted(s1)
        sortedString2=sorted(s2)
        if sortedString == sortedString2:
            print("Both strings are anagrams")
        else : 
            print(" Strings are Not anagrams")
    else:
        print("strings are not anagrams, length difference")
s1 = "hello"
s2 = "ollh"
anagram(s1,s2)


