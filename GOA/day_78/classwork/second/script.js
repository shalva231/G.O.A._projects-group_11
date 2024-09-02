

function changeText() {
    let changed = document.getElementById("paragraph");
    changed.textContent = "hello";
    changed.style.color = "green";
    changed.style.fontSize = "24px";

    setTimeout(3000)    
    
    changed.textContent = "this text will change :o"
    changed.style.color = "black";
    changed.style.fontSize = "15px";
}
