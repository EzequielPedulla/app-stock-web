document.addEventListener('DOMContentLoaded', function () {
  const deleteForms = document.querySelectorAll('form.delete-form');

  deleteForms.forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault(); // Detiene el envío inmediato

      Swal.fire({
        title: '¿Estás seguro?',
        text: 'No podrás revertir esta acción',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#6c757d',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.isConfirmed) {
          form.submit(); // Se envía solo si confirma
        }
      });
    });
  });
});
