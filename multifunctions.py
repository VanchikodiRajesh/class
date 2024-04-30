class multiple():
    def subfields():
        print ("SUB- FIELDS IN AI are:")
        list="Machine Learning","Nueral Network","Vision","Robotics","Speech Processing","Natural Language processing"
    
        for temp in list:
            print (temp)  
    def check():
        number=int(input("enter the number"))
        if number%2==0:
            ans = "the given number is even number"
            print (ans)
        else:
            ans = "the given number is odd number"
            print (ans) 
            return ans
    def eligible():
        age=int(input("enter the age"))
        gender=input("enter the gender")
        if gender=="male" and age >=21:
            print ("your age=",age)
            print ("your gender",gender)
            print ("eligible")
        elif gender=="female" and age >=18:
            print ("your age=",age)
            print ("your gender",gender)
            print ("eligible")
        else:
            print ("your age=",age)
            print ("your gender",gender)
            print("not eligible")
    def percentage():
        tamil=int(input("enter your tamil mark"))
        english=int(input("enter your english mark"))
        maths=int(input("enter your maths mark"))
        science=int(input("enter your science mark"))
        social=int(input("enter your social  mark"))
        total=tamil+english+maths+science+social 
        Average=float(total/5)
        print("------------------------")
        print("MARKSHEET")
        print("------------------------")
        print("TAMIL     = ",tamil)
        print("ENGLISH   = ",english)
        print("MATHS     = ",maths)
        print("SCIENCE   = ",science)
        print("SOCIAL    = ",social)
        print("------------------------")
        print("TOTAL     = ",total)
        print("AVERAGE   = ",Average)
        print("------------------------")
          
    def area_of_triangle():
        height=float(input("enter the height"))
        breadth=float(input("enter the breath"))
        area=(height*breadth/2)
        print("--------------------------")
        print("AREA OF TRIANGLE")
        print ("--------------------------")
        print (" height             = ",height)
        print("breadth              =",breadth)
        print("Area of the triangle = " ,area)
        print("-----------------------------")
        
 
   
    def triangle():
        h1=int(input("enter the number h1"))
        h2=int(input("enter the  h2"))
        breadth=int(input("enter the breadth"))
        perimeter=(h1+h2+breadth)
        print("--------------------------")
        print("PERIMETER OF TRIANGLE")
        print ("--------------------------")
        print (" height1                 = ",h1)
        print (" height2                 = ",h2)
        print("breadth                   =",breadth)
        print("PERIMETER OF THE TRIANGLE = " ,perimeter)
        print("-----------------------------")

               
