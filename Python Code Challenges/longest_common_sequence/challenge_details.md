Code Challenge: Longest Common Sequence (Hackajob)

Given an integer sequence s = (s1,s2,s3,…,sn), a subsequence is another sequence s_ = (s_1, s_2, s_3…., s_k) with 1 < k <= n, and s_1, s_2, s_3…, s_k belonging to s, exactly in that order.

For 2 input sequences a and b, find their longest common subsequence. Focus on time complexity for extra points!
If there are multiple solutions, choose the first one relative to its element's order of appearance in the second sequence.

INPUT
int n ^ length of the first sequence, a

int m
^ length of the second sequence, b

int[] a

int[] b

OUTPUT
string longest_common_subseq

CONSTRAINTS
k < min (m, n)
1 < n <= 3000
1 < m <= 3000
0 <= a_i <= 5000
0 <= b_i <= 5000

EXAMPLE
Input
4 4
[5,6,3,2]
[5,3,6,8]

Output
"5,3"