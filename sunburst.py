import plotly.express as px
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv("changes.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
fig = px.sunburst(
        data_frame=df,
        path=["regulation", 'Class', "Subclass","Compound"],  # Root, branches, leaves
    #color="Class",
    #color_discrete_sequence=px.colors.qualitative.Pastel,
        color="p value",
        color_continuous_scale=px.colors.sequential.Blackbody,
        range_color=[0,0.05],
    #tile="Distribution of differential features",
                        )

fig2 = px.sunburst(
        data_frame=df,
        path=["regulation", 'Class', "Subclass","Compound"],  # Root, branches, leaves
        color="Fold-change",
        color_continuous_scale=px.colors.diverging.Picnic,#amb aixo posem una escala de -1 a +1 (divergent
        color_continuous_midpoint=0,#amb aixo declarem quin es el punt mig de la escala
    #tile="Distribution of differential features",
        )

app.layout = html.Div([
    html.H6("Changes induced in plasma by low AGE diet"),
    html.Div([dcc.Markdown("According p value"),
                    dcc.Graph(id='prob',figure=fig),
              dcc.Markdown("According fold change"),
                    dcc.Graph(id='foldch',figure=fig2)],style={'columnCount': 2},
    ),dcc.Markdown("Annotation is based on exact mass, retention time and isotopic distribution *: confirmed by MS/MS, a: FDR corrected p-value < 0.05. FA: fatty Acyls, GL: glycerolipids, GP: glycerophospholipids, SP: sphingolipids, MG: monoacylglycerol, DG: diacylglycerol, TG: triglyceride,  PA: Phosphatidic acid, PC: Phosphatidylcholine, PE: Phosphatidylethanolamine, PG: Phosphatidylglycerol, PS: Phosphatidylserine ,  Ether lipids may be found as ‘plasmanyl’ (also termed alkyl ethers, and represented by the ‘O-‘ prefix), and as ‘plasmenyl’ (also termed alkenyl ethers or plasmalogens, and represented by the ‘P-‘ prefix)")])

if __name__ == '__main__':
    app.run_server(debug=True)
