from fastapi import FastAPI
app = FastAPI()
path = r'C:/Users/JoshDev/Downloads/testset.csv'



#Date Lookup Endpoint

@app.get('/date-lookup/')
async def dateretreival(date):
    vals = ''
    for i in date:
        if i.isnumeric():
            vals+=i
    print(vals)
    val = ''
    val += vals[4:]
    val += vals[2:4]
    val+= vals[:2]
    print(val)
    with open(path) as file:
        out = []
        for i in file:
            dates = i[:8]
            if val == dates:
                out.append(i)
        if len(out) > 1:
            return out       
    return 'Not Found In Database'


#Month Lookup Endpoint

@app.get('/month-lookup/')
async def dateretreival(month):
    with open(path) as file:
        out = []
        for i in file:
            dates = i[4:6]
            if month == dates:
                out.append(i)
        if len(out) > 1:
            return out       
    return 'Not Found In Database'


#Highest Temperature per Month Endpoint (Default 0)
@app.get('/high-temp')
async def extract_high(year):
    entire_year = []
    months={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    temperatures = []
    c = 0
    with open(path) as file:
        for i in file:
            if c == 0:
                c+=1
                pass
            cyear = i[0:4]
            if year == cyear:
                cmonth = int(i[4:6])
                it = i.split(',')
                if it[11].isnumeric():
                    if months[cmonth] < int(it[11]):
                        months[cmonth] = int(it[11])
                else:
                    pass   


        return months


                    
 #Median Temperature per Month Endpoint (Default [])                   

@app.get('/median-temp')
async def extract_median(year):
    months={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
    temps={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
    c = 0
    with open(path) as file:
        for i in file:
            if c == 0:
                c+=1
                pass
            cyear = i[0:4]
            if year == cyear:
                cmonth = int(i[4:6])
                it = i.split(',')
                if it[11].isnumeric():
                    months[cmonth].append(it[11])
                else:
                    pass   
        for i in range(1,13):
            months[i].sort()
            s = months[i]
            if len(s) == 0:
                pass

            median = s[len(s)//2]
            temps[i] = median

        return temps




#Minimum Temperature per Month Endpoint (Default 9999)

@app.get('/minimum-temp')
async def extract_minimum(year):
    entire_year = []
    months={1:9999,2:9999,3:9999,4:9999,5:9999,6:9999,7:9999,8:9999,9:9999,10:9999,11:9999,12:9999}
    temperatures = []
    c = 0
    with open(path) as file:
        for i in file:
            if c == 0:
                c+=1
                pass
            cyear = i[0:4]
            if year == cyear:
                cmonth = int(i[4:6])
                it = i.split(',')
                if it[11].isnumeric():
                    if months[cmonth] > int(it[11]):
                        months[cmonth] = int(it[11])
                else:
                    pass   


        return months
