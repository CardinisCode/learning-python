french_dict = {"me": "moi", "hello": "bonjour", 
               "goodbye": "au revoir", "cat": "chat", 
               "dog": "chien", "and": "et"}

def french2eng(aSentence):
    aSentence = aSentence.lower()
    stringOfWords = aSentence.split()
    new_sentence = ""

    for i in range(0, len(stringOfWords)): 
        if stringOfWords[i] in french_dict:
            stringOfWords[i] = french_dict[stringOfWords[i]]
 
        if i == len(stringOfWords) - 1:
            new_sentence += ''.join(stringOfWords[i])
        else: 
            new_sentence += ''.join(stringOfWords[i]) + " "

    return new_sentence

print(french2eng("Hello it's me"))

#Feedback received: 

#Interesting solution. Your submission does not have any other submissions like it, 
#but we are working to get you customized feedback.
https://app.sense.education/instant_feedback?t=sub&token=6fa00582-75c9-11e8-b3d2-001dd8b71c70&file_token=2b73306b-4e72-11ea-a33b-02311e3e007e

