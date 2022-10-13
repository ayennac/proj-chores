const form = document.getElementById('form');
const username = document.getElementById('username');
const password = document.getElementById('password');
const login_error = document.getElementsByClassName("login-error")[0];

form.addEventListener('submit', e => {
	e.preventDefault();
	checkInputs();
	login_error.className = 'login-error'
	
	const formInputs = {
		'username': username.value,
		'password': password.value,
	};

	fetch('/user-login', {
		method:'POST',
		body: JSON.stringify(formInputs),
		headers: {'content-type': 'application/json'},
	})
	.then((response) =>response.json())
	.then((data) => {
		if (data['code'] == true){
			console.log(data['code'])
			location.href = '/'
		} else{
			console.log(data['code'])
			console.log(login_error)
			login_error.className= 'login-error-show'
			login_error.textContent = "Incorrect username or password"
			setErrorFor(username, "Check username")
			setErrorFor(password, "Check password")	
		}
	});
});


function checkInputs() {
	// trim to remove the whitespaces
	const usernameValue = username.value.trim();
	const passwordValue = password.value.trim();

	if(usernameValue === '') {
		setErrorFor(username, 'Username cannot be blank');
	} else {
		setSuccessFor(username);
	}
	
	if(passwordValue === '') {
		setErrorFor(password, 'Password cannot be blank');
	} else {
		setSuccessFor(password);
	}    
}

function setErrorFor(input, message) {
	const formGroup = input.parentElement;
	const small = formGroup.querySelector('small');
	formGroup.className = 'form-group error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formGroup = input.parentElement;
	formGroup.className = 'form-group success';
}
	
function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}


