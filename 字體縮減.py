import os

a=['index.html']

s=''
for i in a:
    with open(i,encoding='utf8')as f:
        s+=f.read()
g=lambda i:ord(i)>128 or 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9'
s=[i for i in s if g(i)]
al=''.join(list(set(s)))
print(al)

os.system(f'''
pyftsubset "./劇本/css/SourceHanSerifSC-SemiBold.otf" --text={al} --output-file=./劇本/css/思源縮減.ttf
''')