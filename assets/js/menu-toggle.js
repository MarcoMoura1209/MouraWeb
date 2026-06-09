const botao = document.getElementById('menu-toggle');
const nav = document.getElementById('nav-menu');

botao.addEventListener('click', function() {
    nav.classList.toggle('nav-aberta');
});