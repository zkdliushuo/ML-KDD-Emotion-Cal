CUDA_VISIBLE_DEVICES=1 python baseline.py --bert_id 0 |& tee log1.txt &
train1=$!
CUDA_VISIBLE_DEVICES=2 python baseline.py --bert_id 1 |& tee log2.txt &
train2=$!
CUDA_VISIBLE_DEVICES=3 python baseline.py --bert_id 2 |& tee log3.txt &
train3=$!

flag=1
while [ "$flag" -eq 1 ]
do
    sleep 5s
    echo "${train1},${train2},${train3} not finished!"
    result1=`ps aux | grep ${train1}`
    result2=`ps aux | grep ${train2}`
    result3=`ps aux | grep ${train3}`
    if [[ -z ${result1} ]] && [[ -z ${result2} ]] && [[ -z ${result3} ]];then
        python vote.py
        exit
    fi
done