# data_dags

## What this project can do

This repository contains the DAGs and supporting code used to colect data for my Economic Nowcasting Platform.

The pipelines currently retrieve observation series from the public U.S. Bureau of Labor Statistics (BLS) API and store the resulting data in S3-compatible storage provided by Garage.

The infrastructure configuration for the platform is maintained in a seperate repository [here](https://github.com/domjina/platform).

## DAGs

### Download Data

The download_data_dag retrieves API and API resource details from a PostgreSQL database. It then uses these details to request the latest available observations from the corresponding API endpoints.

The DAG dynamically generates tasks for each API resource, allowing multiple observation series to be downloaded as part of the same workflow.

Once retrieved, the data is uploaded to Garage using its S3-compatible interface. Existing files are checked before uploading to avoid unnecessary duplicate downloads.

## Data Analysis

The repository also contains a Jupyter notebook used to analyse the available BLS observation series.

The observations were selected based on their correlations with one another. Since the public BLS API has a rate limit, the aim was to reduce the number of series collected while retaining as much unique information as possible.

## Future work

* Add more observation series to the dataset.
* Expand the number of supported API providers.
* Import data visualisation and error handling.
* Add CI linting and validation for DAG code.