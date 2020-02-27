# from pandas.compat import to_str
#
# from Kratos import TextRankProject as po
# import csv
# # data=pandas.read_csv("input/chat.csv")
# # data2=pandas.read_csv("input/twitter/twenty_twentyfive.csv",encoding='latin-1')
# sentences, context = po.text_rank_output("twenty_twentyfive.csv")
#
# print(sentences,context)
# with open('output.csv', 'w') as f:
#     f.write("text, context\n")
#     for i in range(4):
#         line=sentences[i]+", "+to_str(context[i])+"\n"
#         f.write(line)
#         # print(type(line))
# # import pandas as pd
# # ss=pd.read_csv("output.csv")
# # print(ss)

# --------PREPROCESSING-----------------
# from Kratos import preprocess as po
# import pandas
# data=pandas.read_csv("../new_dataset.csv", encoding="latin")
# po.pre_precess_text(data)

#---------TRAINING DATA---------------------
import Kratos
from Kratos import Classifications as po
po.training_models("../Kratos/output.csv")
