const form = document.getElementById('form');
const username = document.getElementById('username');
const firstname = document.getElementById('first-name');
const lastname = document.getElementById('last-name');
const email = document.getElementById('inputemail');
const signpassword = document.getElementById('inputpassword');
const login_error = document.getElementsByClassName("login-error")[0];

form.addEventListener('submit', e => {
	e.preventDefault();
	checkInputs();
	login_error.className = 'login-error'
	
	const formInputs = {
		'username': username.value,
		'firstname': firstname.value,
		'lastname': lastname.value,
		'email': email.value,
		'signpassword': signpassword.value
	};

	fetch('/user-signup', {
		method:'POST',
		body: JSON.stringify(formInputs),
		headers: {'content-type': 'application/json'},
	})
	.then((response) =>response.json())
	.then((data) => {
		if (data['code'] == true){
			console.log(data['code'])
			location.href = '/'} else{
				login_error.textContent = "Username and/or email already in use"
				login_error.className = 'login-error-show'
				setErrorFor(username, "")
				setErrorFor(firstname, "")
				setErrorFor(lastname,"")
				setErrorFor(email, "")
				setErrorFor(signpassword,"")
			}
	});
});



//check inputs on change 
function checkInputs() {
	// trim to remove the whitespaces
	const usernameValue = username.value.trim();
	const signpasswordValue = signpassword.value.trim();
    const firstnameValue = firstname.value.trim();
	const lastnameValue = lastname.value.trim();
    const emailValue = email.value.trim();
    
	if(usernameValue === '') {
		setErrorFor(username, 'Username cannot be blank');
	} else {
		setSuccessFor(username);
	}
	

    if(firstnameValue === '') {
		setErrorFor(firstname, 'First Name cannot be blank');
	} else {
		setSuccessFor(firstname);
	}

    if(lastnameValue === '') {
		setErrorFor(lastname, 'Last Name cannot be blank');
	} else {
		setSuccessFor(lastname);
	} 

    if(emailValue === '') {
		setErrorFor(email, 'Email cannot be blank');
	} else {
		setSuccessFor(email);
	}

    if(signpasswordValue === '') {
		setErrorFor(signpassword, 'Password cannot be blank');
	} else {
		setSuccessFor(signpassword);
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


