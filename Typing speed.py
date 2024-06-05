from time import * 
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error=error+1
        except :
             error=error+1
    return error 

def speed_time(time_s,time_e,userinput):
    time_delay=time_e - time_s
    time_R= round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)


while True:
  ck=input("Ready for test: Yes/No")
  if ck=="Yes":
        
        
        test=["I love wild animals. In cities only place to see them is zoo. Last week I got a chance to visit zoo when my elder brother planned a picnic along with his two friends. We reached there at 10 am. Zoo was divided into many sections like apes, birds, reptiles, butterflies, beast of prey etc. We tried to cover each section. But once we entered the birds section, we lost so much that we spent many hours there. We could hardly cover half section. By the evening we were very tired. We came out and took some snacks. Sweet memory of that day is still fresh in my mind.",
              "A friend in need is a friend indeed! A true friend will be one who will stay by your side at all times. A real friend stays by you through thick and thin.A true friend should be cherished and whose friendship should be safeguarded. Losing a true friend is like losing a treasure. And you may never recover the wealth you lose. A true friend is difficult to come by. So value the friendship of such a friend. Most of all, reciprocate the love your friend has for you. And give your friend a special place in your heart.","Girls’ education and gender equality is very important for strengthening the society and lowering crime rates; but girl’s education today goes beyond just sending girls to school. It is also about ensuring girl’s safety while they are in school.Most of the parents in rural areas are now seem to be convinced in sending their girl child to school, but it is important that girls finish all necessary levels of education, learn extra skills and competencies for showcasing same level of competitiveness in the labour market. Education helps shape independent thinking of girls so as to enable them take decisions of their lives on their own and differentiate between right and wrong so that they are able to contribute towards societal development.",
              "Books are an important part of our life. We read many kinds of books. We study text books at school that are part of our syllabus.We also have story books that we read for leisure and fun. We can get them from the school library. We can also buy them from bookshops. Books are printed on paper, and can have pictures too that make them interesting. We can read books on the computer as well.I love reading children’s stories published in colourful books, as they are beautifully presented. I have a nice collection of story books at home."]

        test1=r.choice(test)
        print("Typing Speed")
        print(test1)
        print()
        print()
        time_1=time()
        testinput=input("Enter:-")
        time_2=time()

        print('Speed:', speed_time(time_1,time_2,testinput),"w/sec")
        print("Error:",mistake(test1,testinput))

  elif ck=="No":
        print("Thank You!!!")
        break
 
  else:
        print("Wrong Input")
      
      