// login_page.js

function togglePasswordVisibility(inputId, toggleBtn) {
    const passwordField = document.getElementById(inputId);
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        toggleBtn.textContent = 'Hide';
    } else {
        passwordField.type = 'password';
        toggleBtn.textContent = 'Show';
    }
}

