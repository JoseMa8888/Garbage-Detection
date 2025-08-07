// static/js/script.js
function uploadImage() {
    const fileInput = document.getElementById('imageInput');
    const resultDiv = document.getElementById('result');
    const previewImg = document.getElementById('preview');
    
    if (!fileInput.files || fileInput.files.length === 0) {
        alert('Por favor seleccione una imagen');
        return;
    }

    const file = fileInput.files[0];
    
    // Validar tipo de archivo
    const validExtensions = ['jpg', 'jpeg', 'png', 'JPG'];
    const extension = file.name.split('.').pop().toLowerCase();
    if (!validExtensions.includes(extension)) {
        alert('Formato de imagen no válido. Use JPG, JPEG o PNG');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    // Mostrar vista previa
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImg.src = e.target.result;
        previewImg.style.display = 'block';
    };
    reader.readAsDataURL(file);

    // Determinar el endpoint según la página actual
    const isMvPage = window.location.pathname.includes('mv_detection');
    const endpoint = isMvPage ? '/mv_detection' : '/vit_detection';

    // Mostrar mensaje de carga
    resultDiv.innerHTML = '<p>Procesando imagen...</p>';

    // Enviar a la API
    fetch(endpoint, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.detail) });
        }
        return response.json();
    })

    .then(data => {
        // Verificar que los datos existen antes de usarlos
        const preprocessedTime = data.time_elapsed_preprocessed?.toFixed?.(4) ?? 'N/A';
        const totalTime = data.time_elapse?.toFixed?.(4) ?? 'N/A';
        
        resultDiv.innerHTML = `
            <div class="result-card">
                <h3>Tipo de basura detectado:</h3>
                <p class="result-type">${data.garbage_type || 'No detectado'}</p>
                <div class="result-times">
                    <p>Preprocesamiento: ${preprocessedTime}s</p>
                    <p>Total: ${totalTime}s</p>
                </div>
            </div>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
        resultDiv.innerHTML = `<p class="error">Error: ${error.message}</p>`;
    });
}