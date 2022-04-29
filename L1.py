# lambda parameter_list: expression

# 一、Lambda語法與使用範例

# lambda 關鍵字
# parameter 參數清單 : 傳入lambda的參數，可以有多個參數透過逗號隔開
# expression 運算式 : 針對傳入的參數進行運算

# ---範例 1
# 範例中將Lambda函式指派給一個變數，接著就可以透過此變數並傳入參數來進行呼叫

from ast import Num


m = lambda x,y:x+y
print(m(2,4))

# ---範例 2
# Lambda函式支援IIFE(immediately invoked function expression)語法，意思是利用 function expression 的方式來建立函式，並且立即執行它，語法如下：
# (lambda parameter: expression)(argument)

print((lambda x,y:x*y)(3,5))

# 範例中即是利用此語法在Lambda函式定義後，立即傳入參數執行。

# ---範例 3

TxT="英文ABC"
(lambda TxT:print(TxT))(TxT)

# 二、Python Lambda函式的應用

# ---範例 1 
# 將所有傳入參數個別進行 "條件判斷"
# filter()：在可疊代的物件中，依據條件運算式，選擇特定的元素，語法為：
# filter(lambda parameter: expression, iterable)

num=[10,5,20,50,100]
Re=filter(lambda x : x > 20 , num)
print(list(Re))

# filter()內建方法會將串列(List)中的每個元素傳入Lambda函式進行"條件判斷"，最後回傳符合條件的元素，所以執行結果為串列(List)中大於10的元素

# ---範例 2 
# 將所有傳入參數個別進行 "特定的運算"
# map()：在可疊代的物件中，套用特定運算式於每一個元素，語法為：
# map(lambda parameter: expression, iterable)

num=[1,2,4,8,16]
Re=map(lambda x:x*2,num)
print(list(Re))

# map()內建方法會將串列(List)中的每個元素傳入Lambda函式進行"特定的運算"，最後回傳每個元素的運算結果，所以可以看到執行結果的每個串列(List)元素皆放大兩倍。

# ---範例 3
# reduce()：與map()內建方法同樣在可疊代的物件中，套用特定運算式於每一個元素，但是內部的實作方式不一樣，它的實作步驟為：
# 將可疊代物件中的前兩個元素先進行Lambda運算式的運算。
# 接著將第一個步驟的運算結果和可疊代物件中的下一個元素(第三個)傳入Lambda函式進行運算。
# 依此類推，直到可疊代物件的元素都運算完成。
# 也因為每一次的運算都是兩個元素傳入，所以語法為：
# reduce(lambda parameter1, parameter2: expression, iterable)

from functools import reduce # PS.使用reduce()內建方法時，記得引用functools模組。
num=[1,2,4,8,16] # 1*2=2*4=8*8=64*16
Re=reduce(lambda x,y:x*y,num)
print(Re)

# ---範例 4
# sorted()：用來排序可疊代物件中的元素，語法為：
# sorted(iterable, key=lambda parameter: expression)
cars=[
    ("A",500),
    ("B",200),
    ("C",700)
    ]
print(sorted(cars,key=lambda car: car[1]))

# sorted()內建方法利用關鍵字參數key來指定排序的依據，透過Lambda函式就可以自訂要排序的標的。
# 範例中使用car參數來接收串列(List)中的元素，接著回傳元組(Tuple)的第二個元素(也就是價格)，來進行排序。