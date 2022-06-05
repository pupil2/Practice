def wabbit (a1 ,a2 ):#line:1
    R1 =[1 ,0 ]#line:2
    a3 =1 #line:3
    while a3 <a1 :#line:4
        R1 .insert (0 ,sum (R1 [1 :a2 ]))#line:5
        a3 +=1 #line:6
    print (sum (R1 [0 :a2 ]))
