var uzmiFormu;
var uzmiFrame;
var uzmiInfo;

uzmiFormu=document.getElementById("forma");
uzmiFrame=document.getElementById("frame1");
uzmiInfo=document.getElementById("info");

function prikaziFormu(){
    uzmiFormu.style.display="block";
    if(window.innerWidth>10){

document.getElementsByClassName("slika")[2].classList.add("slideInLeft");
document.getElementsByClassName("slika")[2].classList.add("animated");
}
}
function skloniFormu(){
    uzmiFormu.style.display="none";
}

function prikaziFrame(){
    uzmiFrame.style.display="block";
    if(window.innerWidth>10){
   
    document.getElementsByClassName("slika")[1].classList.add("slideInLeft");
    document.getElementsByClassName("slika")[1].classList.add("animated");
}
}

function skloniFrame(){
    uzmiFrame.style.display="none";
}
function prikaziInfo(){
    uzmiInfo.style.display="block";
    if(window.innerWidth>10){
    
    document.getElementsByClassName("slika")[0].classList.add("slideInLeft");
    document.getElementsByClassName("slika")[0].classList.add("animated");
}
}
function skloniInfo(){
    uzmiInfo.style.display="none";
}