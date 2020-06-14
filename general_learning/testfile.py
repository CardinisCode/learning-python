births = [42567, 42261, 42164, 35951, 34195, 34130, 34128, 30765, 14704, 14615, 13966, 10259, 7700, 7052, 6788, 6194, 564, 3470, 3096, 186, 13875, 2954, 119]

count = 0
for i in births:
    count += i
# print()
# print(count)


births_2 = [42567, 35951, 34128, 30765, 7052]
count_2 = 0
for i in births_2:
    count_2 += i



letter_count = [2954, 119]

# megavenusaur = [80,100,123,122,120,80]
# print("Mega Venusaur:", sum(megavenusaur), "number:", 3)
# megacharizardx = [78,130,111,130,85,100]
# print("Mega Charizard X:", sum(megacharizardx), "number:", 6)
# megacharizardy = [78,104,78,159,115,100]
# print("Mega Charizard Y:", sum(megacharizardx), "number:", 6)
# megablastoise = [79,103,120,135,115,78]
# print("Mega Blastoise:", sum(megablastoise), "number:", 9)
# mega_beedrill = [65,150,40,15,80,145]
# print("Mega Beedrill:", sum(mega_beedrill), "number:", 15) 
# mega_pidgeot = [83,80,80,135,80,121]
# print("Mega Pidgeot:", sum(mega_pidgeot), "number:", 18)
# print()
# all_totals = [625, 634, 634, 630, 495, 579]
# print("Our overall total is:", sum(all_totals))
mega_avg = round(3597 / 6)
print("Our average for Mega:", mega_avg)
print()

venusaur = [80,82,83,100,100,80]
print("Venusaur:", sum(venusaur), "number:", 3)
charizard = [78,84,78,109,85,100]
print("Charizard:", sum(charizard), "number:", 6)
blastoise = [79,83,100,85,105,78]
print("Blastoise:", sum(blastoise), "number:", 9)
beedrill = [65,90,40,45,80,75]
print("Beedrill:", sum(beedrill), "number:", 15)
pidgeot = [83,80,75,70,70,101]
print("Pidgeot:", sum(pidgeot), "number:", 18)
all_totals = [525, 534, 530, 395, 479]
print("Our overall total is:", sum(all_totals))
non_mega_avg = round(2463/5)
print("Our average for Non Mega:", non_mega_avg)

print("The difference is:", abs(mega_avg - non_mega_avg))




print("Mega:")
my_mega_list = [625,634,634,630,495,579,590,590,600,590,600,640,615,780,780,610,610,600,600,600,700,630,630,635,618,480,480,630,510,575,560,560,590,555,565,580,700,700,700,700,780,580,700,625,594,618,545,700]
mega_total_value = sum(my_mega_list)
mega_count = len(my_mega_list)
mega_avg = round(mega_total_value / mega_count)
print(mega_total_value, ":", mega_count, "gives an avg:", mega_avg)

print()
print("Non Mega:")
my_non_mega_list = [525,534,530,395,479,500,490,500,490,500,540,515,680,510,510,500,500,500,600,530,530,535,518,380,380,530,410,475,460,460,490,455,465,480,600,600,600,600,680,480,600,525,494,518,445,600]
non_mega_total_value = sum(my_non_mega_list)
non_mega_count = len(my_non_mega_list)
non_mega_avg = round(non_mega_total_value / non_mega_count)
print(non_mega_total_value, ":", non_mega_count, "gives an avg:", non_mega_avg)


list1 = [625,634,634,630,495,579,590,590,600,590,600,640,615,780,780,610,610,600,600,600,700,630,630,635,618,480,480,630,510,575,560,560,590,555,565,580,700,700,700,700,780,580,700,625,594,618,545,700]
if my_mega_list == list1:
    print("True")

list_2 = [525,534,530,395,479,500,490,500,490,500,540,515,680,510,510,500,500,500,600,530,530,535,518,380,380,530,410,475,460,460,490,455,465,480,600,600,600,600,680,480,600,525,494,518,445,600]
if my_non_mega_list == list_2:
    print("2 True")


"""
Number: 3 name: Mega Venusaur total_stat: 625
Number: 6 name: Mega Charizard X total_stat: 634
Number: 6 name: Mega Charizard Y total_stat: 634
Number: 9 name: Mega Blastoise total_stat: 630
Number: 15 name: Mega Beedrill total_stat: 495
Number: 18 name: Mega Pidgeot total_stat: 579
Number: 65 name: Mega Alakazam total_stat: 590
Number: 80 name: Mega Slowbro total_stat: 590
Number: 94 name: Mega Gengar total_stat: 600
Number: 115 name: Mega Kangaskhan total_stat: 590
Number: 127 name: Mega Pinsir total_stat: 600
Number: 130 name: Mega Gyarados total_stat: 640
Number: 142 name: Mega Aerodactyl total_stat: 615
Number: 150 name: Mega Mewtwo X total_stat: 780
Number: 150 name: Mega Mewtwo Y total_stat: 780
Number: 181 name: Mega Ampharos total_stat: 610
Number: 208 name: Mega Steelix total_stat: 610
Number: 212 name: Mega Scizor total_stat: 600
Number: 214 name: Mega Heracross total_stat: 600
Number: 229 name: Mega Houndoom total_stat: 600
Number: 248 name: Mega Tyranitar total_stat: 700
Number: 254 name: Mega Sceptile total_stat: 630
Number: 257 name: Mega Blaziken total_stat: 630
Number: 260 name: Mega Swampert total_stat: 635
Number: 282 name: Mega Gardevoir total_stat: 618
Number: 302 name: Mega Sableye total_stat: 480
Number: 303 name: Mega Mawile total_stat: 480
Number: 306 name: Mega Aggron total_stat: 630
Number: 308 name: Mega Medicham total_stat: 510
Number: 310 name: Mega Manectric total_stat: 575
Number: 319 name: Mega Sharpedo total_stat: 560
Number: 323 name: Mega Camerupt total_stat: 560
Number: 334 name: Mega Altaria total_stat: 590
Number: 354 name: Mega Banette total_stat: 555
Number: 359 name: Mega Absol total_stat: 565
Number: 362 name: Mega Glalie total_stat: 580
Number: 373 name: Mega Salamence total_stat: 700
Number: 376 name: Mega Metagross total_stat: 700
Number: 380 name: Mega Latias total_stat: 700
Number: 381 name: Mega Latios total_stat: 700
Number: 384 name: Mega Rayquaza total_stat: 780
Number: 428 name: Mega Lopunny total_stat: 580
Number: 445 name: Mega Garchomp total_stat: 700
Number: 448 name: Mega Lucario total_stat: 625
Number: 460 name: Mega Abomasnow total_stat: 594
Number: 475 name: Mega Gallade total_stat: 618
Number: 531 name: Mega Audino total_stat: 545
Number: 719 name: Mega Diancie total_stat: 700

Number: 3 name: Venusaur total_stat: 525
Number: 6 name: Charizard total_stat: 534
Number: 9 name: Blastoise total_stat: 530
Number: 15 name: Beedrill total_stat: 395
Number: 18 name: Pidgeot total_stat: 479
Number: 65 name: Alakazam total_stat: 500
Number: 80 name: Slowbro total_stat: 490
Number: 94 name: Gengar total_stat: 500
Number: 115 name: Kangaskhan total_stat: 490
Number: 127 name: Pinsir total_stat: 500
Number: 130 name: Gyarados total_stat: 540
Number: 142 name: Aerodactyl total_stat: 515
Number: 150 name: Mewtwo total_stat: 680
Number: 181 name: Ampharos total_stat: 510
Number: 208 name: Steelix total_stat: 510
Number: 212 name: Scizor total_stat: 500
Number: 214 name: Heracross total_stat: 500
Number: 229 name: Houndoom total_stat: 500
Number: 248 name: Tyranitar total_stat: 600
Number: 254 name: Sceptile total_stat: 530
Number: 257 name: Blaziken total_stat: 530
Number: 260 name: Swampert total_stat: 535
Number: 282 name: Gardevoir total_stat: 518
Number: 302 name: Sableye total_stat: 380
Number: 303 name: Mawile total_stat: 380
Number: 306 name: Aggron total_stat: 530
Number: 308 name: Medicham total_stat: 410
Number: 310 name: Manectric total_stat: 475
Number: 319 name: Sharpedo total_stat: 460
Number: 323 name: Camerupt total_stat: 460
Number: 334 name: Altaria total_stat: 490
Number: 354 name: Banette total_stat: 455
Number: 359 name: Absol total_stat: 465
Number: 362 name: Glalie total_stat: 480
Number: 373 name: Salamence total_stat: 600
Number: 376 name: Metagross total_stat: 600
Number: 380 name: Latias total_stat: 600
Number: 381 name: Latios total_stat: 600
Number: 384 name: Rayquaza total_stat: 680
Number: 428 name: Lopunny total_stat: 480
Number: 445 name: Garchomp total_stat: 600
Number: 448 name: Lucario total_stat: 525
Number: 460 name: Abomasnow total_stat: 494
Number: 475 name: Gallade total_stat: 518
Number: 531 name: Audino total_stat: 445
Number: 719 name: Diancie total_stat: 600
For Non Mega:
Count: 46 Total stats: 23638

For Non Mega:
Count: 46 Total stats: 23638




"""