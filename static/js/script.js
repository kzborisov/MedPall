const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');

    // Toggle Nav
    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
        // Animate links
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ''
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        })

        // Burger animation
        burger.classList.toggle('toggle');
    });
}


const navColorChange = () => {
    const navbar = document.querySelector('nav');
    window.onscroll = () => {
        if (window.scrollY > 100) {
            navbar.classList.add('nav-scrolled');
        } else {
            navbar.classList.remove('nav-scrolled');
        }
    };
}


const flipCardShow = () => {
    const flipCard = document.querySelector('.flip-card')
    const flipCardInner = document.querySelector('.flip-card-inner')
    flipCard.addEventListener('click', () => {
        flipCardInner.classList.toggle('show')
    })
}


const callFunctions = () => {
    navSlide()
    navColorChange()
    flipCardShow()
}


callFunctions()
