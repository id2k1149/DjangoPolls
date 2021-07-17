//alert('JS alert window');

var button_1 = document.querySelector("#btn-one");
var button_2 = document.querySelector("#btn-two");
//console.log(button_1);

function click_button_1()
{
    alert({{ survey.name }});
}

button_1.addEventListener('click', click_button_1, false);


function click_button_2(event)
{
    element = event.target;

    if ( element.classList.contains('btn-info') )
    {
        var new_class = 'btn-danger';
        var old_class = 'btn-info';
    }
    else {
        var new_class = 'btn-info';
        var old_class = 'btn-danger';
    }

    element.classList.remove(old_class);
    element.classList.add(new_class);
}

button_2.addEventListener('click', click_button_2, false);