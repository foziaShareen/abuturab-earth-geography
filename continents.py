from fastapi import FastAPI
app = FastAPI()
continents = {
    "Asia": [
        "Pakistan", "India", "China", "Japan", "South Korea",
        "Saudi Arabia", "Iran", "Iraq", "Turkey", "Indonesia"
    ],

    "Africa": [
        "Nigeria", "Egypt", "South Africa", "Kenya", "Ethiopia",
        "Ghana", "Morocco", "Algeria", "Sudan", "Tanzania"
    ],

    "Europe": [
        "United Kingdom", "France", "Germany", "Italy", "Spain",
        "Netherlands", "Sweden", "Norway", "Switzerland", "Poland"
    ],

    "North America": [
        "United States", "Canada", "Mexico", "Cuba", "Jamaica",
        "Panama", "Costa Rica", "Honduras", "Guatemala"
    ],

    "South America": [
        "Brazil", "Argentina", "Chile", "Peru", "Colombia",
        "Venezuela", "Bolivia", "Ecuador", "Paraguay"
    ],

    "Australia": [
        "Australia", "New Zealand", "Fiji", "Papua New Guinea"
    ],

    "Antarctica": [
        "McMurdo Station (USA)",
        "Amundsen–Scott South Pole Station (USA)",
        "Rothera Research Station (UK)",
        "Halley Research Station (UK)",
        "Mawson Station (Australia)",
        "Davis Station (Australia)",
        "Casey Station (Australia)",
        "Vostok Station (Russia)",
        "Concordia Station (France–Italy)",
        "Neumayer Station (Germany)"
    ]
}


@app.get("/continents")
async def get_continents():
    return  continents
 
@app.get("/continents/{dynamic_params}")  
async def get_continents_by_name(dynamic_params: str):
    if dynamic_params in continents:
        return {"continent": dynamic_params}
    else:
        return {"error": "Continent not found"}