#! /usr/bin/env python3
import os
import requests

def generate_data():
    t_data = []
    count = 0
    for texts in os.listdir('supplier-data/descriptions/'):
        try:
            with open('supplier-data/descriptions/'+texts, 'r') as f:
                dd = [x.strip(' lbs') for x in f.read().splitlines() if x != '']
                dd.append(os.listdir('supplier-data/images/')[count])
            f.close()
            labels = ['name','weight','description','image_name']
            t_data.append({x:y for x,y in zip(labels,dd)})
            t_data[count]['weight'] = int(t_data[count]['weight'])
            count+=1
        except:
            pass
        
    return t_data

def main():
    t_data = generate_data()
    for dat in t_data:
        try:
            response  = requests.post('http://[linux-instance-external-IP]/fruits', data=dat)
            print("Load Entry Successful")
        except:
            print ("Load Entry Unsuccessful")

if __name__ == '__main__':
    main()
