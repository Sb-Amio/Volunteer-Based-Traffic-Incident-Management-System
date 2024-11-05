
    document.addEventListener("DOMContentLoaded", function () {
        const password1 = document.getElementById("id_password1");
        const password2 = document.getElementById("id_password2");
        const validationMessage = document.getElementById("password-validation");

        function validatePasswords() {
            if (password1.value === password2.value && password1.value !== "") {
                validationMessage.textContent = "Passwords match";
                validationMessage.style.color = "green";
                password1.style.borderColor = "green";
                password2.style.borderColor = "green";
            } else if (password2.value !== "") {
                validationMessage.textContent = "Passwords do not match";
                validationMessage.style.color = "red";
                password1.style.borderColor = "red";
                password2.style.borderColor = "red";
            } else {
                validationMessage.textContent = "";
                password1.style.borderColor = "";
                password2.style.borderColor = "";
            }
        }

        // Add event listeners to check passwords as the user types
        password1.addEventListener("input", validatePasswords);
        password2.addEventListener("input", validatePasswords);
    });

    function togglePasswordVisibility(fieldId, element) {
        const field = document.getElementById(fieldId);
        if (field.type === "password") {
            field.type = "text";
            element.textContent = "Hide";
        } else {
            field.type = "password";
            element.textContent = "Show";
        }
    }

