#while loop count down from 50 to 10 and another to print a word untill you input one secret word
num = 50
while num>=10:
    print (num)
    num-=5
user_input = "not_the_pasword"
while user_input != "Pasword":
    print ("What's the pasword?")
    user_input = input()
#list review

things_I_like = ["The Amazing Digital Circus", "Warframe songs", "Citizen Solder"]
print (things_I_like)
things_I_like.append("Rosendale")
print (things_I_like)
things_I_like.sort()
print (things_I_like)
things_I_like.remove("The Amazing Digital Circus")
print (things_I_like)
