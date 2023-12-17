let hints = [true, true, true, true, true, true, true]

const field = document.getElementById("tags")
const mistakeContainer = document.getElementById("mistake-container")
const titleContainer = document.getElementById("Title")
const textContainer = document.getElementById("Text")

function AddTag(){
    ShowMistake(0)
    let tag = field.value
    if (hints.find((element) => element === tag)){
        ShowMistake(1)
        return
    }
    if (!(hints.find((element) => element === true))){
        ShowMistake(2)
        return
    }
    if (tag == ""){
        ShowMistake(3)
        return
    }
    if (tag.length > 20){
        ShowMistake(4)
        return
    }
    for (i = 0; i < 7; i++){
        if (hints[i] === true){

            tagval = document.getElementById("TAG" + (i+1).toString())
            tagcontainer = document.getElementById("Tag" +(i+1).toString() + "-container")

            tagval.innerHTML = tag
            tagcontainer.style.visibility = "visible"
            hints[i] = tag

            break
        }
    }
    field.value = ""
}

function ShowMistake(code){
//code 0 - clear all mistakes
//code 1 - tag already added
//code 2 - attempt to add more than 7 tags
//code 3 - attempt to apply empty tag
//code 4 - too long tagname(must be 20 or less)

//code 101 - empty title form
//code 102 - empty text form
//code 103 - no tags applied
    switch (code){
        case 0: {mistakeContainer.style.visibility = "hidden"
                break}
        case 1: {mistakeContainer.style.visibility = "visible"
                mistakeContainer.innerHTML = "Tag already applied"
                break}
        case 2: {mistakeContainer.style.visibility = "visible"
                mistakeContainer.innerHTML = "You cannot apply more than 7 tags"
                break}
        case 3: {mistakeContainer.style.visibility = "visible"
                mistakeContainer.innerHTML = "You are trying to apply an empty tag"
                break}
        case 4: {mistakeContainer.style.visibility = "visible"
                mistakeContainer.innerHTML = "Your Tagname is too long"
                break}
        case 101: {mistakeContainer.style.visibility = "visible"
                mistakeContainer.innerHTML = "You haven't filled questions' title"
                break}
        case 102: {mistakeContainer.style.visibility = "visible"
                mistakeContainer.innerHTML = "You haven't filled questions' description"
                break}
        case 101: {mistakeContainer.style.visibility = "visible"
                mistakeContainer.innerHTML = "You haven't applied any tag"
                break}
    }
}

function Close(pam){
    tagval = document.getElementById("TAG" + (pam).toString())
    tagcontainer = document.getElementById("Tag" +(pam).toString() + "-container")
    tagcontainer.style.visibility = "hidden"
    tagval.innerHTML = ""
    hints[pam - 1] = true
    hints = hints.slice(0, pam - 1).concat(hints.slice(pam, 7), [true])
    reDraw()
}

function reDraw(){
    for (i = 0; i < 7; i++){
        if (hints[i] !== true){
            tagval = document.getElementById("TAG" + (i+1).toString())
            tagcontainer = document.getElementById("Tag" +(i+1).toString() + "-container")

            tagval.innerHTML = hints[i]
            tagcontainer.style.visibility = "visible"
        }else{
            tagval = document.getElementById("TAG" + (i+1).toString())
            tagcontainer = document.getElementById("Tag" +(i+1).toString() + "-container")

            tagval.innerHTML = ""
            tagcontainer.style.visibility = "hidden"
        }
    }
}

function Validate(){
    if (titleContainer.value === ""){
        ShowMistake(101)
        return
    }
    if (textContainer.value === ""){
        ShowMistake(102)
        return
    }
    if (hints === [true, true, true, true, true, true, true]){
        ShowMistake(103)
        return
    }
    fetch(window.location.href, {
            method: "POST",
            headers: { "Content-type": "application/json",
                        "X-CSRFToken": (document.getElementsByName("csrfmiddlewaretoken")[0].value).toString()},
            body: JSON.stringify({
                "title" : titleContainer.value,
                "text" : textContainer.value,
                "tag1" : document.getElementById("TAG1").innerHTML,
                "tag2" : document.getElementById("TAG2").innerHTML,
                "tag3" : document.getElementById("TAG3").innerHTML,
                "tag4" : document.getElementById("TAG4").innerHTML,
                "tag5" : document.getElementById("TAG5").innerHTML,
                "tag6" : document.getElementById("TAG6").innerHTML,
                "tag7" : document.getElementById("TAG7").innerHTML
            })
    }).then((response) => {if(response.redirected){
            window.location.href = response.url;
        } })

}