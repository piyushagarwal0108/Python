flamess = {"friends":"best friends always together","love":"wah wah ram ji...jodi kya banai","affectionate":"ek tarfa pyaar ki ....baat he kuch aur hoti hai,\nits the most beautiful feeling in the world","marriage":"milan abhi aadha, adhura hai...love birds","enemies":"ladai ladai maaf karo... pyari se ek takraar karo","sister":"bhaiya mere rakhi ka bandhan tum nibhana...hehe"}
print("This is the Realtion Calculator")
import sys
flames = ["friends","love","affectionate","marriage","enemies","siblings"]
boy = list(input("enter name of boy: ").lower())
girl = list(input("enter name of girl: ").lower())
try:
    common = [i for i in boy if i in girl]
    common = set(common)  
except:
    print("huh...you are just friends")
    sys.exit()
for i in common:
    boy.remove(i)
    girl.remove(i)
total_similar = len(boy)+len(girl)
while(len(flames)!=1):
    count = (total_similar%len(flames))-1
    if count>0:
        right = flames[count+1:]
        left = flames[:count]
        flames = right+left
    else:
        flames = flames[:len(flames)-1]
print(flames[0])
print(flamess[flames[0]])
        
        
    
    
    
    
    
