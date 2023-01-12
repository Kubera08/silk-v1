
import pandas as pd

influs = pd.read_csv("Influs.csv")
restos = pd.read_csv("Restos.csv")

resto_name = input("Entrez le nom du restaurant : ")

index = 0
i = 0

for i in range (len(restos.NOM)):
	if(restos.iloc[i]["NOM"] == resto_name):
		index = i
		
resto_age = restos.iloc[index]["AGE"]
resto_lieu = restos.iloc[index]["LIEU"]
resto_abo = restos.iloc[index]["ABO"]

influscheck = influs[(influs["AGE"] == (resto_age)) & (influs["LIEU"] == (resto_lieu)) & (influs["ABO"] == (resto_abo))]

 ## Le premier [] correspont à la ligne du resto pour lequel on cherche un infu et le deuxiême le critère qu'on analyse

influsname = influscheck["NOM"]

# on stock dans une variable les noms des influs correspondant 
if (len(influsname) == 0 ):
	print("Aucuns influenceurs ne correspond à ces critères")
if (len(influsname != 0)):
	print("les personnes correspondant aux critères du restaurant", resto_name, "sont", influsname)

influsname.to_csv("results")