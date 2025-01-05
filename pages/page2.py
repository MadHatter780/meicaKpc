import streamlit as st
st.set_page_config(layout="wide")

# CSS untuk styling
st.markdown("""
    <style>
        /* Latar belakang aplikasi */
        [data-testid="stAppViewContainer"] {
            background-color: #f0f0f0;
        }

        /* Header Stream */
        .header {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px;
            border-radius: 10px;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        /* Stream container */
        .stream-container {
            background: rgba(0, 0, 0, 0.7); /* Hitam transparan */
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5); /* Efek bayangan */
        }

        /* Tabel */
        .table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }

        .table th, .table td {
            border: 1px solid #ccc;
            padding: 8px;
            text-align: center;
            font-size: 14px;
            color: white;
        }

        .table th {
            background-color: #555;
        }

        .status-run {
            color: white;
            background-color: lime;
            padding: 5px 10px;
            border-radius: 3px;
            font-weight: bold;
        }

        .status-stop {
            color: white;
            background-color: red;
            padding: 5px 10px;
            border-radius: 3px;
            font-weight: bold;
        }

        .info-row {
            background-color: rgba(255, 255, 255, 0.2);
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Fungsi untuk membuat tabel HTML
def generate_stream_html(header, data):
    table_html = f"""
        <div class="stream-container">
            <div class="header">{header}</div>
            <table class="table">
                <thead>
                    <tr>
                        <th>Unit</th>
                        <th>STATUS</th>
                        <th>TPH</th>
                    </tr>
                </thead>
                <tbody>
    """
    for row in data:
        status_class = "status-run" if row["STATUS"] == "RUN" else "status-stop"
        table_html += f"""
            <tr>
                <td>{row['Unit']}</td>
                <td><span class="{status_class}">{row['STATUS']}</span></td>
                <td>{row['TPH']}</td>
            </tr>
        """
    table_html += "</tbody></table></div>"
    return table_html

# Data STREAM-1
stream1_data = [
    {"Unit": "CV05", "STATUS": "RUN", "TPH": "3.500"},
    {"Unit": "CV07", "STATUS": "STOP", "TPH": "0"},
    {"Unit": "OLC-1", "STATUS": "RUN", "TPH": "4.000"},
    {"Unit": "RECLAIMING", "STATUS": "RUN", "TPH": "2.500"},
    {"Unit": "STACKING", "STATUS": "STOP", "TPH": "0"},
    {"Unit": "COAL QUALITY", "STATUS": "MELAWAN", "TPH": ""},
    {"Unit": "DESTINATION", "STATUS": "PORT", "TPH": ""},
]

# Data STREAM-2
stream2_data = [
    {"Unit": "CV05", "STATUS": "RUN", "TPH": "5.000"},
    {"Unit": "CV07", "STATUS": "STOP", "TPH": "0"},
    {"Unit": "OLC-1", "STATUS": "RUN", "TPH": "6.000"},
    {"Unit": "RECLAIMING", "STATUS": "STOP", "TPH": "0"},
    {"Unit": "STACKING", "STATUS": "RUN", "TPH": "3.000"},
    {"Unit": "COAL QUALITY", "STATUS": "ANTANG", "TPH": ""},
    {"Unit": "DESTINATION", "STATUS": "PLANT", "TPH": ""},
]

# Buat dua kolom untuk STREAM-1 dan STREAM-2
col1, col2 = st.columns(2)

# STREAM-1 di kolom pertama
with col1:
    st.markdown(generate_stream_html("STREAM-1", stream1_data), unsafe_allow_html=True)

# STREAM-2 di kolom kedua
with col2:
    st.markdown(generate_stream_html("STREAM-2", stream2_data), unsafe_allow_html=True)
