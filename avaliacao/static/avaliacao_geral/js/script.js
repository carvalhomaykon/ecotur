function dropdown_button(button) {
    let listaSuspensa = button.nextElementSibling;
    if (listaSuspensa.classList.contains("open")) {
        listaSuspensa.classList.remove("open");
    } else {
        listaSuspensa.classList.add("open");
    }
}
