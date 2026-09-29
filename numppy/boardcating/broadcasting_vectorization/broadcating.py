"""prices=[100,200,300]
dis=10 #10%

final_prices=[]

for price in prices:
    final_price=price-(price * dis/100) 
    final_prices.append(final_price)
print(final_prices)

"""

import numpy as np

prices=np.array([100,200,300])
dis=10 #10%
final_pr=prices-(prices * dis/100)
print(final_pr)