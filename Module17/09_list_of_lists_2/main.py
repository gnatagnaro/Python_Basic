nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

output_list = [i for j in nice_list for t in j for i in t]

print(output_list)
