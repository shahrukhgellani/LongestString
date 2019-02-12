from nltk.tokenize import word_tokenize
dictionary = {}

def LongestWord(sen):
    lengthOfLargestWord = 0
    tokens = word_tokenize(sen)
    
    for word in tokens:
        dictionary[word] = len(word)
        print(word)
        print(dictionary[word])
        print(len(word))
    
    for key , value in dictionary.items():
        print ("key = " + str(key) + " : " + " value " + str(value) )
        if value > lengthOfLargestWord:
            lengthOfLargestWord = value
            sen = key
        
    return sen
    
# keep this function call here  
print(LongestWord(input()))
