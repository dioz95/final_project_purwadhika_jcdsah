from flask import Flask, render_template, request

# import plotly adalah library untuk membuat plot
import plotly
import plotly.graph_objs as go

# import pandas sebagai pengolah data
import numpy as np
import pandas as pd  
import json 
import pickle

# maemangiil flask sebagai aplikasi
app = Flask(__name__)

# Load Data
df = pd.read_csv('./static/train.csv')

# Function to plot Age distribution
def age_plot():

    data = [
        go.Box(x=df[df['Response'] == 1]['Age'], name='Potential'),
        go.Box(x=df[df['Response'] == 0]['Age'], name='Non-Potential')
    ]

    layout = go.Layout(
        title = 'Age vs Response',
        title_x = 0.5,
        xaxis = dict(title='Age')
    )

    result = {"data": data, "layout": layout}
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

## Create route for Age Distribution exch
@app.route('/')
def index():

    plot = age_plot()

    return render_template(
        'age_visualization.html',
        plot = plot
    )

@app.route('/age_visualization')
def age_visualization():

    plot = age_plot()

    return render_template(
        'age_visualization.html',
        plot = plot
    )

##### Annual Premium #####
def anp_plot():
    filtered_entries = np.array([True] * len(df))

    col = 'Annual_Premium'
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    low_limit = Q1 - (IQR * 1.5)
    high_limit = Q3 + (IQR * 1.5)

    filtered_entries = ((df[col] >= low_limit) & (df[col] <= high_limit)) & filtered_entries
    df_no_out = df[filtered_entries]

    data = [
        go.Box(x=df['Annual_Premium'], name='With Outliers'),
        go.Box(x=df_no_out['Annual_Premium'], name='No Outliers')
    ]

    layout = go.Layout(
        title = 'Effect on Outliers Removal on Annual Premiums Variable',
        title_x = 0.5,
        xaxis = dict(title='Annual Premium')
    )

    result = {"data": data, "layout": layout}
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

# Create route for anp_plot
@app.route('/anp_visualization')
def anp_visualization():

    plot = anp_plot()

    return render_template(
        'anp_visualization.html',
        plot = plot
    )

####### Previously Insured #####
def pi_plot():
    df_copy = df.copy()
    df_copy['Response'] = df_copy['Response'].apply(str)
    df1 = pd.crosstab(index=df_copy['Previously_Insured'], columns=df_copy['Response'])
    pi = ['Not-Insured', 'Previously-Insured']

    data = [
        go.Bar(
            name = "Not-Potential",
            x = pi,
            y = df1['0'],
            offsetgroup = 0
        ),
        go.Bar(
            name = "Potential",
            x = pi,
            y = df1['1'],
            offsetgroup = 1
        )
    ]

    layout = go.Layout(
        title = 'Previously Insured vs Response',
        # yaxis_title="Count of Customers",
        title_x = 0.5
    )
    
    result = {"data": data, "layout": layout}
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

# Create route for PI Visualization
@app.route('/pi_visualization')
def pi_visualization():
    plot = pi_plot()

    return render_template(
        'pi_visualization.html',
        plot=plot
    )

#####  SHOW DATA ######
def show_data():
    df2 = df[:100].set_index('id') 

    return df2

# Create route for data
@app.route('/data')
def data():

    sample = show_data()

    return render_template(
        'data.html',
        data = sample.to_html()
    )

######## PREDICTION #########
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    return render_template('predict.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        input = request.form

        df_predict = pd.DataFrame({
            'Gender': [input['ge']],
            'Age':[input['Age']],
            'Driving_License':[input['dl']],
            'Previously_Insured':[input['va']],
            'Vehicle_Age':[input['va']],
            'Vehicle_Damage':[input['vd']],
            'Annual_Premium':[input['Annual Premium']],
            'Vintage':[input['Vintage']]
        })

        prediksi = model.predict_proba(df_predict)[0][1].round(3)

        if prediksi > 0.5:
            response = "Potenial"
        else:
            response = "Not-Potential"

        return render_template('result.html',
            data=input, pred=response, prob=prediksi)

# jalankan fungsi ketika file py ini dipanggil
if __name__=='__main__':
    filename = 'estimator_deploy.sav'
    model = pickle.load(open(filename,'rb'))

    app.run(debug=True, port=5000)