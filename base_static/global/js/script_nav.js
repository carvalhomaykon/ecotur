function menuShow() {
    let menuMobile = document.querySelector(".mobile-menu");
    let icon = document.querySelector('.icon');

    if (menuMobile.classList.contains("open")) {
        menuMobile.classList.remove("open");
        icon.src = "/static/img/menu_white_36dp.svg"; // Caminho relativo
    } else {
        menuMobile.classList.add("open");
        icon.src = "/static/img/close_white_36dp.svg"; // Caminho relativo
    }
}

function toggleDropdown() {
    const menuRotas = document.querySelector('.menu-rotas');
    menuRotas.classList.toggle('active'); // Alterna a classe 'active' para abrir/fechar o menu
}