import random
a=['1) Which country became the first Arab nation to host the FIFA World Cup? a) Qatar b) Egypt',
'2) Who is the current Secretary-General of the United Nations?  a) António Guterres b) Tedros Adhanom Ghebreyesus',

'3.Which two countries recently signed a historic peace agreement ending a longstanding conflict? a) Colombia and the FARC b) North Korea and South Korea',
'4. **Which international organization currently faces criticism for its handling of the war in Ukraine? a) NATO b) United Nations',
'5. **Who is the current President of the United States of America? a) Joe Biden b) Kamala Harris ',
'6. **Which global economic indicator is currently experiencing a significant downturn? a) Gross Domestic Product (GDP)  b) Unemployment Rate',
'7. **Which cryptocurrency recently suffered a major collapse, impacting the entire market? a) Bitcoin b) Ethereum']
ans_a=['a','b','a','b','b','a','a']
b=[ i for i in range(len(a))]
def gk():
    c=random.shuffle(b)
    marks=0
    for j in b:
        print(a[j])
        guess=input('Enter only options').lower()
        if guess==ans_a[j]:
            marks=marks+1
            print('correct')
        else:
            print('Incorrect!')
    print('Obtained marks:',marks)
gk()

    
