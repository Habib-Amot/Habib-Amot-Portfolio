/* Now I am going to process the form data as soon as the user is typing and also when the user tries to submit the form */

let form = document.forms[0]; // Accessing the first form in the document

// Accessing the input fields
let emailInput = form.elements['email'];
let passwordInput = form.elements['password'];
let confirmPasswordInput = form.elements['confirm-password'];
let passwordStatus = document.querySelector('.password-status');
let bar =  document.querySelector('.strength-indicator .bar .indicator')

// Function to validate email format
emailInput.addEventListener('change', function() {
    let emailValue = emailInput.value;
    let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple email regex pattern
    if (!emailPattern.test(emailValue)) {
        console.log(emailInput.parentElement)
        emailInput.parentElement.nextElementSibling.style.display = 'block';
        emailInput.parentElement.nextElementSibling.textContent = 'Please enter a valid email address.'
    } else {
        emailInput.setCustomValidity('');
    }
});

//password validation
passwordInput.addEventListener('input', function(e) {
    let passwordStrengthScore = 0;
    let passwordValue = passwordInput.value;
    let passwordLength = /^.{8,}$/u; // At least 8 characters
    let includesUppercase = /[A-Z]/;
    let includesLowercase = /[a-z]/;
    let includesSpecialChar = /[!@#$%^&*(),.?":{}|<>]/;
    let includesNumber = /[0-9]/;

    if (passwordLength.test(passwordValue)) {
        passwordStatus.querySelector('.min-chars').style.opacity = '1';
        passwordStrengthScore++
    }else {
        passwordStatus.querySelector('.min-chars').style.opacity = '0.4';
    }
    if (includesUppercase.test(passwordValue)) {
        passwordStatus.querySelector('.uppercase-letter').style.opacity = '1';
        passwordStrengthScore++
    }else {
        passwordStatus.querySelector('.uppercase-letter').style.opacity = '0.4';
    }
    if (includesLowercase.test(passwordValue)) {
        passwordStatus.querySelector('.lowercase-letter').style.opacity = '1';
        passwordStrengthScore++;
    }else {
        passwordStatus.querySelector('.lowercase-letter').style.opacity = '0.4';
    }
    if (includesSpecialChar.test(passwordValue)) {
        passwordStatus.querySelector('.special-character').style.opacity = '1';
        passwordStrengthScore++;
    }else {
        passwordStatus.querySelector('.special-character').style.opacity = '0.4';
    }
    if (includesNumber.test(passwordValue)) {
        passwordStatus.querySelector('.include-number').style.opacity = '1';
        passwordStrengthScore++;
    }else {
        passwordStatus.querySelector('.include-number').style.opacity = '0.4';
    }
    bar.style.width = ((passwordStrengthScore / 5) * 100) + "%";
    if(passwordStrengthScore <= 2 && passwordStrengthScore != 0){
        bar.style.background = "red";
        bar.parentElement.nextElementSibling.textContent = 'weak'
    }
    else if(3 <= passwordStrengthScore && passwordStrengthScore <= 4) {
        bar.style.background = "green";
        bar.parentElement.nextElementSibling.textContent = 'medium';
    }
    else if(passwordStrengthScore == 5){
        bar.style.background = "blue";
        bar.parentElement.nextElementSibling.textContent = 'strong'
    }
    if(passwordStrengthScore == 5){
        confirmPasswordInput.style.display = 'block'
    }else{
        confirmPasswordInput.style.display = 'none'
    }
});