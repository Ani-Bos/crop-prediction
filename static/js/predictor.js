let a = document.getElementById("toggleshow");
let sub = document.getElementById("sub");
let b= document.getElementById("tog");
sub.addEventListener('click', () => {
    console.log("sfhbjs")
    a.style.display = "none";
    b.classList.remove('dnone');
})