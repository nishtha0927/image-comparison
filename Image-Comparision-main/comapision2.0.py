from PIL import Image

try:
    print("input the first image you want to compare with all")
    i1=  Image.open(str(input()))
    for i in range(1,2001):
        
        i2=Image.open(str(input()))
        pairs = zip(i1.getdata(), i2.getdata())
        if len(i1.getbands()) == 1:
            dif = sum(abs(p1-p2) for p1,p2 in pairs)
        else:
            dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
        ncomponents = i1.size[0] * i1.size[1] * 3
        if ((dif/255.0*100)/ncomponents)>5:
            print("******************************ALERT*************************\n\n")
            print (("Difference (percentage):"), (dif / 255.0 * 100)/ncomponents)
            print("\n**********************************************************")
        else:
            continue
         
except:
    print("wrong image extension or file name ")
    
    for i in range(1,2001):
        
        i2=Image.open(str(input()))
        pairs = zip(i1.getdata(), i2.getdata())
        if len(i1.getbands()) == 1:
            dif = sum(abs(p1-p2) for p1,p2 in pairs)
        else:
            dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
        ncomponents = i1.size[0] * i1.size[1] * 3
        if ((dif/255.0*100)/ncomponents)>5:
            print("******************************ALERT*************************\n\n")
            print (("Difference (percentage):"), (dif / 255.0 * 100)/ncomponents)
            print("\n**********************************************************")
        else:
            continue
    
   

        
        
    
    









