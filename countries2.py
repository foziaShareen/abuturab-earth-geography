from fastapi import FastAPI 
from fastapi import Body

app = FastAPI()
class Countries:
    country: str
    continent: str
    
    def __init__(self, country, continent):
        self.country = country
        self.continent = continent  
            
countries=[
    Countries("Nigeria", "Africa"),
    Countries("Ghana", "Africa"),
    Countries("Togo", "Africa"),
    Countries("Kenya", "Africa"),    
    Countries("Egypt", "Africa"),
    Countries("South Africa", "Africa"),
    Countries("France", "Europe"),
    Countries("Germany", "Europe"),
]

@app.get("/countries2")
async def read_countries2():
    return countries

@app.post("/create_countries2")
async def create_country2(new_country=Body()):
    countries.append(new_country)
    return {"message": "Country added successfully"}