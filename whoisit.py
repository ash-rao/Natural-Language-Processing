N=int(input())
sentences=[]
for _ in range(N):
    sentences.append(input())
characters=input().split(";")
str_sent=''
for sentence in sentences:
    str_sent=str_sent+sentence
sentences=str_sent
import re
def determining_pronouns(sentence, characters):
    pronouns=re.findall('[*]+[A-Za-z]+[*]+',sentence)
    cur_index=-1
    values=[]
    for word in pronouns:
        cur_index=sentence.find(word, cur_index+1)
        values.append(cur_index)
    pronouns=[word.split("**")[1] for word in pronouns]
    word_index=dict(zip(values, pronouns ))
    
    char_dict={}
    for character in characters:
        char=re.findall(character, sentence)
        cur_index=-1
        values=[]
        for word in char:
            cur_index=sentence.find(word, cur_index+1)
            values.append(cur_index)
        char_dict[character]=values
    he_pronouns=['he', 'his', 'him']
    she_pronouns=['she', 'her', 'hers']
    they_pronouns=['they', 'theirs', 'their']
    it_pronouns=['it', 'its']
    output=[]
    kind={}
    for char in char_dict:
        kind[char]=she_pronouns+he_pronouns+they_pronouns+it_pronouns
    for word in pronouns:
        for key in word_index:
            if word_index[key]==word:
                index=key
                diff=len(sentence)
                for character in char_dict:
                    #print(character)
                    for num in char_dict[character]:
                    
                        if(min(diff, (index-num))!=diff )and index-num>0 and word.lower() in kind[character]:
                            diff=min(diff, index-num)
                            selected_character=character
                            selected_index=num
                break
        output.append(selected_character)
        word_index.pop(index)
        if word in she_pronouns:
            kind[selected_character]=she_pronouns
        elif word in he_pronouns:
            kind[selected_character]=he_pronouns
        elif word in they_pronouns:
            kind[selected_character]=they_pronouns
        elif word in it_pronouns:
            kind[selected_character]=it_pronouns
            
    for out in output:
        print(out)

determining_pronouns(sentences, characters)
        
            
