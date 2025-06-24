import csv
import numpy as np
test=np.load('./processed_data/uci/ml_uci.npy')
np.set_printoptions(threshold=np.inf)
save_result_folder = f"./processed_data/uci/ml_uci_node_npy.csv"
# save_result_path = os.path.join(save_result_folder, f"ml_wikipedia_node_npy.txt")
# with open(save_result_folder, 'w') as file:
#     file.write(test)
# print("The test dataset has {}".format(save_result_path,))
with open('ml_uci_node_npy.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(test)

