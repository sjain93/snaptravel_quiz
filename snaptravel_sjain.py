# assuming input is a number and the program requests the user to input the details
#brute force method
def hotelrates(N, Q):
    n_list = []
    n2_list = []
    q_list = []
    q2_list = []
    out = {}
    for i in range(0,N):
        n_list.append(input("Please enter City,Vendor,rate")) #alternatively use list comprehension
        n2_list.append(n_list[i].split(','))
    for i in range(0,Q):
        q_list.append(input("Please enter City,Days_till_check_in"))
        q2_list.append(q_list[i].split(','))
    
    for query in q2_list:
        for rate in n2_list:
            if query[0] not in rate:
                if n2_list.index(rate) == len(n2_list) - 1:
                    out[query[0]] == None
                continue
            else:
                if rate[1] == 'A' and query[1] == 1:
                    if out.get(query[0]):
                        out[query[0]].append(int(rate[2])*1.5)
                    else:
                        out[query[0]] == [int(rate[2])*1.5]
                    out[query[0]].sort()
                elif rate[1] == 'B' and query[2] < 3:
                    if out.get(query[0]):
                        out[query[0]].append(None)
                    else:
                        out[query[0]] == [None]
                    out[query[0]].sort()
                elif rate[1] == 'C' and query[2] >= 7:
                    if out.get(query[0]):
                        out[query[0]].append(0.9*int(rate[2]))
                    else:
                        out[query[0]] == [0.9*int(rate[2])]
                    out[query[0]].sort()
                elif rate[1] == 'D' and query[2] <= 7:
                    if out.get(query[0]):
                        out[query[0]].append(1.1*int(rate[2]))
                    else:
                        out[query[0]] == [1.1*int(rate[2])]
                    out[query[0]].sort()
                else:
                    if out.get(query[0]):
                            out[query[0]].append(int(rate[2]))
                    else:
                        out[query[0]] == [int(rate[2])]
                    out[query[0]].sort()
        
        print(out[query[0]])
                



    

    



# Sample input params

'''
7
Toronto, A, 100.00
North York, B, 250
Waterloo, C, 19.99
Toronto, D, 100.00
Kitchener, F, 25
Kitchener, F, 24
Kitchener, F, 25

4
Toronto, 1
North York, 2
Waterloo, 8
Kitchener, 10
'''
