#esto es um ejemplo
#esto es um ejemplo local
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
import models, schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/libros/", response_model=schemas.Libro)
async def create_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    db_libro = models.Libro(autor=libro.autor,titulo=libro.titulo,estado=libro.estado)
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro

@app.get("/libros/", response_model=List[schemas.Libro])
async def read_libros(db: Session = Depends(get_db)):
    return db.query(models.Libro).all()


@app.post("/usuarios/", response_model=schemas.Usuario)
async def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_libro = models.Usuario(nombre=usuarios.nombre, documento=usuarios.documento)
    db.add(db_usuarios)
    db.commit()
    db.refresh(db_usuarios)
    return db_usuarios

@app.get("/usuarios/", response_model=List[schemas.Usuario])
async def read_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuarios).all()

@app.post("/libros_usuarios/", response_model=schemas.LibroUsuario)
async def create_libro_usuario(libro_usuario: schemas.LibroUsuarioCreate, db: Session = Depends(get_db)):
    db_libros_usuarios = models.LibroUsuario(usuario_id=libro_usuario.usuario_id,libro_id=libro_usuario.libro_id, tiempo_prestamo=libro_usuario.tiempo_prestamo)
    db.add(db_libros_usuarios)
    db.commit()
    db.refresh(db_libros_usuarios)
    return db_libros_usuarios


@app.get("/libro/{libro_id}", response_model=schemas.Libro)
async def read_libro(libro_id: int, db: Session = Depends(get_db)):
    db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    return db_libro

@app.get("/libros/search/", response_model=List[schemas.Libro])
async def search_libros(query: str, db: Session = Depends(get_db)):
    db_libro = db.query(models.Libro).filter(models.Libro.titulo.like(f"%{query}%")).first()
    return db_libro



@app.put("/libro/{libro_id}", response_model=schemas.Libro)
async def update_libro(libro_id: int, libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    db.libro.autor = libro.autor
    db.libro.titulo = libro.titulo
    db.libro.estado = libro.estado
    db.commit()
    db.refresh(db_libro)
    return db_libro


@app.delete("/libro/{libro_id}", response_model=dict)
async def delete_libro(libro_id: int, db: Session = Depends(get_db)):
    db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    db.delete(db_libro)
    db.commit()
    return {"message": "libro eliminado"}