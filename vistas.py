from typing import Annotated

from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

from dependencias import ConnectionDep
from repositorio import obtener_producto, obtener_productos

router = APIRouter(tags=["productos"])

templates = Jinja2Templates(directory="templates")


@router.get("/productos")
async def listar_productos(request: Request, conn: ConnectionDep):
    # Ya implementado: muestra la página con la lista de productos.
    productos = await obtener_productos(conn)
    return templates.TemplateResponse(
        request=request,
        name="productos.html",
        context={"productos": productos},
    )


@router.get("/productos/{producto_id}/editar")
async def editar_producto_vista(request: Request, conn: ConnectionDep, producto_id: int):
    # TODO(5): busca el producto por su id y muestra el formulario de
    # edición con sus valores actuales.
    # Pista: usa obtener_producto() y la plantilla
    # "componentes/fila_editar.html". El contexto necesita:
    # producto, nombre, precio, cantidad, descripcion y errores.
    ...


@router.get("/productos/{producto_id}/cancelar")
async def cancelar_edicion_vista(request: Request, conn: ConnectionDep, producto_id: int):
    # Cancelar solo vuelve a mostrar la fila original, sin modificar nada.
    producto = await obtener_producto(conn, producto_id)
    if producto is None:
        return templates.TemplateResponse(
            request=request,
            name="componentes/producto_no_encontrado.html",
            context={"producto_id": producto_id},
        )
    return templates.TemplateResponse(
        request=request,
        name="componentes/fila_producto.html",
        context={"producto": producto},
    )


@router.post("/productos/{producto_id}")
async def guardar_producto_vista(
    request: Request,
    conn: ConnectionDep,
    producto_id: int,
    nombre: Annotated[str | None, Form()] = None,
    precio: Annotated[str | None, Form()] = None,
    cantidad: Annotated[str | None, Form()] = None,
    descripcion: Annotated[str | None, Form()] = None,
):
    # TODO(6): este es el corazón del ejercicio. Pasos a seguir:
    # 1. Convierte precio y cantidad a número (float / int).
    # 2. Valida los datos con el esquema ProductoActualizar.
    # 3. Si hay errores, vuelve a mostrar el formulario con los valores
    #    que el usuario escribió y los mensajes de error (HTTP 422).
    # 4. Si los datos son válidos, ejecuta actualizar_producto() y
    #    responde con la plantilla "componentes/fila_actualizada.html".
    ...