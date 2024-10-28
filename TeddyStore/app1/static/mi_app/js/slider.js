//Selecciona todas las imágenes del slider
let slides = document.querySelectorAll('.slider');
let currentSlide = 0;

//Función para cambiar imagen
function changeSlide() {
    //Oculta la imagen actual
    slides[currentSlide].classList.remove('active');
    //Cambia al siguiente slide
    currentSlide = (currentSlide + 1) % slides.length;
    //Muestra la siguiente imagen
    slides[currentSlide].classList.add('active');
}

//Iniciar slider cambiando cada 3 segundos
setInterval(changeSlide, 3000); // Cambié el intervalo a 3000 ms (3 segundos)
