from fastapi import FastAPI

app = FastAPI(title="E-Ticaret Urun Katalogu")

URUNLER = [
    {"id": 1, "ad": "Kablosuz Kulaklik", "fiyat": 1250.0},
    {"id": 2, "ad": "Mekanik Klavye", "fiyat": 2100.0},
    {"id": 3, "ad": "Oyuncu Faresi", "fiyat": 850.0}
]

@app.get("/")
def ana_sayfa():
    return {"mesaj": "E-Ticaret API Calisiyor!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/products")
def urunleri_listele():
    return {"data": URUNLER}