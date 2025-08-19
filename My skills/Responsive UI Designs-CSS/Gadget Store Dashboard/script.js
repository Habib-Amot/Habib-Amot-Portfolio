let menuIcon = document.getElementsByClassName("menu-icon")[0];
let closeBtn = document.getElementById('close-btn')
let settingsMenu = document.getElementsByClassName("mobile-settings")[0];

menuIcon.addEventListener("click", (e)=> {
    closeBtn.style.visibility = 'visible';
    closeBtn.style.display = "flex";
    settingsMenu.style.display = "block";
    settingsMenu.style.visibility = "visible";
    settingsMenu.style.width = "250px";
    e.stopPropagation();
});

closeBtn.addEventListener("click", (e)=> {
    closeBtn.style.visibility = 'hidden';
    closeBtn.style.display = "none";
    settingsMenu.style.width = "0px";
    settingsMenu.style.display = "none";
    settingsMenu.style.visibility = "hidden";
    e.stopPropagation();
    
});

settingsMenu.addEventListener('click', (e)=>{
    e.stopPropagation();
})

document.body.addEventListener("click", (e)=> {
    if(e.target != settingsMenu && settingsMenu.style.width !== "0px"){
        settingsMenu.style.width = "0px";
        settingsMenu.style.display = "none";
        settingsMenu.style.visibility = "hidden";
        closeBtn.style.visibility = 'hidden';
        closeBtn.style.display = 'none';
    }
});
