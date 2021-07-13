class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        return input_str[::-1]

    def is_english_vowel(self, character):
        if(character in ['a','e','i','o','u','A','E','I','O','U']):
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        Sentence=sentence.split(' ')
        return max(Sentence,key=len)
        

    def get_word_lengths(self, text):
        sentence=text.split(' ')
        List=[]
        for i in sentence:
            List.append(len(i))
        return(List)