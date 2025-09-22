from tkinter import *
from tkinter import ttk
from conexion import *
from datetime import datetime

#fecha actual
fecha_actual = datetime.now().strftime("%Y-%m-%d")

# Inicializar la variable modificar
modificar = False
ventana= Tk()
ventana.title("Gastos & ingresos")
# ancho,alto, ejex,ejey
ventana.geometry("1100x750+500+50")

def gastoClick(event):
    # ========================
    # Muestra la información en los input al actualizar datos
    # ========================
    item_seleccionado = tablaData.selection()
    id = tablaData.item(item_seleccionado, "text") 
    if int(id) > 0:
        fecha.set(tablaData.item(item_seleccionado, "values")[1])
        descripcion.set(tablaData.item(item_seleccionado, "values")[2])
        categoria.set(tablaData.item(item_seleccionado, "values")[3])
        metodo_pago.set(tablaData.item(item_seleccionado, "values")[4])
        cantidad.set(tablaData.item(item_seleccionado, "values")[5])
        fuente.set(tablaData.item(item_seleccionado, "values")[6])
        Entidad.set(tablaData.item(item_seleccionado, "values")[7])
        Tipo.set(tablaData.item(item_seleccionado, "values")[8])
        Importe.set(tablaData.item(item_seleccionado, "values")[9])
        tiempo_horas.set(tablaData.item(item_seleccionado, "values")[10])
        proyecto_meta.set(tablaData.item(item_seleccionado, "values")[11])
             

db=ConexionDB()
id=StringVar()
fecha=StringVar()
descripcion=StringVar()
categoria=StringVar()
cantidad=StringVar()
fuente=StringVar()
Entidad=StringVar()
Tipo=StringVar()
Importe=StringVar()
tiempo_horas= StringVar()
metodo_pago = StringVar()
proyecto_meta = StringVar()


#Valores predeterminados
fecha.set(fecha_actual)
descripcion.set("")
Importe.set(0)
cantidad.set(1)
tiempo_horas.set(0)

marco= LabelFrame(ventana,text="Formulario de gastos & ingresos")
marco.place(x=10,y=10,width=1100,heigh=750)

def label(Frame,text,column,row,padx=10,pady=10):
    text=text.title()
    label=Label(Frame,text=text).grid(column=column,row=row,padx=padx,pady=pady)
    return label

def entry(Frame,var,column,row):
    entry=Entry(Frame,textvariable=var)
    entry.grid(column=column,row=row)

#===== label y entrys====
#Label y entry fecha
lblFecha=label(marco,'Fecha',0,0)
entryFecha=entry(marco,fecha,1,0)

#Label y entry descripción
lblDescripcion=label(marco,'Descripcion',column=0,row=1)
query="select distinct trim(Descripcion) from finanzas.finanzas where length(Descripcion) > 0 order by Descripcion asc "
db.cursor.execute(query)
filas=db.cursor.fetchall()
entryDescripcion=ttk.Combobox(marco,values=[fila[0] for fila in filas],textvariable=descripcion)
entryDescripcion.grid(column=1,row=1)
#entryDescripcion.current(21)

#Label y entry categoria
lblCategoria=label(marco,'Categoria',column=0,row=2)
query="""
         select distinct trim(c.nombre) as categoria 
         from finanzas.finanzas f
         join finanzas.dim_categoria c on c.categoria_id = f.categoria_id 
         where length(c.nombre) > 0 
         """
db.cursor.execute(query)
filas=db.cursor.fetchall()
entryCategoria=ttk.Combobox(marco,values=[fila[0] for fila in filas],textvariable=categoria)
entryCategoria.grid(column=1,row=2)
#entryCategoria.current(21)

#Label y entry ingresos
lblMetodoPago=label(marco,'Metodo de pago',column=2,row=0)
entryMetodoPago=ttk.Combobox(marco,values=["efectivo","tranf .bancolombia", "tranf .nequi"],textvariable=metodo_pago)
entryMetodoPago.grid(column=3,row=0)

#Label y entry Tipo  // este campo se usa para determinar si el ingreso es ahorro o inversión
lblTipo=label(marco,'Tipo',column=2,row=1)
entryTipo=ttk.Combobox(marco,values=["gasto","ingreso" ,"inversión","Ahorro","retiro inversión","ganancia inversión","inversion inmaterial"],textvariable=Tipo)
entryTipo.grid(column=3,row=1)

#Label y entry cantidad
lblCantidad=label(marco,'Cantidad',2,2)
entryCantidad=entry(marco,cantidad,3,2)

#Label y entry tiempo_horas
lblTiempo_Horas=label(marco,'tiempo_horas',2,3)
entryTiempo_Horas=entry(marco,tiempo_horas,3,3)


#Label y entry Entidad
lblEntidad=label(marco,'Entidad',column=4,row=0)
query="""select distinct trim(e.nombre) as entidad 
         from finanzas f
         join dim_entidad e on e.entidad_id = f.entidad_id 
         where length(e.nombre) > 0 
        """

db.cursor.execute(query)
filas=db.cursor.fetchall()
entryEntidad=ttk.Combobox(marco,values=[fila[0] for fila in filas],textvariable=Entidad)
entryEntidad.grid(column=5,row=0)
#entryEntidad.current(0)

#Label y entry Importe
lblProyectoMeta=label(marco,'Proyecto_meta',column=4,row=1)
lblProyectoMeta=entry(marco,proyecto_meta,5,1)

#entryTipo.current(0)

#Label y entry fuente
lblFuente=label(marco,'Fuente (Activo/Pasivo)',column=0,row=3)
entryFuente=ttk.Combobox(marco,values=["Activo","Pasivo",""],textvariable=fuente)
entryFuente.grid(column=1,row=3)
entryFuente.current(0)

#Label y entry Importe
lblImporte=label(marco,'Importe',column=4,row=2)
entryImporte=entry(marco,Importe,5,2)

#=== Texto de alertas
txtMensaje=Label(marco,text="messages here".title(),fg='green')
txtMensaje.grid(column=0,row=4,columnspan=4)


#=== Tabla de datos
tablaData=ttk.Treeview(marco,selectmode=NONE,height=15)
tablaData.grid(column=0,row=5,columnspan=6,padx=18,pady=10)

#=== Declaración de columnas dentro de tabla de datos
tablaData["columns"]=(
    "id","fecha","descripcion","categoria","metodo_pago",
    "cantidad","fuente","entidad","tipo","importe","tiempo_horas","proyecto_meta"
)

tablaData["show"] = "headings"  # <<--- ESTO ES IMPORTANTE

# Configuración de columnas
tablaData.column("id", width=100, anchor=CENTER)
tablaData.column("fecha", width=80, anchor=CENTER)
tablaData.column("descripcion", width=100, anchor=CENTER)
tablaData.column("categoria", width=80, anchor=CENTER)
tablaData.column("metodo_pago", width=70, anchor=CENTER)
tablaData.column("cantidad", width=70, anchor=CENTER)
tablaData.column("fuente", width=50, anchor=CENTER)
tablaData.column("entidad", width=70, anchor=CENTER)
tablaData.column("tipo", width=100, anchor=CENTER)
tablaData.column("importe", width=70, anchor=CENTER)
tablaData.column("tiempo_horas", width=100, anchor=CENTER)
tablaData.column("proyecto_meta", width=100, anchor=CENTER)

# Encabezados de columnas
tablaData.heading("id", text="Id", anchor=CENTER)
tablaData.heading("fecha", text="Fecha", anchor=CENTER)
tablaData.heading("descripcion", text="Descripción", anchor=CENTER)
tablaData.heading("categoria", text="Categoría", anchor=CENTER)
tablaData.heading("metodo_pago", text="Método de Pago", anchor=CENTER)
tablaData.heading("cantidad", text="Cantidad", anchor=CENTER)
tablaData.heading("fuente", text="Fuente", anchor=CENTER)
tablaData.heading("entidad", text="Entidad", anchor=CENTER)
tablaData.heading("tipo", text="Tipo", anchor=CENTER)
tablaData.heading("importe", text="Importe", anchor=CENTER)
tablaData.heading("tiempo_horas", text="Tiempo Horas", anchor=CENTER)
tablaData.heading("proyecto_meta", text="Proyecto/Meta", anchor=CENTER)

tablaData.bind("<<TreeviewSelect>>", gastoClick)

# BOTONES DE ACCIÓN
def btn(Frame,text,command,columna,fila,background=None):
    btn=Button(Frame,text=text,command=command,background=background)
    btn.grid(column=columna,row=fila)

btnEliminar=Button(marco,text='Eliminar',command=lambda:eliminar(),background="#ff5757")
btnEliminar.grid(column=3,row=6)
btnNuevo=Button(marco,text='Guardar',command=lambda:nuevo(),background="#85a8ff")
btnNuevo.grid(column=4,row=6)
btnModificar=Button(marco,text='Seleccionar',command=lambda:actualizar(),background="#808080")
btnModificar.grid(column=5,row=6)

#FUNCIONES CRUD
def validar():
    return len(fecha.get()) and len(descripcion.get())  and len(cantidad.get()) and len(fuente.get()) and len(Entidad.get()) and len(Importe.get()) 

def limpiar_campos():
    fecha.set(fecha_actual)
    descripcion.set("")
    cantidad.set(0)
    fuente.set("Activo")
    Entidad.set("La Roka")
    Tipo.set("gasto")
    Importe.set(0)
    tiempo_horas.set(0)
    proyecto_meta.set("")
    metodo_pago.set("efectivo")

def vaciar_tabla():
    filas=tablaData.get_children()
    for fila in filas:
        tablaData.delete(fila)

def llenar_tabla():
    vaciar_tabla()
    query = """
            SELECT 
                f.id, 
                f.fecha, 
                f.descripcion, 
                c.nombre AS categoria,
                m.nombre AS metodo_pago,
                f.cantidad, 
                f.fuente, 
                e.nombre AS entidad,
                t.nombre AS tipo,
                f.importe, 
                f.tiempo_horas, 
                f.proyecto_meta
            FROM finanzas.finanzas f
            JOIN dim_entidad e       ON f.entidad_id = e.entidad_id
            JOIN dim_tipo t          ON f.tipo_id = t.tipo_id
            JOIN dim_categoria c     ON f.categoria_id = c.categoria_id
            JOIN dim_metodo_pago m   ON f.metodo_pago_id = m.metodo_pago_id
            order by id desc;
            """
    db.cursor.execute(query)
    filas=db.cursor.fetchall()
    for fila in filas:
        id=fila[0]  
        tablaData.insert("",END,text=id,values=fila)

def eliminar():
    item_seleccionado = tablaData.selection()
    if not item_seleccionado:
        txtMensaje.config(text="No hay ningún registro seleccionado")
        return
    

    # Obtener valor de la columna que identifica la fila en la DB
    id = tablaData.item(item_seleccionado[0], "text") 

    print(id)

    if int(id) > 0:
        query=f"DELETE FROM finanzas WHERE id={id}"
        db.cursor.execute(query)
        db.connection.commit()

        # Eliminar del Treeview usando el iid
        tablaData.delete(item_seleccionado[0])
        txtMensaje.config(text=f"Se elimino el registro con id # {id}")
    else:
        txtMensaje.config(text="Seleccione un registro a eliminar".title())

def modificarFalse():
    global modificar
    modificar=False
    tablaData.config(selectmode=NONE)
    btnNuevo.config(text="Guardar")
    btnModificar.config(text='Seleccionar')
    btnEliminar.config(state=DISABLED)

def modificarTrue():
    global modificar
    modificar=True
    tablaData.config(selectmode=BROWSE)
    btnNuevo.config(text="Nuevo")
    btnModificar.config(text='Modificar')
    btnEliminar.config(state=NORMAL)

def get_or_create(col,table, value):
    """
    Busca si existe un valor en la tabla de dimensión, si no lo crea.
    Retorna el id correspondiente.
    """

    # 1. Buscar si existe
    db.cursor.execute(f"SELECT {col} FROM {table} WHERE nombre = %s", (value,))
    result = db.cursor.fetchone()
    
    if result:
        return result[0]  # ya existe
    else:
        # 2. Insertar nuevo registro y devolver id
        db.cursor.execute(f"INSERT INTO {table} (nombre) VALUES (%s)", (value,))
        db.connection.commit()
        return db.cursor.lastrowid

def nuevo():
    if modificar == False:
        if validar():
            # Paso 1: obtener o crear ids en tablas dim
            categoria_id = get_or_create('categoria_id' , "dim_categoria", categoria.get())
            metodo_pago_id = get_or_create('metodo_pago_id',"dim_metodo_pago", metodo_pago.get())
            entidad_id = get_or_create("entidad_id","dim_entidad", Entidad.get())
            tipo_id = get_or_create("tipo_id","dim_tipo", Tipo.get())  

            # Paso 2: insertar en tabla principal con FKs
            values = (
                fecha.get(), descripcion.get(), categoria_id, metodo_pago_id, 
                cantidad.get(), fuente.get(), entidad_id, tipo_id, 
                Importe.get(), tiempo_horas.get(), proyecto_meta.get()
            )

            query = """
                INSERT INTO finanzas.finanzas
                (fecha, descripcion, categoria_id, metodo_pago_id, cantidad, 
                 fuente, entidad_id, tipo_id, importe, tiempo_horas, proyecto_meta)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            
            db.cursor.execute(query, values)
            db.connection.commit()
            txtMensaje.config(text="Registro guardado!!", fg='green')
            llenar_tabla()
            limpiar_campos()
        else:
            txtMensaje.config(text="Los campos no deben estar vacios".title(), fg='red')
    else:
        modificarFalse()

def actualizar():
    if modificar == True:
        if validar():
            # Paso 1: obtener o crear ids en tablas dim
            categoria_id = get_or_create('categoria_id' , "dim_categoria", categoria.get())
            metodo_pago_id = get_or_create('metodo_pago_id',"dim_metodo_pago", metodo_pago.get())
            entidad_id = get_or_create("entidad_id","dim_entidad", Entidad.get())
            tipo_id = get_or_create("tipo_id","dim_tipo", Tipo.get())  

            # Paso 2: actualizar tabla principal con FKs
            values = (
                fecha.get(), descripcion.get(), categoria_id, metodo_pago_id, 
                cantidad.get(), fuente.get(), entidad_id, tipo_id, 
                Importe.get(), tiempo_horas.get(), proyecto_meta.get()
            )

            item_seleccionado = tablaData.selection()
            if item_seleccionado:
                id_db = tablaData.item(item_seleccionado[0], "text")  # ID de la base de datos
                query = """
                    UPDATE finanzas.finanzas
                    SET fecha=%s,
                        descripcion=%s,
                        categoria_id=%s,
                        metodo_pago_id=%s,
                        cantidad=%s,
                        fuente=%s,
                        entidad_id=%s,
                        tipo_id=%s,
                        importe=%s,
                        tiempo_horas=%s,
                        proyecto_meta=%s
                    WHERE id=%s
                """
                # Agregamos id_db al final de la tupla
                db.cursor.execute(query, values + (id_db,))
                db.connection.commit()
                txtMensaje.config(text="Actualización realizada!!", fg='green')
                llenar_tabla()
                limpiar_campos()
        else:
            txtMensaje.config(text="Los campos no deben estar vacíos".title(), fg='red')
    else:
        modificarTrue()

llenar_tabla()
limpiar_campos()
ventana.mainloop()