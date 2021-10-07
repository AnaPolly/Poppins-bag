friend_1_name = "Isa Pereira"
friend_1_email = "isa.pereira@example.com"
friend_1_age = 38
friend_1_the_best = True 

friend_1 = [friend_1_name , friend_1_email , friend_1_age , friend_1_the_best]


friend_2_name = "Dri Renno"
friend_2_email = "dri.renno@example.com"
friend_2_age = 38
friend_2_the_best = True 

friend_2 = [friend_2_name , friend_2_email , friend_2_age , friend_2_the_best]


friend_3_name = "Si Fernandes"
friend_3_email = "si.fernandes@example.com"
friend_3_age = 40
friend_3_the_best = True 

friend_3 = [friend_3_name , friend_3_email , friend_3_age , friend_3_the_best]


friend_4_name = "Rafa Selem"
friend_4_email = "rafa.selem@example.com"
friend_4_age = 38
friend_4_the_best = True 

friend_4 = [friend_4_name , friend_4_email , friend_4_age , friend_4_the_best]


friend_5_name = "Anita Chorny"
friend_5_email = "anita.chorny@example.com"
friend_5_age = 39
friend_5_the_best = True 

friend_5 = [friend_5_name , friend_5_email , friend_5_age , friend_5_the_best]


friend_6_name = "Ze Flores"
friend_6_email = "ze.flores@example.com"
friend_6_age = 37
friend_6_the_best = False

friend_6 = [friend_6_name , friend_6_email , friend_6_age , friend_6_the_best]


friend_7_name = "Nat Lopes"
friend_7_email = "nat.lopes@example.com"
friend_7_age = 40
friend_7_the_best = False

friend_7 = [friend_7_name , friend_7_email , friend_7_age , friend_7_the_best]


list = []

list.append(friend_1)
list.append(friend_2)
list.append(friend_3)
list.append(friend_4)
list.append(friend_5)
list.append(friend_6)
list.append(friend_7)

print (list, end="\n\n\n")


i=0

for i in list:
    print (i[0] , "is", i[2], "years old.", "Email:", i[1], end="\n\n")


for i in list:
    if i[3]:
        print (i[0], "is one of my besties.") 
