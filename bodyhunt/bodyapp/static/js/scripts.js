var updateBtns = document.getElementsByClassName("updateitem");

for (var i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productid = this.dataset.product;
    var action = this.dataset.action;
    url = "/updatecart/"
    fetch(url, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({'productid': productid, 'action': action})
    })
    .then((response) => {
      return response.json();
    }).then(() => {
      console.log('Succesfully added!');
    })
  });
}