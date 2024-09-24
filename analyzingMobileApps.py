import csv
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
                    id = linea[0]
                    trackName = linea[1]
                    sizeBytes = linea[2]
                    currency = linea[3]
                    price = linea[4]
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
                    datosApple.append(lineaParseada=(columnTitle[0],columnTitle[1],columnTitle[2],columnTitle[3],columnTitle[4],columnTitle[5],columnTitle[6],columnTitle[7],columnTitle[8],columnTitle[9],columnTitle[10],columnTitle[11],columnTitle[12],columnTitle[13],columnTitle[14],columnTitle[15]))

                
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
print(explore_data(parseoApple(),0,len(parseoApple())))