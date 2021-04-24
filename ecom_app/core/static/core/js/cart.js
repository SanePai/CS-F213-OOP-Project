var UpdateBtns = document.getElementsByClassName('update-cart')

for(i=0; i<UpdateBtns.length; i++){
    UpdateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        updateUserOrder(productId, action);
        console.log("update", action);
    })
}
function updateUserOrder(productId, action){
    var url = '/update-item/'

    fetch(url,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({"productId": productId, "action": action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('Data:', data)
        location.reload()
    })
}
