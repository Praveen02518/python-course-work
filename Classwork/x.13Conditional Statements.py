#12. Conditional Statements

#1.if Statement
s=input("Enter the status(R O G) : ")

if s=='R':
    print("Stop")

if s=='O':
    print("Get Ready!")

if s=='G':
    print("Goooo0")
    
#2.if-else Statement

gadgets=['Anywhere door','small light','big light','magic pencil','helicopter','toycar']

print('Hey User Welcome to the Doraemon Store'.center(50,'-'))
searchinput=input("Enter the gadgets:").lower()

if searchinput in gadgets:
    print(f"{searchinput} found. Buy now!!!")
else:
    print(f'{searchinput} is in repair now. Come later...')    

#3.if-elif-else Statement

#Weekend Budget Plan
amount=int(input("Enter the Weekend Budget: "))
if amount>20000:
    print("Trip to Manali")
elif amount>15000:
    print("Go for Goa")
elif amount>5000:
    print("Araku")
elif amount>2000:
    print("Dinner Date")
elif amount>1000:
    print("Movie Date")
elif amount>500:
    print("Long Drive")
elif amount>100:
    print("Save the money for next weekend brooo!")
else:
    print("You can't even buy Alekhya Chitti pickles... Earn more brooo!")
    
#4. Nested Conditional Statements

#Influencer level Detection...

followers = int(input("Enter your Instagram followers count: "))
print("Welcome to the Instagram Kiddooo...\nThanks for using Instagram!")
if followers > 0:
    print("...")
    if followers>1000000:
        print("You're an Influencer God!!! Salaam Rocky Bhai")
    elif followers>100000:
        print("Influencer detected: CEO of Reels, Nice To Meet you Sarkaar!")
    elif followers>10000:
        print("Influencer detected: You can start earning now & buy Alekhya Chitti Pickles...")
    elif followers>1000:
        print("Just a reel away from going viral. Keep posting viral stuff!")
    elif followers>100:
        print("You can't buy Alekhya Chitti Pickles!!!")
    else:
        print("I know kiddooo that You’re here for fun")
else:
    print("No followers? Are You Stalking your EX brooo ??")
    
           