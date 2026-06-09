const form = document.getElementById('userForm');

const message = document.getElementById('message');

form.addEventListener('submit', function(event) {

    event.preventDefault();

    const name = document.getElementById('name').value;

    const email = document.getElementById('email').value;

    if(name === '' || email === '') {

        message.innerText = 'All fields are required';

        message.style.color = 'red';

        return;
    }

    message.innerText = 'Form Submitted Successfully';

    message.style.color = 'green';
});