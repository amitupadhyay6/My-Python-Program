def group_by_owners(files):
    key=list(files.keys())
    val=list(files.values())
    l=len(files)
    dic={}
    i=0
    while i!=l:
        temp=val[i]
        cd=[]
        j=i
        while j!=l:
            if val[j] in dic.keys():
                j+=1
                continue
            else:
                if val[j]==temp:
                    cd.append(key[j])
                    j+=1
                else:
                    j+=1
        if len(cd)!=0:
            dic[temp]=cd
            i+=1
        else:
            i+=1
    return dic

if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy',
        'newbook.exel' : 'Stan'
    }
    print(group_by_owners(files))

########## Passing File name and owner, now we need to return owner and assigned books to them
