 const seeMenu = document.getElementById('menu');
    const theMenu = document.getElementById('mobile-menu')

console.log("JS carregado com sucesso!");

    function closeLightbox() {
        document.getElementById('lightbox').classList.add('hidden');
    };

    seeMenu.addEventListener('click', () => {
        theMenu.classList.toggle('-translate-x-full')
        theMenu.classList.toggle('translate-x-0')
    })

    document.querySelectorAll('.edition').forEach(edition => {
        const header = edition.querySelector('.header');
        const content = edition.querySelector('.content');
        const icon = edition.querySelector('.arrow');

        let isOpen = false;

        header.addEventListener('click', () => {
            isOpen = !isOpen;

            if (isOpen) {
                content.classList.remove('max-h-0');
                content.classList.add('max-h-[1000px]');
                icon.classList.add('rotate-180');
            } else {
                content.classList.add('max-h-0');
                content.classList.remove('max-h-[1000px]');
                icon.classList.remove('rotate-180');
            }
        });
    });
