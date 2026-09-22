const modalCambiarEstadoCuenta = document.getElementById('modalCambiarEstado');

if (modalCambiarEstadoCuenta) {
    modalCambiarEstadoCuenta.addEventListener('show.bs.modal', function (event) {
        // Botón eliminar
        const boton = event.relatedTarget;
        
        // información de los atributos data
        const id = boton.getAttribute('data-id');
        const estadoActual = boton.getAttribute('data-estado');

        if (estadoActual=='activa'){
            estadoFuturo="inactiva"
        }
        else{
            estadoFuturo="activa"
        }

        // Escribir la información en los campos del modal 
        document.getElementById('estadoFut').value = estadoFuturo;
        document.getElementById('estadoFuturo').textContent = estadoFuturo;
        document.getElementById('idCuenta').value = id;
    });
}