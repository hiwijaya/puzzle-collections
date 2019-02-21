'''

CHOCOLATE

Rob likes chocolates. He finds N chocolates in his refrigerator to which he gives a special value.
He is also a mathematics lover, so he decides to do something peculiar with the chocolates.

He performs some operations on the chocolates. In each operation, he takes one or more chocolates which are lying in
a continuous manner. He then finds and notes down the minimum special value of a chocolate in that group of chocolates.
He performs this operation for all the groups of chocolates he could find. But unfortunately his pet dog ate
the paper on which he had written the results. Your task is to find the sum of all the numbers he had written.

Input Specification:
input1: The number of chocolates N.
input2: The array representing the special values of chocolates.

Output Specification:
The desired sum.

Example:
input1: 2
input2: {3,4}

Output: 10

Explanation:
Here, the groups he can form by using one or more continuous chocolates are {3},{4},{3,4} and
the minimum of each group is 3, 4, 3 and the sum of these is 10.

'''


n = input('chocolate N: ')
n = int(n)
values = []
for i in range(n):
    val = input('chocolate value ' + str(i) + ':')
    val = int(val)
    values.append(val)

total = 0
for group_length in range(1, n+1):
    for j in range(n):
        if (j + group_length) > n:
            break
        group = []
        for k in range(group_length):
            idx = j+k
            if idx >= n:
                break
            group.append(values[idx])
        print(group)

        # find minimum in group || otherwise, you can use build in function --> min(group)
        minimum = 0
        for i, val in enumerate(group):
            if i == 0:
                minimum = val
                continue
            if val < minimum:
                minimum = val
        total += minimum
print('')
print(total)
