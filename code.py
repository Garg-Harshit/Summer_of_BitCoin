#    ____                       _   _                _     _ _   
#   / ___| __ _ _ __ __ _      | | | | __ _ _ __ ___| |__ (_) |_ 
#  | |  _ / _` | '__/ _` |_____| |_| |/ _` | '__/ __| '_ \| | __|
#  | |_| | (_| | | | (_| |_____|  _  | (_| | |  \__ \ | | | | |_ 
#   \____|\__,_|_|  \__, |     |_| |_|\__,_|_|  |___/_| |_|_|\__|
#                   |___/                                        


print('''
  ____                                               __   ____  _ _    ____      _       
 / ___| _   _ _ __ ___  _ __ ___   ___ _ __    ___  / _| | __ )(_) |_ / ___|___ (_)_ __  
 \___ \| | | | '_ ` _ \| '_ ` _ \ / _ \ '__|  / _ \| |_  |  _ \| | __| |   / _ \| | '_ \ 
  ___) | |_| | | | | | | | | | | |  __/ |    | (_) |  _| | |_) | | |_| |__| (_) | | | | |
 |____/ \__,_|_| |_| |_|_| |_| |_|\___|_|     \___/|_|   |____/|_|\__|\____\___/|_|_| |_|

                                               
Submitted By - Harshit Garg
GitHub Username - Garg-Harshit
LinedIn Username - harshitgarg02
E-Mail ID - harshitgarg3012@gmail.com

                                                                                         ''')

from time import sleep

print('Importing Data From "mempool.csv"..')
with open('mempool.csv') as csv_file:
    read_data = csv_file.readlines()
read_data=read_data[1:]
print('Importing Data From "mempool.csv"....')
data_dic = {}
txn_num = 0
for row in read_data:
    txn_num += 1
    temp_var = row.strip().split(',')
    data_dic[temp_var[0]]=[txn_num,temp_var[1],temp_var[2],True]
    data_dic[temp_var[0]]+=temp_var[3].split(';')
print('Importing Data From "mempool.csv"....Finished!\n\n')


print('Cleaning Data and Storing..')
for i in data_dic.keys():
    if data_dic[i][-1] == '':
        data_dic[i][3] = False
    else:
        flag = False
        for parent in data_dic[i][4:]:
            if data_dic[i][0] < data_dic[parent][0]:
                flag = True
                break
        if not flag:
            data_dic[i][3] = False
print('Cleaning Data and Storing....')
transactions_valid = []
weight = []
for i in data_dic.keys():
    if data_dic[i][3] == False:
        transactions_valid.append(i)
        weight.append((int(data_dic[i][1]),int(data_dic[i][2]), i))
print('Cleaning Data and Storing....Finished!\n\n')


print('Creating BlockChain with Combined Weight Less than or Equal to 4000000..')
n=len(weight)
weight = sorted(weight,reverse=True)
weight_in_block = 0
block_chain=[]
s = 0
for i in weight:
    s += i[0]
    weight_in_block += i[1]
    if weight_in_block > 4000000:
        weight_in_block -= i[1]
        s -= i[0]
        break
    block_chain.append(i[2])
print('Creating BlockChain with Combined Weight Less than or Equal to 4000000..Finished!\n\n')


print(f"BlockChain consistes of {len(block_chain)} transactions with total Transaction Value (FEE) - {s} and of Block Weight - {weight_in_block} .\n\n")


print('Creating File named "block.txt" and writting Transaction ID\'s to it...')
with open(r"block.txt", "w") as Final_Result:
    for i in block_chain:
        Final_Result.write(f"{i}\n")
    Final_Result.close()
print('Creating File named "block.txt" and writting Transaction ID\'s to it...Finished!\n\n')

print("Closing Output File Done!\n\nExecution Completed!\n\n")


print("Code Will Exit in 5 sec.!")
sleep(5)
exit(0)