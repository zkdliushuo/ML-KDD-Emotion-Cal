import pandas as pd
from collections import Counter
import os

if os.path.exists('baseline_merge.tsv'):
    os.remove('baseline_merge.tsv')

roberta_data=pd.read_csv('baseline_chinese-roberta-wwm-ext.tsv',sep='\t')
roberta_result=roberta_data['emotion'].tolist()
roberta_data.head()

albert_data=pd.read_csv('baseline_albert_chinese_base.tsv',sep='\t')
albert_result=albert_data['emotion'].tolist()
albert_data.head()

base_data=pd.read_csv('baseline_bert-base-chinese.tsv', sep='\t')
base_result=base_data['emotion'].tolist()
base_data.head()

macbert_data=pd.read_csv('baseline_chinese-macbert-base.tsv', sep='\t')
macbert_result=macbert_data['emotion'].tolist()
macbert_data.head()

ernie_data=pd.read_csv('baseline_chinese-macbert-base.tsv', sep='\t')
ernie_result=ernie_data['emotion'].tolist()
ernie_data.head()

def get_counts(list_x):
    count = Counter(list_x).most_common(1)
    # Counter('abracadabra').most_common(3)
    #[('a', 5), ('r', 2), ('b', 2)]
    return count[0]

merge_result=[]
result_analyse=[]
for i in range(len(roberta_result)):
    x1_arr=roberta_result[i].split(',')
    x2_arr=albert_result[i].split(',')
    x3_arr=base_result[i].split(',')
    x4_arr=macbert_result[i].split(',')
    x5_arr=ernie_result[i].split(',')
    result=[]
    for x1,x2,x3,x4,x5 in zip(x1_arr,x2_arr,x3_arr,x4_arr,x5_arr):
        list_x=[]
        list_x.append(round(float(x1)))
        list_x.append(round(float(x2)))
        list_x.append(round(float(x3)))
        list_x.append(round(float(x4)))
        list_x.append(round(float(x5)))
        key,count=get_counts(list_x)
        result.append(key)
        if(count!=0 and count !=5):
            result_analyse.append([i,count])
    merge_result.append(result)
# print(result_analyse[:10])

submit = pd.read_csv('data/submit_example.tsv', sep='\t')
sub_merge = submit.copy()
sub_merge['emotion'] =merge_result
sub_merge['emotion'] = sub_merge['emotion'].apply(lambda x: ','.join([str(i) for i in x]))
sub_merge.to_csv('baseline_merge.tsv', sep='\t', index=False)
sub_merge.head()