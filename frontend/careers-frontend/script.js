// script.js

// This file can be used for general client-side scripting if needed.
// Form submissions are handled inline in the respective HTML files for simplicity
// as per the project requirements (Vanilla JS, no complex frameworks).

// Smooth scrolling for anchor links
window.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});

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

// Navbar highlight on scroll (if nav links use #ids)
window.addEventListener('scroll', function() {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('nav ul li a');
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 80;
        if (pageYOffset >= sectionTop) {
            current = section.getAttribute('id');
        }
    });
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Add the CSS for .active-reveal to style.css if not present:
// .active-reveal { opacity: 1 !important; transform: translateY(0) scale(1) !important; transition: opacity 0.8s cubic-bezier(0.4,0,0.2,1), transform 0.8s cubic-bezier(0.4,0,0.2,1); }


