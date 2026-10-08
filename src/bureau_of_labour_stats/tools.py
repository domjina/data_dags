"""Methods Bureau of Labour Statistics (BLS) data"""

def fetch_data_bls_api(
        url: str = "",
        series_id: list[str] = [""],
        start_year: str | None = None,
        end_year: str | None = None
    ) -> dict:
    """Fetch data from the BLS API"""
    import json
    import requests

    if url == "" or series_id == [""]:
        raise ValueError("url or series_id is empty")
    headers = {"Content-type": "application/json"}
    data = json.dumps(
            {
                "seriesid": series_id,
                "startyear": start_year,
                "endyear": end_year
            }
        )
    request = requests.post(
        url=url,
        data=data,
        headers=headers
    )
    return json.loads(request.text)["Results"]

def naming_convention_bls(name: str, id: str, date: str) -> str:
    """Convert a date, series_name, and series_id into S3 format"""
    res = f"BLS/{name.replace(" ", "-").replace("(","-").replace(")","-")}/{id}/{date}/series.json"
    return res

def bls_fill_na(series):
    """
    Use the mean to fill null values.

    Params:
    series: pandas.Series, dtype == int
    """
    import pandas
    series = series.fillna(series.mean())
    return series

def bls_transformations(df):
    """
    Transform an observation dataframe to: 
    * contain year-period
    * fill missing values
    * convert series types

    Params:
    df: pandas.DataFrame
    """
    import pandas
    df["value"] = pandas.to_numeric(df["value"], errors="coerce")
    df["filled"] = df["value"].isna()
    df["value"] = bls_fill_na(df["value"])
    df = df.astype({"value": "int", "year": "str"})
    df["year-period"] = df["year"] + "-" + df["period"].str[1:]
    return df
