randomlist = [42567, 42261, 42164, 35951, 34523, 34195, 34130, 34128, 33962, 30765, 35612, 36109, 41000]
babies_with_vowel_names = [42567, 35951, 34128, 30765]
babies_with_A = [30765, 42050, 29090, 35090]
babies_with_G = [25046, 18561]
sum_of_numbers = 0
for i in randomlist:
    sum_of_numbers += i
#print(sum_of_numbers)

sum_of_babies = 0
# for i in babies_with_vowel_names:
#     sum_of_babies += i

for i in babies_with_G:
    sum_of_babies += i
print(sum_of_babies)