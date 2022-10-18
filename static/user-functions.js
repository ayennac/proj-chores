
////// Submitting a image /////////////////////////

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

////Editing an image modal ////


let edit_button = document.getElementById("edit-button-1");

//get all the edit buttons 
//for every edit button class in this thing 
// get the element
// add an eventlistener to the element

let edit_img_modal = document.getElementById("edit-img-modal");

let edit_description_text = document.getElementById("edit-img-description");
let edit_alt_text = document.getElementById("edit-alt-text");
let edit_img_file = document.getElementById("img-prev");
let edit_img_id = document.getElementById("edit-img-id");


let edit_buttons = document.getElementsByClassName("edit-button");
console.log(edit_buttons)

// console.log(edit_buttons)

for (edit_button of edit_buttons){
  const my_button = edit_button
  my_button.addEventListener("click", () => {
    console.log(my_button)
    const queryString = new URLSearchParams({'image_id':my_button.value})
    // console.log(edit_button.value)
    const url = `/view-image?${queryString}`;
    fetch(url)
    .then((response) => response.json())
    .then((image_details) => {
      edit_img_file.innerHTML = `<video src = '${image_details[0]['image_src']}' style = "height: 100px;">`
      edit_alt_text.value = image_details[0]['alt_text']
      edit_description_text.value = image_details[0]['description']
      edit_img_id.value = image_details[0]['image_id']
      edit_img_modal.style.display = 'block';
    }) 
  })
}



let edit_span = document.getElementsByClassName("close")[1];

edit_span.onclick = function(){
  edit_img_modal.style.display = "none";
 
}




function handleFiles(event) {
  const files = event.target.files;
  //set classname to active class which has the right dimensions
  //style = "width:300px;height:400px"
  let canvas = document.getElementById('canvas');
  let video = document.getElementById("preview-video");
  
  video.src = URL.createObjectURL(files[0]);
  video.load();
  video.play();
  // let ctx = canvas.getContext('2d');
  // ctx.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);  
  // const thumbnailURL = canvas.toDataURL();
  // console.log(thumbnailURL);
}

document.getElementById("input-img").addEventListener("change", handleFiles, false);

