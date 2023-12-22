import shutil
import io
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile, Form
import pandas as pd
from typing import List
from pydantic import BaseModel as PydanticBaseModel

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class Valoracion(BaseModel):
    index: int
    id: str
    title: str
    type: str
    description: str
    release_year: int
    age_certification: str
    runtime: int
    imdb_id: str
    imdb_score: float
    imdb_votes: float

class ListadoValoraciones(BaseModel):
    valoraciones = List[Valoracion]

app = FastAPI(
    title="Servidor de datos",
    description="""Servimos datos de valoraciones de películas y series de Netflix.""",
    version="0.1.0",
)

@app.get("/retrieve_data/")
def retrieve_data():
    todosmisdatos = pd.read_csv('./Netflix_TV_Shows_and_Movies.csv')
    todosmisdatos = todosmisdatos.fillna(0)
    todosmisdatosdict = todosmisdatos.to_dict(orient='records')
    listado = ListadoValoraciones()
    listado.valoraciones = todosmisdatosdict
    return listado
