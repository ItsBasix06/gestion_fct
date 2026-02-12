const aparecerElementos = () => {
    const elementos = document.querySelectorAll('.reveal');
    
    elementos.forEach((el, i) => {
        setTimeout(() => {
            el.classList.add('active');
        }, i * 150); 
    });
};

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', aparecerElementos);
} else {
    aparecerElementos();
}