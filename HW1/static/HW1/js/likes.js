const box = document.getElementsByClassName("buttons")

for (let item of box){
    console.log(item.children[0], item.children[1])
    const [button1,counter1] = item.children[0].children
    const [button2,counter2] = item.children[1].children
    button1.addEventListener('click', function () {
        likeReciever(true, button1, button2, counter1, counter2)
    })
    button2.addEventListener('click', function () {
        likeReciever(false, button2, button1, counter1, counter2)
    })
}

function likeReciever(like, button_it, button_other, counter1, counter2){
    const request = new Request('/like/', {
            method: 'POST',
            body: JSON.stringify({"question_id" : button_it.dataset.id,
                                        "like" : like})
        });

        fetch(request)
            .then((response) => response.json())
            .then((data) => {
                console.log({data});
                counter1.innerHTML = data.likenum
                counter2.innerHTML = data.dislikenum
                if (button_it.className === "btn rounded-5 bg-blue"){
                        button_it.className = "btn rounded-5 bg-white"
                    }
                else{
                    button_it.className = "btn rounded-5 bg-blue"
                    button_other.className = "btn rounded-5 bg-white"
                }
            })
    }

