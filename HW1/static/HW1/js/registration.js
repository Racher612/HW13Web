function OpenLoginPage(){
    open("login")
}

const EMAIL_REGEXP = /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/iu;
const input = document.querySelector('#email');
const pass1 = document.getElementById("pass1")
const pass2 = document.getElementById("pass2")
const avatarfield = document.getElementById("id_avatar")
bar = document.getElementById("mistake-container")
bar2 = document.getElementById("mistake-container-2")
function isEmailValid(value) {
    return EMAIL_REGEXP.test(value);
}
function onInput() {
    if (isEmailValid(input.value)) {
        input.style.borderColor = 'green';
        bar.style.visibility = "hidden";
    } else {
        input.style.borderColor = 'red';
        bar.textContent = "email must include @ and .{domen}"
        bar.style.visibility = "visible";
    }
}
function validpass(){

    let uppercaseRegex = /[A-Z]/g;
    let lowercaseRegex = /[a-z]/g;
    let numbersRegex = /[0-9]/g;

    if (pass1.value.match(uppercaseRegex)){
        pass1.style.borderColor = 'green';
        bar.style.visibility = "hidden";
    }else{
        pass1.style.borderColor = 'red';
        bar.style.visibility = "visible";
        bar.textContent = "Password must include Uppercase & numbers"
    }

    if (pass2.value.match(uppercaseRegex)){
        pass2.style.borderColor = 'green';
        bar.style.visibility = "hidden";
    }else{
        pass2.style.borderColor = 'red';
        bar.style.visibility = "visible";
        bar.textContent = "Password must include Uppercase & numbers"
    }

    if (pass1.value.match(lowercaseRegex)){
        pass1.style.borderColor = 'green';
        bar.style.visibility = "hidden";
    }else{
        pass1.style.borderColor = 'red';
        bar.style.visibility = "visible";
        bar.textContent = "Password must include Uppercase & numbers"
    }

    if (pass2.value.match(lowercaseRegex)){
        pass2.style.borderColor = 'green';
        bar.style.visibility = "hidden";
    }else{
        pass2.style.borderColor = 'red';
        bar.style.visibility = "visible";
        bar.textContent = "Password must include Uppercase & numbers"
    }

    if (pass1.value.match(numbersRegex)){
        pass1.style.borderColor = 'green';
        bar.style.visibility = "hidden";
    }else{
        pass1.style.borderColor = 'red';
        bar.style.visibility = "visible";
        bar.textContent = "Password must include Uppercase & numbers"
    }

    if (pass2.value.match(numbersRegex)){
        pass2.style.borderColor = 'green';
        bar.style.visibility = "hidden";
    }else{
        pass2.style.borderColor = 'red';
        bar.style.visibility = "visible";
        bar.textContent = "Password must include Uppercase & numbers"
    }
}
function PasswordsEqual(){
    if (pass1.value === pass2.value){
        bar2.style.visibility = "hidden"
    }else{
        bar2.style.visibility = "visible"
        bar2.textContent = "passwords must be equal"
    }
}
var loadFile = function(event) {
    var item = document.getElementsByClassName("avatar avatar-128 rounded-circle")[0]
    item.src = URL.createObjectURL(event.target.files[0]);
    item.onload = function() {
      URL.revokeObjectURL(item.src) // free memory
    }
  };

input.addEventListener('input', onInput);
pass1.addEventListener('input', validpass);
pass2.addEventListener('input', validpass);
pass1.addEventListener('input', PasswordsEqual);
pass2.addEventListener('input', PasswordsEqual);
avatarfield.addEventListener('input', loadFile);

