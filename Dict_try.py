from Kratos import TextRankProject as tp
sentences, context = tp.text_rank_output("twenty_twentyfive.csv")

l = context.tolist
max = 0
temp = 0
for i in range(5):

    if max < context.count(i):
        temp = i
        max = context.count(i)
    i = i + 1

print(temp)