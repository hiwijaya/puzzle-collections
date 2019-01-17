'''

MINIMUM DISTANCE

A non-empty array A consisting of N non-negative integers is given. For elements A[P] and
A[Q] that are distinct, i.e P != Q, their distance as:

* (A[P] - A[Q]) if (A[P] - A[Q]) >= 0;
* (A(Q) - A[P]) if (A[P] - A[Q]) < 0;

write a solution() that given an array A consisting of N non-negative integers, returns
the minimum distance between two distinct of A.

For example, given array A such that:
A[0] = 8
A[1] = 24
A[2] = 3
A[3] = 20
A[4] = 1
A[5] = 17

the solution should return 2, because (A[2] - A[4]) = 2 and no other two distinct elements of A
have a smaller distance

'''


n = input('A length: ')
n = int(n)
A = []
for i in range(n):
    val = input(f'A-[{i}] = ')
    val = int(val)
    A.append(val)


def solution(A):

    distance = None
    for i, val_p in enumerate(A):

        for j in range(i+1, len(A)):
            val_q = A[j]

            d = val_p - val_q
            if d < 0:
                d = val_q - val_p

            if distance is None:
                distance = d
            else:
                distance = d if d < distance else distance

            if distance == 0:
                break

        if distance == 0:
            break

    return distance


print(solution(A))
