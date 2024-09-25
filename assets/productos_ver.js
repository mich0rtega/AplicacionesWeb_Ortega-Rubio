// Obtener el valor del parámetro URL
const ParametroURL = new URLSearchParams(window.location.search);
const id_producto = parseInt(ParametroURL.get('id_producto'), 10);

// Datos del producto
const producto = {
    1: {
        nombre: "Conejo Gris",
        imagen: "images/Anglo Dutch Pools and Toys _ Quality Toys for Kids, Pool & Spa Supply.jpg",
        descripcion: "Conejo Gris de peluche suave",
        precio: "$546"
    },
    2: {
        nombre: "Pinguino Raw",
        imagen: "images/Aurora World Pompom Penguin - 7__ Pompom Dino, Green (1).jpg",
        descripcion: "Pinguino vestido de dinosaurio",
        precio: "$350"
    },
    3: {
        nombre: "Plush Dino",
        imagen: "images/Rawr the Stuffed T-Rex 5 Inch Rolly Pet Plush by Aurora.jpg",
        descripcion: "Dinosaurio verde pequeño rauw",
        precio: "$400"
    },
    4: {
        nombre: "Plush Elephant",
        imagen: "images/Easy Calm Down Kit for Sensory Needs and Fidgeting.jpg",
        descripcion: "Elefante gris pequeño peluche suave",
        precio: "$500"
    },
    5: {
        nombre: "Plush Winnie Poo",
        imagen: "images/Disney World Dining Tips and Tricks (plus how to save money on food!) (September 2024).jpg",
        descripcion: "Peluche winnie poo amarillo",
        precio: "$500"
    },
};

// Actualizar HTML según producto
if (producto[id_producto]) {
    document.getElementById("nombre_producto").textContent = producto[id_producto].nombre;
    document.getElementById("imagen_producto").src = producto[id_producto].imagen;
    document.getElementById("descripcion_producto").textContent = producto[id_producto].descripcion;
    document.getElementById("precio_producto").textContent = producto[id_producto].precio;
} else {
    document.getElementById("nombre_producto").textContent = "producto no existe";
    document.getElementById("imagen_producto").style.display = "none";
    document.getElementById("descripcion_producto").textContent = "producto no existe";
    document.getElementById("precio_producto").textContent = "producto no existe";
}
