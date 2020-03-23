import pandas as pd
df = pd.read_csv("C:\\SANJIT\\testing\\414.txt", sep="\t",names = ['Text'])
df_que = df[df.index%2 == 0].reset_index(drop=True)
df_ans = df[df.index%2 != 0].reset_index(drop=True)
df_que.rename(columns={"Text": "Question"}, inplace=True)
df_ans.rename(columns={"Text": "Answer"}, inplace=True)
df_f = pd.concat([df_que, df_ans], axis=1)

print(f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[\n')
for i in df_f.index:
    q = df_f['Question'][i]
    a = df_f['Answer'][i]
    if i < df_f.index.stop-1:
        print(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}},\n')
    else:
        print(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}\n')
    
print(f']}}\n</script>')
