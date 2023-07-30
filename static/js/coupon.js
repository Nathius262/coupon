let bodyEl = document.querySelector("body")
let navEl = document.querySelectorAll(".navbar")
let modeBtn = document.getElementById("mode-btn")
let imgLogo = document.getElementById("header-logo")

window.addEventListener("DOMContentLoaded", ()=>{
    screenSwitcher(false)
})

function copyText() {
    // Get the text field
    var copyText = document.getElementById("myInput");

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
        changeMode?localStorage.setItem("mode", "day"):screenMode ="day"
        darkMode()
    }else if(screenMode == "day"){
        console.log("light mode activated!")
        changeMode?localStorage.setItem("mode", "night"):screenMode ="night"
        lightMode()
    }else{
        console.log("first timer")
        changeMode?localStorage.setItem("mode", "night"):screenMode ="night" 
    }

}

//console.log(modeBtn.firstChild)
function darkMode(){
    modeBtn.firstElementChild.classList.replace("fa-moon-o", "fa-sun-o")
    bodyEl.classList.add("body-dark")

}

function lightMode(){
    modeBtn.firstElementChild.classList.replace("fa-sun-o", "fa-moon-o")
    bodyEl.classList.remove("body-dark")
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
                //totalEarnEl.innerText = data.
                
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
