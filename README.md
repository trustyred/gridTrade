# 如何运行程序
本程序目前只有一个函数GrideTradeInit，这个函数有7个参数，分别是区间上限，区间下限，网格数量，投入金额，成本价格，每笔交易手续费率，手续费预留倍率。
将这些参数填写到函数参数中，然后使用python3运行程序即可。
例如：
```
~# python3 main.py
每网格价差:  0.018036072144288578
当前价格:  3.225
距离当前价格最近的下方网格的价格:  3.218
上区间价格:  10
下区间价格:  1
网格数:  500
当前价格上方网格数量:  376
当前价格下方网格数量:  124
每个网格应成交多少meth:  0.68
初始的时候应该购买多少个meth:  255.86
初始的时候实际到手多少个meth:  255.73
购买meth占有总资产的百分比:  0.8221722365038561
初始预留作为手续费的meth为:  0.309196
初始预留作为手续费的usdt为:  1.700578
```
