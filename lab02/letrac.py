import random
import numpy as np

def randSlots():
    result=[]
    for i in range (0,3):
        result.append(random.choice(["bar", "bell", "lemon", "cherry"]))
    return result

def game(number_of_coins):
    #print("init game()")
    coins=number_of_coins
    jogos=0
    while True:
        jogos+=1
        coins-=1
        if coins < 1:
            return jogos
        else:
            result=randSlots()
           # print("valor da roleta {} e valor de moedas {}\n".format(result,coins))
            if(result[0]=='bar' and result[1]=='bar' and result[2]=='bar'):
                coins= coins+21
            if(result[0]=='bell' and result[1]=='bell' and result[2]=='bell'):
                coins= coins+16
            if(result[0]=='lemon' and result[1]=='lemon' and result[2]=='lemon'):
                coins= coins+5
            if(result[0]=='cherry' and result[1]=='cherry' and result[2]=='cherry'):
                coins= coins+3
            if(result[0]=='cherry' and result[1]=='cherry' and result[2]!='cherry'):
                coins= coins+2
            if(result[0]=='cherry' and result[1]!='cherry'):
                coins= coins+1
            
            
    

def numberOfGames(number):
    jogos=[]
    for i in range (0,number):
        jogos.append(game(8))
    somatorio= np.sum(jogos)
    print(f"soma dos jogos = {somatorio} e o total de jogos é = {number}\n")
    media = np.mean(jogos)
    mediana =  np.median(jogos)
    print(f"media é ={media} e o valor da mediana é = {mediana}\n")
        

numberOfGames(1000)