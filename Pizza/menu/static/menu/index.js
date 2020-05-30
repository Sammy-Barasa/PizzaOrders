
let items=[]

let cartButton=document.querySelector("#UserCart")
    cartButton.addEventListener("click",(event)=> {
      event.preventDefault()
      console.log("clicked cartbutton!")  
      items.forEach((item)=>{
        let cart=document.querySelector("#listItems")
        let newlistItem=document.createElement("li")
        // let newButton=document.createElement("button")
         newlistItem.innerHTML=item
        //  newButton.setAttribute("id","delete")
        //  newButton.classList.add("btn btn-primary")
         newlistItem.classList.add("list-group-item")
        //  newlistItem.appendChild(newButton)
         cart.appendChild(newlistItem)
      })
      // get cart items via xml
    });

let modalButton=document.querySelectorAll("#confirm")
let confirmButton=modalButton.forEach(function(item){
    item.addEventListener("click",(event)=> {
    console.log("Confirm clicked.");
    let newItem=event.target.value
    console.log(newItem)
    items.push(newItem);
    console.log(items)
    document.querySelector("#itemcount").innerHTML=items.length
    return newItem
        //send via xml to /cart
    })
    
})
 


    