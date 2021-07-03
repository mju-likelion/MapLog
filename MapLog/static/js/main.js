
const main = document.querySelector(".main__container"),
    sub = document.querySelector(".sub__container"),
    pr = document.querySelector(".pr__container"),
    body = document.querySelector("body"),
    downBtnMain = main.querySelector(".favicon"),
    downBtnSub = sub.querySelector(".favicon"),
    upBtnTop = pr.querySelector(".favicon");


downBtnMain.addEventListener("click", function() { 
    sub.scrollIntoView({behavior: "smooth", block: "start"}); 
});

downBtnSub.addEventListener("click", function() { 
    pr.scrollIntoView({behavior: "smooth", block: "start"}); 
});

upBtnTop.addEventListener("click", function() { 
    body.scrollIntoView({behavior: "smooth", block: "start"}); 
});