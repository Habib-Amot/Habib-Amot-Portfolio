let body = document.querySelector('body');
let dropdownMenu = document.querySelector('.dropdown-menu');
let selectedOption = dropdownMenu.querySelector('.selected-option');
let options = dropdownMenu.querySelectorAll('.option');
let inputField = selectedOption.querySelector('input');
let profileBar = document.querySelector('.profile-bar');


body.addEventListener('click', (e) => {
    if(e.target !== selectedOption && e.target !== inputField){
        dropdownMenu.classList.remove('active');
    }
    if(e.target !== profileBar){
        profileBar.classList.remove('active');
    }
});


profileBar.addEventListener('click', (e) => {
    profileBar.classList.toggle('active');
    e.stopPropagation();
});



selectedOption.addEventListener('click', (e) => {
    dropdownMenu.classList.toggle('active');
    e.stopPropagation();
});

options.forEach((value, index) => {
    value.addEventListener('click', () => {
        inputField.value = value.textContent;
        options.forEach((val, idx) => {
            val.classList.remove('active');
        });
        value.classList.add('active');
        dropdownMenu.classList.remove('active');
    });
});
