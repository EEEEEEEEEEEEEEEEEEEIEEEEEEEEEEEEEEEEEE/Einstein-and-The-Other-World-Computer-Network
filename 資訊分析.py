import sys
import collections

import opencc
import jieba
import jieba.analyse
import jieba.posseg

import 詞性表

sys.path.append('d:/librian')

import 編譯

with open('./劇本/試寫.liber', encoding='utf8') as f:
    編譯結果 = 編譯.編譯(f)
    
句組 = []
for i in 編譯結果:
    if i["類型"]=='人物對話':
        句組.append(i["語"])
    if i["類型"]=='旁白':
        句組.append(i["旁白"])

cc = opencc.OpenCC('t2s')
警告數 = 0 
for 句 in 句組: 
    句=cc.convert(句)
    
    分析 = list(jieba.posseg.cut(句))
    
    詞數 = dict(collections.Counter([a for a,b in 分析]))
    for 詞, 詞性 in set(分析):
        if 詞性 in ['x','o','p','eng','zg','ng','d','y'] or 詞性[0]=='u':
            continue
        if 詞數[詞]>1:
            print('')
            # print(f'「{句}」中，({詞性})「{詞}」出現{詞數[詞]}次。')
            print(f'「{句}」中，{詞性表.詞性表[詞性]}({詞性})「{詞}」出現{詞數[詞]}次。')
            警告數 +=1 
            
print(f'驗證完了，共有 {警告數} 警告。')