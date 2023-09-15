var updateBtns = document.getElementsByClassName("products__btn");

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productid = this.dataset.product
        var action = this.dataset.action
        console.log(productid + ', ' +action);
    })
}

// I need to create a Fetch request inside of this cycle
