// array  representing cart
let items=[]


const ListCart=(items,func)=>{
let cartButton=document.querySelector("#UserCart")
    cartButton.addEventListener("click",(event)=> {
      event.preventDefault()
      // get cart items via xml
      console.log("clicked cartbutton!")  
      items.forEach((item,index)=>{
        let cart=document.querySelector("#listItems")
        let newlistItem=document.createElement("li")
        let newButton=document.createElement("button")
            newButton.setAttribute("id","delete")
            newButton.setAttribute("type","button")
            newButton.setAttribute("class","btn")
            newButton.setAttribute("value",`${index}`)
            newButton.classList.add("btn-danger")
            newButton.innerHTML = "Remove"
            func(newButton)
            newlistItem.innerHTML=item
            newlistItem.appendChild(newButton)
            newlistItem.classList.add("list-group-item")
            cart.appendChild(newlistItem)
      }) 
    });
  }



let modalButton=document.querySelectorAll("#confirm")
let confirmButton=modalButton.forEach(function(item){
    item.addEventListener("click",(event)=> {
    console.log("Confirm clicked.");
    let newItem=event.target.value
    console.log(newItem)
    //send via xml to /cart
    items.push(newItem);
    console.log(items)
    document.querySelector("#itemcount").innerHTML=items.length
    return newItem   
    })
    
})
const CartDeleteButton=(btn)=>{
  //add eventlistener to every delete button in the cart
  btn.addEventListener("click",(event)=>{
    console.log("deleteButtonClicked!")
    let itemToRemove=event.target.value
    items.splice(`${itemToRemove}`,1)
    console.log(items)
    btn.parentElement.style.display="none"
    // update  cart via xml
  })
}

function SendOrder(items){
  console.log(items)
  console.log("sent order")
  //send order via xml request
}

let PlaceOrder= document.querySelector("#Order")
    PlaceOrder.addEventListener("click",(event,items)=>{

    })


      


ListCart(items,CartDeleteButton)

 