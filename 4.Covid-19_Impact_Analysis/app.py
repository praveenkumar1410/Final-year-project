from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')
def covid_impact_analysis():
    # Importing the Libraries
    # Loading and Processing the Data
    data = pd.read_csv("transformed_data.csv")
    data2 = pd.read_csv("raw_data.csv")

    data["COUNTRY"].value_counts().mode()

    # Aggregating the data

    code = data["CODE"].unique().tolist()
    country = data["COUNTRY"].unique().tolist()
    hdi = []
    tc = []
    td = []
    sti = []
    population = data["POP"].unique().tolist()
    gdp = []

    for i in country:
        hdi.append((data.loc[data["COUNTRY"] == i, "HDI"]).sum()/294)
        tc.append((data2.loc[data2["location"] == i, "total_cases"]).sum())
        td.append((data2.loc[data2["location"] == i, "total_deaths"]).sum())
        sti.append((data.loc[data["COUNTRY"] == i, "STI"]).sum()/294)
        population.append((data2.loc[data2["location"] == i, "population"]).sum()/294)

    aggregated_data = pd.DataFrame(list(zip(code, country, hdi, tc, td, sti, population)), 
                                   columns = ["Country Code", "Country", "HDI", 
                                              "Total Cases", "Total Deaths", 
                                              "Stringency Index", "Population"])

    data = aggregated_data.sort_values(by=["Total Cases"], ascending=False)

    data = data.head(10)

    data["GDP Before Covid"] = [65279.53, 8897.49, 2100.75, 
                                11497.65, 7027.61, 9946.03, 
                                29564.74, 6001.40, 6424.98, 42354.41]
    data["GDP During Covid"] = [63543.58, 6796.84, 1900.71, 
                                10126.72, 6126.87, 8346.70, 
                                27057.16, 5090.72, 5332.77, 40284.64]

    # Analyzing the Spread of Covid-19
    cases = data["Total Cases"].sum()
    deceased = data["Total Deaths"].sum()

    labels = ["Total Cases", "Total Deaths"]
    values = [cases, deceased]

    death_rate = (data["Total Deaths"].sum() / data["Total Cases"].sum()) * 100

    return render_template('covid_impact_analysis.html',
                            title='Covid Impact Analysis',
                            labels=labels,
                            values=values,
                            death_rate=death_rate,
                            bar_fig1=px.bar(data, y='Total Cases', x='Country',title="Countries with Highest Covid Cases"),
                            bar_fig2=px.bar(data, y='Total Deaths', x='Country', title="Countries with Highest Deaths"),
                            bar_fig3=go.Figure(data=[go.Bar(x=data["Country"], y=data["Total Cases"], name='Total Cases'),
                                                     go.Bar(x=data["Country"], y=data["Total Deaths"], name='Total Deaths')],
                                              layout=go.Layout(title='Total Cases and Deaths by Country', barmode='group', xaxis_tickangle=-45)),
                            pie_fig=px.pie(data,











































'''from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analysis")
def analysis():
    # copy and paste the entire Covid_impact_analysis.ipynb code here
    return render_template("analysis.html")

if __name__ == "__main__":
    app.run(debug=True)'''