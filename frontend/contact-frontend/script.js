// Minimal JS: Fade-in animation on scroll for the main section
function revealOnScroll() {
    const reveals = document.querySelectorAll('section');
    for (let i = 0; i < reveals.length; i++) {
        const windowHeight = window.innerHeight;
        const elementTop = reveals[i].getBoundingClientRect().top;
        const elementVisible = 100;
        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add('active-reveal');
        } else {
            reveals[i].classList.remove('active-reveal');
        }
    }
}
window.addEventListener('scroll', revealOnScroll);
window.addEventListener('DOMContentLoaded', revealOnScroll);


