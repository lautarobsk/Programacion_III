// Clase SistemaReservas
class SistemaReservas {
    constructor() {
        this.reservas = []; // Array interno de reservas
    }

    agregarReserva(reserva) {
        this.reservas.push(reserva);
    }

    mostrarReservasEnTabla(tablaId) {
        const tabla = document.getElementById(tablaId).getElementsByTagName('tbody')[0];
        tabla.innerHTML = ""; // Limpiar tabla antes de agregar filas

        this.reservas.forEach(reserva => {
            const fila = tabla.insertRow();
            
            const celdaNombre = fila.insertCell(0);
            const celdaDestino = fila.insertCell(1);
            const celdaClase = fila.insertCell(2);

            celdaNombre.textContent = reserva.nombre;
            celdaDestino.textContent = reserva.destino;
            celdaClase.textContent = reserva.clase;
        });
    }
}

// Crear instancias de Reserva de prueba
const reserva1 = new Reserva("Córdoba", "Mendoza", "2025-09-15", "Económica", 2, "Ventana", 12, "Juan Pérez", 12345678, "1990-05-20", "M");
const reserva2 = new Reserva("Mendoza", "Tucumán", "2025-10-01", "Ejecutiva", 1, "Pasillo", 5, "María Gómez", 87654321, "1985-03-15", "F");
const reserva3 = new Reserva("Tucumán", "Córdoba", "2025-09-20", "Económica", 3, "Centro", 8, "Luis Fernández", 23456789, "1992-07-10", "M");

// Instanciar el sistema de reservas
const sistema = new SistemaReservas();
sistema.agregarReserva(reserva1);
sistema.agregarReserva(reserva2);
sistema.agregarReserva(reserva3);

// Mostrar las reservas en la tabla
sistema.mostrarReservasEnTabla("tablaReservas");
