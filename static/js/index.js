// Selecting elements
const menuBtn = document.querySelector('.menu_btn');
const closeMenuBtn = document.querySelector('.close_menu');
const navbar = document.querySelector('.navbar');

// Add class 'active' when menu button is clicked
menuBtn.addEventListener('click', () => {
    navbar.classList.add('active');
});

// Remove class 'active' when close button is clicked
closeMenuBtn.addEventListener('click', () => {
    navbar.classList.remove('active');
});