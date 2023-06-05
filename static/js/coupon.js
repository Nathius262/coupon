function copyText() {
    // Get the text field
    var copyText = document.getElementById("myInput");

    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices

        // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.value);

    // Alert the copied text    
    alert("Copied the text: " + copyText.value);
}

let dropdown = $('#dropdownMenuButton')
let dropdown_menu = $('#dropdown-menu-ul')
dropdown.click(()=>{
    dropdown.toggleClass('show')
    dropdown.attr("aria-expanded", (_, attr) => attr =="false"?"true":"false");
    dropdown_menu.toggleClass('show show-dropdown')
    
})

$('#dropdown-menu-ul').blur(()=>{
    document.querySelector('#dropdownMenuButton').classList.remove('show')
    document.querySelector('#dropdownMenuButton').setAttribute("aria-expanded", "false");
    document.querySelector('#dropdown-menu-ul').classList.remove('show', 'show-dropdown')
})

let currency = document.querySelectorAll('.currency')

for(let i=0; i<currency.length;i++){
    let currency_value = currency[i]
    currency_value.addEventListener('click', ()=>{
        console.log(currency_value.textContent)
        let dataobj = {
            "currency":currency_value.textContent,
            csrfmiddlewaretoken:currency_value.dataset.csrftoken,
        }
        $.ajax({
            type:'POST',
            url: "/currency/change/",
            data:dataobj,
            success: function(data){
                console.log(data)
                window.location.reload()
            },
            error: function(error){
                console.log(error)
            },
        });
    })
}

