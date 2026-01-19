from fastapi import  Body, FastAPI     
app = FastAPI()

countries = [
    {
        "country": "Nigeria",
        "continent": "Africa"
    },
    {
        "country": "Ghana",
        "continent": "Africa"
    },
    {
        "country": "Togo",
        "continent": "Africa"
    },
    {
        "country": "Kenya",
        "continent": "Africa"
    },
    {
        "country": "Egypt",
        "continent": "Africa"
    },
    {
        "country": "South Africa",
        "continent": "Africa"
    },
    {
        "country": "France",
        "continent": "Europe"
    },
    {
        "country": "Germany",
        "continent": "Europe"
    },
    {
        "country": "Italy",
        "continent": "Europe"
    },
    {
        "country": "Spain",
        "continent": "Europe"
    },
    {
        "country": "Portugal",
        "continent": "Europe"
    },
    {
        "country": "Netherlands",
        "continent": "Europe"
    },
    {
        "country": "Belgium",
        "continent": "Europe"
    }
]





@app.get("/countries")
async def get_countries():
    return countries

@app.get("/countries/{dynamic_params}")  
async def get_countries_by_name(dynamic_params: str):
    for country in countries:
        if country.get("country").casefold() == dynamic_params.casefold():
            return country
    return {"message": "Country not found"}    
    
@app.get("/countries/")
async def get_country_continents(country_name: str):
    countries_to_return = []
    for country in countries:
        if country.get("country").casefold() == country_name.casefold():
            countries_to_return.append(country)
    return countries_to_return

@app.get("/countries/{continent_name}/")
async def get_continent_countries(continent_name: str, country_name: str ):
    countries_to_return = []
    for country in countries:
        if (country.get("continent").casefold() == continent_name.casefold() and
            country.get("country").casefold() == country_name .casefold()):
            countries_to_return.append(country)
    return countries_to_return

@app.post("/countries/create_country")
async def create_country(new_country=Body()):
    countries.append(new_country)
        
        
        
@app.put("/countries/update_country")
async def update_country( updated_country=Body()): 
    for i in range(len(countries)):
        if countries[i].get("country").casefold() == updated_country.get("country").casefold():
            countries[i] = updated_country
            return {"message": "Country updated successfully"}       
            
            
@app.delete("/countries/delete_country/{country_name}")
async def delete_country(country_name: str):
    for i in range(len(countries)):
        if countries[i].get("country").casefold() == country_name.casefold():
            countries.pop(i)
            break
    return {"message": "Country deleted successfully"}
        