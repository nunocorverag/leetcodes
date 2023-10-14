from collections import defaultdict

def groupAnagrams(strs):
    #This is used for map the character count of each string and map that to the list of anagrams
    #NOTE: We use the defaultdict method to specify the default value when the dictionary is initialized
    result = defaultdict(list)

    #go through every string
    for s in strs:
        #This list contains 26 elements (26 letters for english alphabet) all initialized on 0
        count = [0] * 26 #a ... z
        #We wanna map a -> 0 and z -> 26
        for c in s:
            #We take the ascii value of the letter and substract the ascii value for a to arrange it from 0 - 26
            count[ord(c) - ord("a")] += 1 #Increment the character by one

        result[tuple(count)].append(s)

    for k,v in result.items():
        print(f"Key: {k}, Value: {v}")
    return result.values()

def main():
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

main()