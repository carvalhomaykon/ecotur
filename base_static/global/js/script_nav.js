function menuShow() {
    let menuMobile = document.querySelector(".mobile-menu");
    let button = document.querySelector(".mobile-menu-icon button");
    let icon = document.querySelector(".icon");

    if (menuMobile.classList.contains("open")) {
        menuMobile.classList.remove("open");
        icon.src = button.getAttribute("data-close-icon");
    } else {
        menuMobile.classList.add("open");
        icon.src = button.getAttribute("data-open-icon");
    }
}

function toggleDropdown() {
    const menuRotas = document.querySelector('.menu-rotas');
    menuRotas.classList.toggle('active'); // Alterna a classe 'active' para abrir/fechar o menu
}
