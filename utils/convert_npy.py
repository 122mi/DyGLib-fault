import pandas as pd
import numpy as np
 
# 先用pandas读入csv
data = pd.read_csv("./processed_data/wikipedia/ml_wikipedia_node_npy1.csv")
print(data.shape)
# 再使用numpy保存为npy
np.save("./processed_data/wikipedia/ml_wikipedia_node.npy", data)