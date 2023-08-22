def commonChars(self, words):
    '''
        minimumFrequencies: Holds the minimum frequency of each character in all strings
        result: Holds common characters with the least frequency
    '''
    minimumFrequencies = [float(inf)]*26
    result = []

    '''
        Iterate over the words and counter their character frequencies
        Once we count word's character frequencies we update the minimumFrequencies
    '''
    for word in words:
        frequencies = [0]*26
        for char in word:
            frequencies[ord(char) - ord('a')] += 1
        
        for (letter, frequency) in enumerate(frequencies):
            minimumFrequencies[letter] = min(minimumFrequencies[letter], frequency)
    
    '''
        We traverse the minimumFrequencies in order to create the result
    '''
    for (letter, frequency) in enumerate(minimumFrequencies):
        for times in range(frequency):
            result.append(chr(ord('a')+letter))

    return result

print(commonChars(["bella","label","roller"]))
