while True:
        p=int(input('Factors for :'))
        x=range(1,p+1)
        for i in x:
                if p/i in x:
                        print(i)
                else:
                        continue
