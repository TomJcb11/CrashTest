import plotly.graph_objects as go

def create_colored_world_map(df, selected_indicator, year, show_ocean, projection_type, colorscale):
    df_filtered = df[df['year'] == year]
    df_pivot = df_filtered.pivot_table(index='country', values=selected_indicator, fill_value=0).reset_index()
    
    # Vérifiez que la colonne selected_indicator existe dans le DataFrame pivoté
    if selected_indicator not in df_pivot.columns:
        raise KeyError(f"L'indicateur sélectionné '{selected_indicator}' n'existe pas dans les données pour l'année {year}.")
    
    countries = df_pivot['country'].tolist()
    values = df_pivot[selected_indicator].tolist()
    links = [f'<a href="/?country={country}" target="_self">{country}</a>' for country in countries]

    fig = go.Figure(go.Choropleth(
        locationmode='country names',
        locations=countries,
        z=values,
        text=links,
        colorscale=colorscale,
        showscale=True,
        marker_line_color='black',
        marker_line_width=0.5,
        hovertemplate='%{text}  %{z}<extra></extra>'
    ))

    fig.update_geos(
        visible=True,
        resolution=110,
        showcountries=True,
        countrycolor="Black",
        showcoastlines=False,
        showland=True,
        landcolor="white",
        showocean=show_ocean,
        oceancolor="LightBlue" if show_ocean else "white",
        projection_type=projection_type
    )

    fig.update_layout(
        title_text='{} par Pays en {}'.format(selected_indicator, year),
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type=projection_type
        ),
        autosize=True,
        height=400
    )

    return fig