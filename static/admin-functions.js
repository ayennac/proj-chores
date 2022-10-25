//TO DO:
// [] Add event listeners to each of the Update Info Buttons
// [] Call the server to update the submission status of the file

let update_buttons = document.getElementsByClassName("update-info");

for(update_button of update_buttons){
    const my_button = update_button
    my_button.addEventListener("click", () => {
    image_id = my_button.value
    const submission_status =   document.getElementById(`submission-status-${image_id}`).value;
    console.log(submission_status)
    const queryString = new URLSearchParams({'image_id':image_id, 'image_approval':submission_status})
    // console.log(edit_button.value)
    const url = `/admin-edit-status?${queryString}`;
    fetch(url)
    .then((response) => response.json())
    .then((image_details) => {
        console.log(image_details)
    })

    })
}
