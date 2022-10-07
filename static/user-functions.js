////// Submitting a location /////
// Get the modal
let submit_img_modal = document.getElementById("submit-img-modal");

// Get the button that opens the modal
let submit_img_btn = document.getElementById("submit-img-btn");

// Get the <span> element that closes the modal
let submit_span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
submit_img_btn.onclick = function() {
  submit_img_modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
submit_span.onclick = function() {
  submit_img_modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == submit_img_modal) {
    submit_img_modal.style.display = "none";
  }
}

////Editing a location modal ////


//for every edit button class in this thing 
// get the element
// add an eventlistener to the element

let edit_button = document.getElementById("edit-button-1");

let edit_img_modal = document.getElementById("edit-img-modal");

let edit_description_text = document.getElementById("edit-img-description");

edit_button.addEventListener("click", () => {
  const queryString = new URLSearchParams({'image_id':edit_button.value})
  const url = `/view-image?${queryString}`;
  fetch(url)
  .then((response) => response.json())
  .then((image_details) => {
    edit_description_text.value += image_details[0]['description']
    edit_img_modal.style.display = 'block';
  }) 

})



let edit_span = document.getElementsByClassName("close")[1];

edit_span.onclick = function(){
  edit_loc_modal.style.display = "none";
 
}
//When the user clicks on edit location
//Get location id
//Edit location id
