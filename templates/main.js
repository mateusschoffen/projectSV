function open_menu(){
    document.getElementById("menuop").style.width ='13%';
    document.getElementById('meio').style.marginLeft = '13%'
}
function close_menu(){
    document.getElementById("menuop").style.width = '0px'
    document.getElementById('meio').style.marginLeft = '0'
}
function open_filter(){
    document.getElementById("visi").style.visibility  = false
 
    
    

}
const selected = document.querySelector(".selected");
const optionsContainer = document.querySelector(".options-container");

const optionsList = document.querySelectorAll(".option");

selected.addEventListener("click", () => {
  optionsContainer.classList.toggle("active");
});

optionsList.forEach(o => {
  o.addEventListener("click", () => {
    selected.innerHTML = o.querySelector("label").innerHTML;
    optionsContainer.classList.remove("active");
  });
});