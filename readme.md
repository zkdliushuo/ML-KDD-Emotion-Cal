# 运行
运行一个脚本示例如下
```
CUDA_VISIBLE_DEVICES=1 python baseline.py --bert_id 1 
```
不同的bert_id指定选择不同的tokenizer的ckpt版本，可以参考[baseline.py](./baseline.py#L21)查看id对应的ckpt

最好使用不同的GPU卡来运行训练

## FAQ
### 现在的run.sh运行有问题，先不要用run.sh