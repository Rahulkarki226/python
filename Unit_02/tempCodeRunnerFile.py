s="However, Ram has been in the news for all the wrong reasons too. Illiterate bigots have weaponized the slogan Jai Shri Ram for wanton acts of violence, crime and hatred, which are anathema to what Ram actually stands for. These lumpen elements do not know that Ram is maryada purushottam, the epitome of rectitude, the touchstone of impeccable behaviour, the role model of the perfect human being, and the very incarnation of saumya rasa, harmonious equilibrium"
total=0
list=s.split()
for i in list:
    if(i=="Ram"):
        total+=1
print(total)

 #5-Replace ‘Ram’ with ‘Shree Ram’ in above phrase
s1=s.replace("Ram","Shree Ram")
print(s1)

#6- Sort all the words in above phrase in descending order using string and list
list=s.split(" ")
list.sort(reverse=True)
string=""
for i in list:
    string =string +i +" "
s3=string.rstrip()
print(s3)
s4=str(list)
print(s4)

s4=str(list)
print(s4)
print(s4[0])