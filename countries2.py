from fastapi import FastAPI 
from fastapi import Body ,Path,HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status 

app = FastAPI()

class Countries:
    id: int
    country: str
    continent: str
    
    def __init__(self, id, country, continent):
        self.id = id
        self.country = country
        self.continent = continent  
        
class CountriesModel(BaseModel):
    id: Optional[int] = Field(default=None, description="ID of the country not required for creation")
    country: str = Field(min_length=2, max_length=50)
    continent: str = Field(min_length=2, max_length=50)  
    

    
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "country": "Brazil",
                "continent": "South America"
            }
        }
    }

COUNTRIES = [
    Countries(1, "USA", "North America"),
    Countries(2, "Canada", "North America"),
]  
    
            


@app.get("/countries2")
async def read_countries2():
    return COUNTRIES

@app.get("/countries2/{country_id}", status_code=status.HTTP_200_OK)
async def read_country2(country_id: int =Path(gt=0)):
    for country in COUNTRIES:
        if country.id == country_id:
            return country
    raise HTTPException(status_code=404, detail="Country not found")    
        
@app.put("/countries2/update_countries2",status_code=status.HTTP_204_NO_CONTENT)
async def update_country2(updated_country: CountriesModel):
    country_changed = False
    for i in range(len(COUNTRIES)):
        if COUNTRIES[i].id == updated_country.id:
            COUNTRIES[i].country = updated_country.country
            COUNTRIES[i].continent = updated_country.continent
            country_changed = True
            return {"message": "Country updated successfully"}
    if not country_changed:
        raise HTTPException(status_code=404, detail="Country not found")                    

@app.post("/create_countries2")
async def create_country2(new_country: CountriesModel):
    new_country = Countries(**new_country.model_dump())
    print(type(new_country))
    COUNTRIES.append(find_country_id(new_country))
    return {"message": "Country added successfully"}
def find_country_id(country :Countries):
    # if len(COUNTRIES) > 0:
    #     country.id=COUNTRIES[-1].id + 1
    # else:
    #     country.id=1
    country.id=1 if len(COUNTRIES) == 0 else COUNTRIES[-1].id + 1
    return country

@app.delete("/countries2/{country_id}")
async def delete_country2(country_id: int ):
    country_changed = False
    for i in range(len(COUNTRIES)):
        if COUNTRIES[i].id == country_id:
            COUNTRIES.pop(i)
            country_changed = True
    if not country_changed:
        raise HTTPException(status_code=404, detail="Country not found")