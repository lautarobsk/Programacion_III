function validarFechaVuelo(fechaVuelo) {
    const fechaIngresada = new Date(fechaVuelo);
    
    const hoy = new Date();
    hoy.setHours(0, 0, 0, 0); 

    if (fechaIngresada < hoy) {
        return "Fecha de Vuelo debe ser Mayor a la Fecha Actual";
    }

    return true;
}

const inputFecha = document.getElementById("fecha");
inputFecha.addEventListener("change", () => {
    const resultado = validarFechaVuelo(inputFecha.value);
    if (resultado !== true) {
        alert(resultado);
        inputFecha.value = ""; 
    }
});


const origen = document.getElementById("origen");
const destino = document.getElementById("destino");

const opcionesDestinoOriginales = Array.from(destino.options);

origen.addEventListener("change", () => {
    const valorOrigen = origen.value;

    destino.innerHTML = "";

    opcionesDestinoOriginales.forEach(opcion => {
        if (opcion.value !== valorOrigen) {
            destino.appendChild(opcion);
        }
    });
});






