# An application which tells future based upon the zodiac sign

next = True
while next == True:
    print("Project created by Pratik Ledaskar")
    print(''' From all mentioned Zodiac Signs
    1) Aries
    2) Tauras
    3) Gemini
    4) Cancer
    5) Leo
    6) Virgo
    7) Libra
    8) Scorpio
    9) Saggitaraus
    10) Capricorn
    11) Aquarius
    12) Pisces
    ''')

    S = int(input("Pick your sign number and press Enter to know your future\n"))
    print(S)

    if S==1:
        print("Today you may receive some kind of material support from family.It is probably for a wise cause, so be sure to use it accordingly, says Ganesha. You may spend the evenings with those loved ones who have supported you.")
    elif S==2:
        print("There is a strong prospect that you will work extremely hard to prove yourself at your workplace today, predicts Ganesha. At times, the returns may not be in proportion to your efforts. You will unwind at the end of the day with a happy and content feeling, expects Ganesha.")
    elif S==3:
        print("Today the moon is positive. You may have some sort of energy; you may be able to perform at work efficiently. You may also help some needy person, which may create your prestige among people around you. You may spend your time studying intellectual stuff. You may also plan for higher study to groom your career." )
    elif S==4:
        print("Today until evening, you may be impatient, have a lack of confidence, which may reflect into your way of working. Parent's health may make you upset. Kids' notorious behaviour may make you upset. You should try to focus yourself and try to avoid scattering your energy into many holes. Investments in risky assets are advised to avoid now.")
    elif S==5:
        print("Today you may be happy. You are likely to plan for an overseas work-related journey, which will increase your business in the near future. Spending money on luxury stuff may improve your lifestyle. But you are advised not to drive yourself towards glamour or addictions; it may affect your financial health.")
    elif S==6:
        print("Today, you advised us to control your way of speaking, your harsh speaking may affect your family harmony. You may spend your hard-earned money in buying some worthless stuff to maintain your social status, it is advised to not to keep your money loose in the pocket.")
    elif S==7:
        print("Today, you may be busy in kid career or extracurricular activities. You may take some advice from someone to choose career options. You may meet consultants or specialists also. You may also hear good news regarding kids' results. You may also invest some capital into your family business.")
    elif S==8:
        print("Today you must control your way of speaking, shall be careful in terms of hidden enemies and opponents. You may be a victim of a conspiracy. It is advised to make investments in risky assets. You must avoid lending money to anyone; it may not be recoverable easily. You are advised to do meditation and yoga to come out from stress. Love birds are advised to be involved in controversies. Students are advised to work hard.")
    elif S==9:
        print("Today, job seekers may get a new job; there are chances of promotions in their current job. In the business, I may get new clients, which will be helpful in the growth in terms of profits. Singles are likely to find their good match. In domestic life, you must avoid hiding anything from your spouse; otherwise, it will create distance in your relationship.")
    elif S==10:
        print("Today is a day of success in terms of profession. Your plans are now going to give positive results in terms of profits. There may be good news related to your past investments in terms of gains. Your creativity may help you to improve your professional skills. Job seekers are likely to get a suitable job. Students may have good focus after self-analysis. You may be able to understand the feelings of your spouse.")
    elif S==11:
        print("Today until afternoon, you may be upset. Afternoon onwards elders blessings may protect you from this messy situation. Your willpower may help you to complete your delayed projects. It is advised to avoid arguments in domestic life. By the evening, you may have gained in terms of past investments.")
    elif S==12:
        print("Today, the moon is not positive, there are chances that you may not feel well, you might have health issues. You are advised not to make investments in new business projects, otherwise, you may face losses. Students are advised to avoid the fantasy and should work hard in their studies. You are also avoiding rash driving.")
    else:
        print("Are you sure about the number?")

       
    if input("\n Do you want to check it again? (Y/N) ")=="Y":
        next = True
    else:
        next = False
   