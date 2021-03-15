var updateButtons = document.getElementsByClassName('update-kart')

for(i=0;i<updateButtons.length;i++){
    updateButtons[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        //console.log('product_id :', productId , 'action :', action)
        if (user == 'AnonymousUser'){
             console.log('User not logged in')
        }else{
             updateUserOrder(productId,action)
        }
    })
}

function updateUserOrder(productId,action){
    var url = '/update_item/'

    fetch(url,{
        method:'POST',
        headers:{
            'content-type' :'application/json',
            'X-CSRFToken' : csrftoken
        },
        body:JSON.stringify({'Product_id':productId,
                             'Action': action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:',data)
        location.reload()
    })
}