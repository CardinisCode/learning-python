Barracks Challenge - Hackajob

Soldiers really like sleeping and resting. n soldiers settle in k barracks following this set of rules:

- soldiers come one at a time from 1 to n;
-   each soldier chooses the most empty barrack available. If he can choose from more than one equally empty barracks, he chooses one of them randomly;

Your job is to find how many possible ways the soldiers can settle in barracks for a given pair (n, k). Two ways are considered distinct if at least one of the barracks has different soldiers. To make things easier, return the result modulo 1000000007

INPUT
int n
int k

OUTPUT
int nr_ways

CONSTRAINTS
1 <= n <= 10^18
1 <= k <= 10 ^ 6

EXAMPLE 1
Input
3,2
Output
4

EXAMPLE 2
Input
5,2
Output
8