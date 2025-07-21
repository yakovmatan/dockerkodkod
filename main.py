from fastapi import FastAPI, HTTPException, Query
import httpx

app = FastAPI()
BASE_URL = "https://ipinfo.io"

@app.get("/ipinfo")
async def get_ip_info(ip: str = Query(..., description="IPv4 or IPv6 address")):
    url = f"{BASE_URL}/{ip}/json"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Invalid IP or API error")
        data = response.json()
        return {
            "ip": data.get("ip"),
            "hostname": data.get("hostname"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "location": data.get("loc"),
            "org": data.get("org"),
            "timezone": data.get("timezone")
        }