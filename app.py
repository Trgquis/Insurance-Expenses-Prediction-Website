from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('InsuranceExpensesFinal.pkl', 'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])

        sex = request.form['sex']
        if (sex == 'sex_male'):
            sex = 0
            # sex_female = 0
        else:
            sex = 1
            # sex_female = 1

        smoker = request.form['smoker']
        if (smoker == 'smoker_yes'):
            smoker = 1
            # smoker_no = 0
        else:
            smoker = 0
            # smoker_no = 1

        bmi = float(request.form['bmi'])
        children = int(request.form['children'])

        region = request.form['region']
        if (region == 'region_northwest'):
            region_northwest = 1
            region_southeast = 0
            region_southwest = 0
            region_northeast = 0
        elif (region == 'region_southeast'):
            region_northwest = 0
            region_southeast = 1
            region_southwest = 0
            region_northeast = 0
        elif (region == 'region_southwest'):
            region_northwest = 0
            region_southeast = 0
            region_southwest = 1
            region_northeast = 0
        else:
            region_northwest = 0
            region_southeast = 0
            region_southwest = 0
            region_northeast = 1

        
        print(type(age))
        values = np.array([[age,sex,smoker,bmi,children,region_northeast,region_northwest,region_southeast,region_southwest]])
        print(values)
        prediction = model.predict(values)
        prediction = round(prediction[0],2)


        return render_template('result.html', prediction_text=format(prediction))



if __name__ == "__main__":
    app.run(debug=True)