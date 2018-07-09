import re
passage=input()
quotes=re.findall(r'\"(.+?)\"',passage)
#type(quotes)
#print(quotes)
passage=re.sub(r'\"(.+?)\"', "QUOTES", passage)
d="."
lines= [e+d for e in passage.split(d) if e]

lines= [l for l in lines if l]
new=[]
sentence=[]
for words in lines:
    new_line=words.split("?")
    for word in new_line:
        if word and new_line.index(word)!=len(new_line)-1:
            word=word+"?"
            new.append(word)
        elif word:
            new.append(word)
    #sentence.append(new)
            
lines=new
new=[]
for words in lines:
    new_line=words.split("!")
    for word in new_line:
        if word and new_line.index(word)!=len(new_line)-1:
            word=word+"!"
            new.append(word)
        elif word:
            new.append(word)
lines=new
i=0
index=0
for words in lines:

    if words.find("QUOTES")!=-1:
        words=words.replace("QUOTES", '"'+quotes[i]+'"')
        i=i+1

        lines[index]= words
    index=index+1
lines = [ l for l in lines if l]

        
for line in lines:
    print(line)

        
