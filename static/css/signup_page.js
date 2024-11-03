
        function togglePasswordVisibility(id, element) {
            const passwordField = document.getElementById(id);
            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                element.textContent = 'Hide';
            } else {
                passwordField.type = 'password';
                element.textContent = 'Show';
            }
        }

        const password1Field = document.getElementById('id_password1');
        const password2Field = document.getElementById('id_password2');
        const validationMessage = document.getElementById('password-validation');

        password2Field.addEventListener('input', function() {
            if (password1Field.value && password2Field.value) {
                if (password1Field.value === password2Field.value) {
                    password1Field.style.borderColor = 'green';
                    password2Field.style.borderColor = 'green';
                    validationMessage.textContent = 'Passwords match!';
                    validationMessage.style.color = 'green';
                } else {
                    password1Field.style.borderColor = 'red';
                    password2Field.style.borderColor = 'red';
                    validationMessage.textContent = 'Passwords do not match!';
                    validationMessage.style.color = 'red';
                }
            } else {
                password1Field.style.borderColor = '#dddfe2';
                password2Field.style.borderColor = '#dddfe2';
                validationMessage.textContent = '';
            }
        });
