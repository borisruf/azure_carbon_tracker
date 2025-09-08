# Azure Carbon Tracker
The Azure Carbon Optimization Dashboard currently does not include the OpenAI service. This Python library uses the [Cost Management API](https://learn.microsoft.com/en-us/rest/api/cost-management/) and the [Retail Prices API](https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices) to obtain token consumption data which it enriches with [AI model carbon scenarios](https://github.com/borisruf/carbon-footprint-modeling-tool?tab=readme-ov-file#ai-model-inferences) and region emission factors to estimate the missing information.

## Installation

To install the package, you can use `pip`, the Python package manager. Open a command line or terminal and run the following command:

```bash
pip install azure_carbon_tracker
```

## Usage

Make sure to [login to your Azure CLI](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest) first. You can then use the library as follows:

__Sample code__
```python
from azure_carbon_tracker import get_carbon_emissions

df = get_carbon_emissions(
    subscription_id="[your-subscription-id]",
    resource_group="[your-resource-group]",
    start_date="2024-09-01",
    end_date="2025-08-01"
)
```



__Sample output__
```bash
print(df.head())

month                         azure_name location  total_cost_usd  \
0  2025-01-01       gpt-4o-0806-Inp-regnl Tokens  US East        0.08215   
1  2025-01-01      gpt-4o-0806-Outp-regnl Tokens  US East        0.197672   
2  2025-01-01   gpt-4o-mini-0718-Inp-glbl Tokens  US East        0.024068 
3  2025-01-01  gpt-4o-mini-0718-Inp-regnl Tokens  US East        0.00018   
4  2025-01-01  gpt-4o-mini-0718-Outp-glbl Tokens  US East        0.056312   

   unit_price_usd  token_count                   model_name  \
0        0.002750        29872       gpt4o-ruf-mortas-token   
1        0.011000        17970       gpt4o-ruf-mortas-token   
2        0.000150       160460  gpt4o-mini-ruf-mortas-token   
3        0.000165         1088  gpt4o-mini-ruf-mortas-token   
4        0.000600        93854  gpt4o-mini-ruf-mortas-token   

   milliwatt_hour_per_token  total_energy_kilowatt_hour  \
0                   10.5186                    0.157106   
1                   10.5186                    0.094510   
2                    0.6375                    0.051147   
3                    0.6375                    0.000347   
4                    0.6375                    0.029916   

   kg_co2_per_kilowatt_hour  total_co2e_kg  
0                    0.2902       0.045592  
1                    0.2902       0.027427  
2                    0.2902       0.014843  
3                    0.2902       0.000101  
4                    0.2902       0.008682  
```

### Customization

Default CSVs for pricing, model mapping, carbon models, and emission factors are [included in the package](https://github.com/borisruf/azure_carbon_tracker/tree/main/azure_carbon_tracker/data). You can overwrite them by passing your own file paths to the relevant functions:

```python
df = get_carbon_emissions(
    subscription_id,
    resource_group,
    start_date,
    end_date,
    pricing_path="/custom/path/pricing.csv",
    model_mapping_path="/custom/path/model_mapping.csv",
    carbon_models_path="/custom/path/carbon_models.csv",
    emission_factors_path="/custom/path/emission_factors.csv"
)
```

You can also query specific prices or create an updated pricing CSV. 

```python
from azure_carbon_tracker import query_price, create_pricing_table

# Query a price for a specific meter and location
price = query_price(meter_name="Standard_D2_v3", location="westeurope")

# Update the pricing file
create_pricing_table("pricing.csv", "updated_pricing.csv")
```
