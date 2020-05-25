
let items=[]

let modalButton=document.querySelectorAll("#confirm")
  for(var i=0;i<=modalButton.length; i++)
  modalButton[i].addEventListener("click", (event)=> {
    console.log("Confirm clicked.");
    var newItem=event.target.value
    console.log(newItem)
      items.push(newItem);
      console.log(items)
      let theList=document.querySelector("#listCartItems")
      items.forEach(item => {
        let listitem = document.createElement("li")
        listitem.innerHTML=item
        theList.appendChild(listitem)
        
      });
      document.querySelector("#itemcount").innerHTML=items.length
      //send via xml to /cart
  });
let cartButton=document.querySelector("#UserCart")
    cartButton.addEventListener("click",   (event)=>{
      console.log("clicked me!")
      // console.log(items)
      // get cart items via xml
      
    });
    