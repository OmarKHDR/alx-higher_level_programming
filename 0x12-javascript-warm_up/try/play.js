const myButton = document.querySelector("#but");
const myHead = document.querySelector("h1");

getuser = () =>
{
    var name = localStorage.getItem("name")
    if(name)
    {
        return name
    }
    else{
        let name = prompt("enter your name")
        localStorage.setItem("name", name)
        return name
    }
}
myHead.textContent= `hello, ${getuser()}`


myButton.onclick = () =>
{
    localStorage.setItem("name", "");
    getuser();
    myHead.textContent= `hello, ${getuser()}`
}