document.addEventListener('DOMContentLoaded', () => {
  const forms = document.querySelectorAll('form.validate-form');

  console.log('Archivo de validación cargado ✅');

  forms.forEach((form) => {
    form.addEventListener('submit', (e) => {
      const name = form.querySelector("[name='name']").value.trim();
      const price = parseFloat(form.querySelector("[name='price']").value);
      const stock = parseInt(form.querySelector("[name='stock']").value);
      const barcode = form.querySelector("[name='barcode']").value.trim();

      // Validaciones
      if (!name) {
        e.preventDefault();
        Swal.fire('Error', 'El nombre es obligatorio', 'error');
        return;
      }

      if (isNaN(price) || price <= 0) {
        e.preventDefault();
        Swal.fire('Error', 'El precio debe ser mayor a 0', 'error');
        return;
      }

      if (isNaN(stock) || stock < 0) {
        e.preventDefault();
        Swal.fire('Error', 'El stock no puede ser negativo', 'error');
        return;
      }

      if (barcode && barcode.length > 13) {
        // Valida solo si se escribió algo
        e.preventDefault();
        Swal.fire(
          'Error',
          'El código de barras no puede tener más de 13 caracteres',
          'error'
        );
        return;
      }
    });
  });
});
