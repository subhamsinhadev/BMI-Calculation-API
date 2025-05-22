from flask import Flask ,jsonify,render_template
import socket

app=Flask(__name__)


@app.route('/api/')
def home():
    return render_template("index.html")
@app.route('/api/bmi/<weight>/<height>',methods=["GET"])
def calcbmi(weight,height):
    try:
        weight=float(weight)
        height=float(height)
    except ValueError:
        return jsonify({"error":"Invalid parameters. Please provide numeric values for weight and height."})
        
    
    
  

    if height==0:
        return jsonify({"Error":"Height parameter cannot be Zero"}),400
    bmi=weight/height**2
    cat=bmi_class(bmi)
    

    return jsonify({"weight":weight,
                    "height":height,
                    "bmi":round(bmi,3),
                    "Category":cat})

    

    
def bmi_class(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"

if __name__== '__main__':
    host=socket.gethostbyname(socket.gethostname())
    app.run(debug=True,host="0.0.0.0",port=5000)
