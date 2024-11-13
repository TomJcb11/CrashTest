def load_custom_css():
    custom_css = """
    <style>
    .dataframe-container {
        width: 100%;
        height: 400px;
        overflow: auto;
    }
    .dataframe-container table {
        width: 100%;
        border-collapse: collapse;
    }
    .dataframe-container th {
        background-color: #FF0000;
        color: white;
    }
    .dataframe-container td, .dataframe-container th {
        border: 1px solid #ddd;
        padding: 8px;
    }
    </style>
    """
    return custom_css