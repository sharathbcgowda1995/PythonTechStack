class reverse_word:
    @staticmethod
    def reverse_word_space(word_string):
        word = list(word_string)
        start = 0
        end = len(word)-1
        while(start<end):
            if word[start]==' ':
                start+=1
            elif word[end]==' ':
                end-=1
            else :
                word[start],word[end]=word[end],word[start]
                start+=1
                end-=1

        return ''.join(word)
print(reverse_word.reverse_word_space("Welcome to java"))
