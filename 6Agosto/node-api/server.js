const express = require('express');
const app = express();
app.use(express.json());

// Ejercicio 1: campo "categoria"
// Ejercicio 4: campo "visitas"
let productos = [
    { id: 1, nombre: 'Laptop', precio: 2500000, categoria: 'Computo', visitas: 0 },
    { id: 2, nombre: 'Mouse', precio: 45000, categoria: 'Accesorios', visitas: 0 },
    { id: 3, nombre: 'Teclado', precio: 120000, categoria: 'Accesorios', visitas: 0 }
];

//Busqueda de todos los productos
app.get('/productos', (req, res) => {
    res.json(productos);
});

//Ejercicio 3: BUSCAR POR NOMBRE PARCIAL - GET
app.get('/productos/buscar/:nombre', (req, res) => {
    const nombre = req.params.nombre.toLowerCase();
    const resultados = productos.filter(p =>
        p.nombre.toLowerCase().includes(nombre));
    res.json(resultados);
});

//Busqueda por ID
app.get('/productos/:id', (req, res) => {
    const producto = productos.find(p => p.id ===
        parseInt(req.params.id));
    if (!producto) return res.status(404).json({
        mensaje: 'Producto no encontrado'
    });
    // Ejercicio 4: suma una visita
    producto.visitas++;
    res.json(producto);
});

//POST
app.post('/productos', (req, res) => {
    // Ejercicio 2: validacion de precio
    if (req.body.precio <= 0) {
        return res.status(400).json({
            mensaje: 'El precio debe ser mayor a cero'
        });
    }
    const nuevo = {
        id: productos.length + 1,
        nombre: req.body.nombre,
        precio: req.body.precio,
        categoria: req.body.categoria,
        visitas: 0
    };
    productos.push(nuevo);
    res.status(201).json(nuevo);
});

//PUT
app.put('/productos/:id', (req, res) => {
    const producto = productos.find(p => p.id ===
        parseInt(req.params.id));
    if (!producto) return res.status(404).json({
        mensaje: 'Producto no encontrado'
    });
    producto.nombre = req.body.nombre;
    producto.precio = req.body.precio;
    producto.categoria = req.body.categoria;
    res.json(producto);
});

//DELETE
app.delete('/productos/:id', (req, res) => {
    const index = productos.findIndex(p => p.id ===
        parseInt(req.params.id));
    if (index === -1) return res.status(404).json({
        mensaje: 'Producto no encontrado'
    });
    const eliminado = productos.splice(index, 1);
    res.json(eliminado[0]);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log('Servidor Node.js corriendo en puerto '
        + PORT);
});