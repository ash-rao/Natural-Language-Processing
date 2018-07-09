def getmaintext(url):
    url=url.split(".")
    try:
        index=url.index('www')
        return url[index+1]
    except Exception:
        return url[0]
    
def findword(merged):
    with open("words.txt", "r") as f:
        wordset=f.readlines()
    wordset=[word.rstrip().lower() for word in wordset]
    i=-1
    splitwords=[]
    if merged in wordset:
        return [merged]
    while( i!=-(len(merged))):
        if merged[:i] in wordset:
            splitwords.append(merged[:i])
            temp=findword(merged[i:])
            if type(temp) is str:
                splitwords.append(temp)
            else:
                splitwords.extend(temp)
            break
        i=i-1
    return (splitwords)
def findwordfromfront(string, split_result):
    i=-1
    with open("words.txt", "r") as f:
        word=f.readlines()
    word=[w.rstrip().lower() for w in word]
    
    split_token=[]
    for j in range(len(split_result)):
        i=-1
        while(i>=-len(split_result[j])):
            if split_result[j][:i] in word:
                split_token.append(split_result[j][:i])
                new_string=string[(len(''.join(split_result[:j]))+len(split_result[j][:i])):]
                new_split_result=findword(string[(len(''.join(split_result[:j]))+len(split_result[j][:i])):])
                if len(new_string)==len(''.join(new_split_result)):
                    split_token.extend(new_split_result)
                    return split_token
                if [new_string]!=new_split_result and len(new_split_result)!=0:
                    split_token.extend(findwordfromfront(new_string,new_split_result))
                else:
                    split_token.extend(new_split_result)
                return split_token
            i=i-1
        if len(split_token)<=j:
            split_token.append(split_result[j])
N=int(input())
for _ in range(N):
    string=input().lower()
    if string[0]=="#":
        result=(' '.join(findword(string[1:])))
        if len(''.join(result.split(" ")))!=len(string[1:]):
            result1=(findwordfromfront(string[1:], result.split(' ')))
            if result1!=None:
                print(' '.join(result1))
            else:
                print(result)
            
        else:
            print(result)
    else:
        result=(' '.join(findword(getmaintext(string))))
        if len(''.join(result.split(" ")))!=len(getmaintext(string)):
            result1=findwordfromfront(getmaintext(string), result.split(' '))
            if result1!=None:
                result1=' '.join(result1)
                print(result1)
            else:
                print(result)
            
        else:
            print(result)
