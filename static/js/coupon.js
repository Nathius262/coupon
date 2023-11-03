let bodyEl = document.querySelector("body")
let navEl = document.querySelectorAll(".navbar")
let modeBtn = document.getElementById("mode-btn")
let imgLogo = document.getElementById("header-logo")

window.addEventListener("DOMContentLoaded", ()=>{
    screenSwitcher(false)
})

function copyText(input) {
    // Get the text field
    var copyText;
    if (input===true){
        copyText= document.getElementById("myInput");
    }else{
        copyText= document.getElementById("vendorInput");
    }
    

    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices

        // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.value);

    // Alert the copied text    
    //alert("Copied the text: " + copyText.value);
    let copyAlert = document.getElementById("copy-alert")
    copyAlert.style.display = "block"
    setTimeout(
        function(){

            //console.log("runing")
            copyAlert.style.display = "none";
        }, 3000
    )
    
    
}

modeBtn.addEventListener("click", ()=>{
    screenSwitcher(true)
})

function screenSwitcher(changeMode){
    let screenMode = localStorage.getItem("mode")
    if (screenMode == "night"){
        if (changeMode) {
            lightMode()
            localStorage.setItem("mode", "day")
        }else {
            darkMode()
        }
    }else if(screenMode == "day"){
        if(changeMode){
            console.log("not true")
            darkMode()
            localStorage.setItem("mode", "night")
        }else {
            lightMode()
        }
    }else{
        if(changeMode){
            darkMode()
            localStorage.setItem("mode", "night")
        }else screenMode ="day";
    }
}


//console.log(modeBtn.firstChild)
function darkMode(){
    bodyEl.classList.add("body-dark")
    modeBtn.firstElementChild.classList.replace( "fa-sun", "fa-moon")
}

function lightMode(){
    bodyEl.classList.remove("body-dark")
    modeBtn.firstElementChild.classList.replace("fa-moon", "fa-sun")
}

let dropdown = $('.dropdownMenuButton')
let dropdown_menu = $('.dropdown-menu-ul')
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


//dashboard

let total_balance = document.getElementById('total-balance')
let balance_toggle = document.getElementById('balance-toggle')
try {
    balance_toggle.addEventListener('click', (e)=>{
        if (balance_toggle.value == "on"){    
            toggleShowBalance(true)         
            balance_toggle.value = "off"
        }
        else if (balance_toggle.value == "off"){
            toggleShowBalance(false)
            balance_toggle.value = "on"
        }
    })
} catch (TypeError) {
}

function toggleShowBalance(boolean){

    let totalBalance = document.getElementById("total-balance")
    let taskEl = document.getElementById("task-el")
    let affilateEl = document.getElementById("affilate-el")
    let withdrawalEl = document.getElementById("withdraw-el")
    let totalEarnEl = document.getElementById("total-earn-el")

    if (boolean){
        totalBalance.innerText ="****"
        taskEl.innerText = "****"
        affilateEl.innerText = "****"
        withdrawalEl.innerText = "****"
        totalEarnEl.innerHTML = "****"
    }else{
        $.ajax({
            method:"get",
            url: "/user/currency/info/",
            success: function(data){
                let currency = data.currency
                totalBalance.innerText =`${currency} ${data.total_balance}`
                taskEl.innerText = `${currency} ${data.task}`
                affilateEl.innerText = `${currency} ${data.affilate}`
                withdrawalEl.innerText = `${currency} ${data.total_withdraw}`
                totalEarnEl.innerText = `${currency} ${data.total_earning}`
                
            },
            error: function(err){
                console.log(err)
            }
        })
    }
}



///////////////////////////
///////////////////////////
///////////////////////////
/////footer             ///
///////////////////////////
///////////////////////////
///////////////////////////

let footerDate = document.querySelector("#footer-date")
let date = new Date
footerDate.innerText = date.getFullYear()


let y_top_objectEl = document.querySelectorAll('.scroll-y-top-el')
let y_down_objectEl = document.querySelectorAll('.scroll-down-top-el')
let x_top_objectEl = document.querySelectorAll('.scroll-x-top-el')
let x_down_objectEl = document.querySelectorAll('.scroll-x-down-el')

objectEl(y_top_objectEl, 'Y', '+')
objectEl(y_down_objectEl, 'Y', '-')
objectEl(x_top_objectEl, 'X', '+')
objectEl(x_down_objectEl, 'X', '-')

function objectEl(elementClass, axis, sign){
    for (let element of elementClass){
        let observer = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting){
                    element.style.transform = `translate${axis}(0)`
                }else{
                    element.style.transform = `translate${axis}(${sign}50%)`
                }
            })
        })
        
        observer.observe(element)
    }
    
}


function test(url, option){
    fetch(url, option)
    .then(response  =>{
        return response.text()
    })
    .then(data => {
        let json_response = JSON.parse(data);

        if (json_response.success){
            
            pagedone.style.display = 'block'
            setTimeout(function(){
                pagedone.style.display = 'none'
                window.location.reload()
            }, 4000)
        }
        else if (json_response.error){
            var jsonObject = json_response;

            // Access the 'error' object
            var errorObject = jsonObject.error;
            let errorEl = document.querySelector('#error')


            // Iterate through the properties of the 'error' object
            for (var key in errorObject) {
                if (errorObject.hasOwnProperty(key)) {
                    var errorMessages = errorObject[key];

                    // Log or process the error messages
                    for (var i = 0; i < errorMessages.length; i++) {
                        
                        errorEl.innerText =`${key}:  ${errorMessages[i]}`
                    }
                }
            }
        }
      
    })
    .catch(error =>{
      console.log(error)
    })
}