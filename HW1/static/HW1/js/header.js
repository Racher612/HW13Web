const SearchField = document.getElementById("SearchField")
const SearchContainer = document.getElementById("QuestionList")
console.log(SearchContainer.children)

SearchField.oninput = function (){
    console.log(5)
    const request = new Request('/search/', {
        method: 'POST',
        body: JSON.stringify({"search": SearchField.value})
    });

    fetch(request)
        .then((response) => response.json())
        .then((data) => {
            SearchContainer.innerHTML = ""
            for (item of data["FoundQuestions"].slice(0, 100)) {
                var option = document.createElement('option')
                option.value = item
                SearchContainer.appendChild(option)
            }
        })
    }

function Search(){
    window.location.replace("/SearchQuestion/" + SearchField.value)
    // open("login")
}

function ChangeLang() {
    fetch("/changelang/", {
        method : "POST",
        headers : { "Content-type": "application/json"},
        body : JSON.stringify(
            {"href" : window.location.href}
        )})
        .then((response) => {if(response.redirected){
            window.location.href = response.url;
        } })

}
