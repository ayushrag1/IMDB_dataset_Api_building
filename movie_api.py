from itertools import count
from flask import Flask,jsonify
import csv

with open('D:\projects\Movie_Dataset.csv', 'r') as file:
   reader = csv.DictReader(file, skipinitialspace=True)
   data=[]
   for l in reader:
    data.append(l)
count=1
app=Flask(__name__)
#print("hello_11111111111111111111111")
@app.route('/movie_data/<string:id>')
def api_calling(id):
    #print("hello_22222222222222222222")
    global count
    if(count<3):
        for movie in data:
            if(movie['Movie_id']==id):
                print("The current counter is:",count)
                count+=1
                return jsonify(movie)
        else:
            return jsonify("your entered id is not match!!!!")
            
    else:
        return jsonify("your access time is finished!!!")
            

if __name__ == "__main__":
    app.run(debug=True)