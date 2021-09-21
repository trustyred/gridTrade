def GrideTradeInit(lower, upper, num, inputUsdt, coinPrice, gasPrice, mult):
    priceDiff = (upper - lower)/(num-1)*1.0
    
    print("每网格价差: ", priceDiff)
    def thePriceForNth(n):
        # 输入的网格数据
        return lower + (n-1)*priceDiff
    
    def theLowerForPrice(price):
        # 这个价格之下最接近的网格
        return ((price - lower) // priceDiff*1.0) + 1
    
    def theUpperForPrice(price):
        # 这个价格之上最接近的网格
        return theLowerForPrice(price) + 1
    # 计算成本价格之下有多少网格
    lNum = int(theLowerForPrice(coinPrice))
    # 计算成本价格之上有多少网格
    uNum = num - lNum    
    # 距离当前价格最近的下方网格的价格
    latestPrice = float(format(thePriceForNth(lNum), '.3f'))
    
    quotePerGrid = 0
    
    print("当前价格: ", coinPrice)
    print("距离当前价格最近的下方网格的价格: ", latestPrice)
    print("上区间价格: ", upper)
    print("下区间价格: ", lower)
    print("网格数: ", num)
    print("当前价格上方网格数量: ", uNum)
    print("当前价格下方网格数量: ", lNum)
    quotePerGrid = inputUsdt * 1.0 / ((latestPrice + lower)*lNum / 2.0 + (lower + upper)*num*mult*gasPrice / 2.0 + coinPrice*(mult*gasPrice*num+uNum)*1.0/(1-gasPrice))
    quotePerGrid = float(format(quotePerGrid, '.2f'))
    coin_init_buy = (mult*quotePerGrid*num*gasPrice + uNum*quotePerGrid)/1.0*(1-gasPrice)
    coin_init_buy = float(format(coin_init_buy, '.2f'))
    coin_init_buy_actually = float(format(coin_init_buy * (1-gasPrice), '.2f'))
    print("每个网格应成交多少meth: ", quotePerGrid)
    print("初始的时候应该购买多少个meth: ", coin_init_buy)
    print("初始的时候实际到手多少个meth: ", coin_init_buy_actually)
    print("购买meth占有总资产的百分比: ", coin_init_buy*coinPrice/inputUsdt)
    print("初始预留作为手续费的meth为: ", mult*quotePerGrid*num*gasPrice)
    print("初始预留作为手续费的usdt为: ", (lower + upper)*num*mult*gasPrice*quotePerGrid / 2.0)
if __name__ == "__main__":
    GrideTradeInit(1, 10, 500, 1003.62, 3.225, 0.0005, 1.8188)