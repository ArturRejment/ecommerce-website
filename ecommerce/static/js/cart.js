var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++)
{
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('product id:', productId, 'action', action)
        
        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            console.log('Not logged in')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken, // Csrf token passed declared in main.html header
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('Data:', data)
            location.reload()
        });
}