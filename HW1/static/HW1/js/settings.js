


window.onload = function (){
    SetClasses()
}

function SetClasses(){
    var avatarfield = document.getElementById("id_avatar")
    avatarfield.addEventListener('input', loadFile);
    let arr = document.getElementsByTagName("input")
    for(i = 0; i < arr.length; i++){
        if ((arr[i].type === "file"))
        {
            continue
        }
        arr[i].className = "form-control"
    }
}

var loadFile = function(event) {
    var item = document.getElementsByClassName("avatar avatar-128 rounded-circle")[0]
    item.src = URL.createObjectURL(event.target.files[0]);
    item.onload = function() {
      URL.revokeObjectURL(item.src) // free memory
    }
  };
