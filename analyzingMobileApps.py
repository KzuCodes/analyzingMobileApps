import csv
import math
rutaAndroid= "data/googleplaystore.csv"
rutaApple="data/AppleStore.csv"
apple = open(rutaApple, "r")
datosAndroid=[]
datosApple=[]

def parseoAndroid():
    with open (rutaAndroid, "r") as csv_file:
        android = csv.reader(csv_file)
        first=0
        
        for linea in android:
            
            if(first==0):
                columnTitles=linea
                first+=1
                datosAndroid.append(columnTitles)
            else:
                if(len(linea)==13):
                    appName=linea[0]
                    category=linea[1]
                    rating = float(linea[2])
                    reviews = int(linea[3])
                    size = linea[4]
                    installs = linea[5]
                    type = linea[6]
                    price = float(linea[7].replace("$",""))
                    contentRating= linea[8]
                    genres= linea[9]
                    lastUpdated= linea[10]
                    currentVersion=linea[11]
                    androidVersion=linea[12]
                    lineaParseada = (appName, category, rating, reviews,size,installs, type,price,contentRating,genres,lastUpdated,currentVersion,androidVersion)
                    datosAndroid.append(lineaParseada)
    return datosAndroid


def parseoApple():
    with open (rutaApple, "r") as csv_file:
        apple = csv.reader(csv_file)
        first=0

        for linea in apple:
            if(first==0):
                columnTitle=linea
                first+=1
                datosApple.append(columnTitle)
            else:

                if len(linea)==16:
                    id = int(linea[0])
                    trackName = linea[1]
                    sizeBytes = linea[2]
                    currency = linea[3]
                    price = float(linea[4].replace("$",""))
                    ratingCountTot = linea[5]
                    ratingCountVer = linea[6]
                    userRating = linea[7]
                    userRatingVer = linea[8]
                    version = linea[9]
                    contRating = linea[10]
                    primeGenre = linea[11]
                    supDevicesNum = linea[12]
                    ipadScUrlsNum = linea[13]
                    langNum = linea[14]
                    vppLic = linea[15]
                    lineaParseada=(id, trackName, sizeBytes, currency, price, ratingCountTot, ratingCountVer, userRating, userRatingVer, version, contRating, primeGenre, supDevicesNum, ipadScUrlsNum, langNum, vppLic)   
                    datosApple.append(lineaParseada)
    return datosApple


    

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

#print(explore_data(parseoAndroid(),0,len(parseoAndroid()), True))
#print(explore_data(parseoApple(),0,len(parseoApple()), True))
#print(explore_data(parseoApple(),0,1))
#print(explore_data(parseoAndroid(),0,1))


##Although the way of collecting the data has some error-solving, there are some duplicates. We will eliminate the rows with less reviews.
def eliminatingDuplicates(dataset):
    uniqueApps=[]
    duplicatedApps=[]
    for app in dataset:
        if(app[0] in uniqueApps):
            duplicatedApps.append((app[0]))
        else:
            uniqueApps.append(app[0])
    #print(len(duplicatedApps))

    max_reviews = dict()
    for app in parseoAndroid():
        name = app[0]
        n_reviews= app[3]
        if name in max_reviews.keys() and max_reviews[name]<n_reviews:
            max_reviews[name]=n_reviews
        if name not in max_reviews.keys():
            max_reviews[name]=n_reviews

   ### POR SI SIRVE LUEGO duplicatedApps= duplicatedApps.sort(key=lambda a:   a[1])
    androidClean=[]
    alreadyAdded=[]
    for app in parseoAndroid():
        name = app[0]
        numRev = app[3]
        if numRev==max_reviews[name] and name not in alreadyAdded:
            androidClean.append(app)
            alreadyAdded.append(name)
    return androidClean


#print(len(eliminatingDuplicates(parseoAndroid())))

def eliminatingNonEnglish(str):
    eng=True
    sum=0
    for char in str:
        if ord(char)>127:
            sum+=1
    if sum>3:
        eng=False
    return eng

# print(eliminatingNonEnglish('Instagram'))
# print(eliminatingNonEnglish('爱奇艺PPS -《欢乐颂2》电视剧热播'))
# print(eliminatingNonEnglish('Docs To Go™ Free Office Suite'))
# print(eliminatingNonEnglish('Instachat 😜'))

def cleanDatasets(dataset):
    res=[]
    for app in dataset:
        if len(app)>13:
            name = app[1]
        else:
            name = app[0]
        if eliminatingNonEnglish(name)==True:
            res.append(app)
    return res

#print(len(cleanDatasets(parseoApple())))

def gettingFreeApps(dataset):
    res=[]
    first=True
    for app in dataset:
        if(first==True):
            first=False
        else:

            if len(app)>13:
                price=app[4]
            else: 
                price = app[7]
            if math.isclose(price, 0.0):
                res.append(app)
    return res

#print(len(gettingFreeApps(parseoApple())))

def freqTable(dataset, index):
    res=dict()
    for app in dataset:
        genre=app[index]
        if genre not in res.keys():
            res[genre]=1
        else:
            res[genre]+=1
    for key in res.keys():
        res[key]=(res[key]/(len(dataset)-1))*100
    return res

def display_table(dataset, index):
    table = freqTable(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0]) 


print(display_table(parseoApple(),11))