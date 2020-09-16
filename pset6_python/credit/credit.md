Week 6, Python challenge: Credit

Implement a program that determines whether a provided credit card number is valid according to Luhn’s algorithm.

$ python credit.py
Number: 378282246310005
AMEX

Contents: 
-   Specification
-   Problem set 1 info
-   Luhn's Algorithm
-   Testing

*** Specification: ***

In credit.py in ~/pset6/credit/, write a program that prompts the user for a credit card number and then reports (via print) whether it is a valid American Express, MasterCard, or Visa card number, exactly as you did in Problem Set 1, except that your program this time should be written (a) in Python and (b) in CS50 IDE.
So that we can automate some tests of your code, we ask that your program’s last line of output be AMEX\n or MASTERCARD\n or VISA\n or INVALID\n, nothing more, nothing less.
For simplicity, you may assume that the user’s input will be entirely numeric (i.e., devoid of hyphens, as might be printed on an actual card).
Best to use get_int or get_string from CS50’s library to get users’ input, depending on how you to decide to implement this one.
Usage
Your program should behave per the example below.

$ python credit.py
Number: 378282246310005
AMEX

*** Problem Set 1 info: ***

In Problem Set 1, we got the following info to solve this challenge: 

A credit (or debit) card, of course, is a plastic card with which you can pay for goods and services. Printed on that card is a number that’s also stored in a database somewhere, so that when your card is used to buy something, the creditor knows whom to bill. There are a lot of people with credit cards in this world, so those numbers are pretty long: American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers. And those are decimal numbers (0 through 9), not binary, which means, for instance, that American Express could print as many as 10^15 = 1,000,000,000,000,000 unique cards! (That’s, um, a quadrillion.)

Actually, that’s a bit of an exaggeration, because credit card numbers actually have some structure to them. All American Express numbers start with 34 or 37; most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers which we won’t concern ourselves with for this problem); and all Visa numbers start with 4. But credit card numbers also have a “checksum” built into them, a mathematical relationship between at least one number and others. That checksum enables computers (or humans who like math) to detect typos (e.g., transpositions), if not fraudulent numbers, without having to query a database, which can be slow. Of course, a dishonest mathematician could certainly craft a fake number that nonetheless respects the mathematical constraint, so a database lookup is still necessary for more rigorous checks.

*** Luhn's Algorithm: ***

So what’s the secret formula? Well, most cards use an algorithm invented by Hans Peter Luhn of IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:

Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
Add the sum to the sum of the digits that weren’t multiplied by 2.
If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
That’s kind of confusing, so let’s try an example with David’s Visa: 4003600000000014.

For the sake of discussion, let’s first underline every other digit, starting with the number’s second-to-last digit:

4003600000000014

Okay, let’s multiply each of the underlined digits by 2:

1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2

That gives us:

2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

Now let’s add those products’ digits (i.e., not the products themselves) together:

2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13

Now let’s add that sum (13) to the sum of the digits that weren’t multiplied by 2 (starting from the end):

13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20

Yup, the last digit in that sum (20) is a 0, so David’s card is legit!

So, validating credit card numbers isn’t hard, but it does get a bit tedious by hand. Let’s write a program.


*** Testing: ***

No check50 for this problem, but be sure to test your code for each of the following.

Run your program as python credit.py, and wait for a prompt for input. Type in 378282246310005 and press enter. Your program should output AMEX.

Run your program as python credit.py, and wait for a prompt for input. Type in 371449635398431 and press enter. Your program should output AMEX.

Run your program as python credit.py, and wait for a prompt for input. Type in 5555555555554444 and press enter. Your program should output MASTERCARD.

Run your program as python credit.py, and wait for a prompt for input. Type in 5105105105105100 and press enter. Your program should output MASTERCARD.

Run your program as python credit.py, and wait for a prompt for input. Type in 4111111111111111 and press enter. Your program should output VISA.

Run your program as python credit.py, and wait for a prompt for input. Type in 4012888888881881 and press enter. Your program should output VISA.

Run your program as python credit.py, and wait for a prompt for input. Type in 1234567890 and press enter. Your program should output INVALID.
