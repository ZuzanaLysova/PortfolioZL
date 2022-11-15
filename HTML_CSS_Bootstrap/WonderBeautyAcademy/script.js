let menu;
let toggle;

function initializeMenu() {
    toggle = document.getElementById("menu-toggle");
    menu = document.getElementById("menu");

    toggle.addEventListener('click', toggleMenu);
    menu.addEventListener('click', toggleMenu);
}

function toggleMenu() {
    const isVisible = menu.classList.contains("expanded");

    if (isVisible) {
        menu.classList.remove('expanded');
    } else {
        menu.classList.add('expanded');
    }
}

function initializeSubmenus() {
    const toggles = document.getElementsByClassName('submenu-toggle');

    for (const toggle of toggles) {
        toggle.addEventListener('click', toggleSubmenu);
    }
}

function toggleSubmenu(event) {
    event.stopPropagation(); // block other parent's click events, like hiding the whole menu

    const id = event.target.dataset.submenu; // get the clicked element (event.target) and its data-submenu attribute (.dataset.submenu).
    const category = document.getElementById(id);

    if (category.classList.contains('expanded')) {
        category.classList.remove('expanded');
    } else {
        hideAllMenus();
        category.classList.add('expanded');
    }
}

function hideAllMenus() {
    const submenus = document.getElementsByClassName('category');
    for (const submenu of submenus) {
        submenu.classList.remove('expanded');
    }
}

document.addEventListener("DOMContentLoaded", () => {
    initializeMenu();
    initializeSubmenus();
});