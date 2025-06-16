    const seeMenu = document.getElementById('menu');
    const theMenu = document.getElementById('mobile-menu')
    console.log("JS carregado com sucesso!");
    document.querySelectorAll('.thumbnail').forEach(img => {
        img.addEventListener('click', () => {
            const lightbox = document.getElementById('lightbox');
            const lightboxImg = document.getElementById('lightbox-img');
            const lightboxDesc = document.getElementById('lightbox-desc');

            lightboxImg.src = img.src;
            lightboxDesc.textContent = img.getAttribute('data-description');
            lightbox.classList.remove('hidden');
        });
    });

    function closeLightbox() {
        document.getElementById('lightbox').classList.add('hidden');
    };

    seeMenu.addEventListener('click', () => {
        theMenu.classList.toggle('-translate-x-full')
        theMenu.classList.toggle('translate-x-0')
    })