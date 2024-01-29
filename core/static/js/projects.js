// Get the modal
var modal = document.getElementById("projectModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Handle opening the modal and setting the content
document.querySelectorAll('.view-details').forEach(function(link) {
    link.onclick = function() {
        var projectId = this.getAttribute('data-project-id');

        // AJAX request to fetch project details
        fetch('/project_details/' + projectId + '/')
            .then(response => response.json())
            .then(data => {
                // Update modal content with fetched data
                document.getElementById('modalTitle').textContent = data.title;
                document.getElementById('modalDescription').textContent = data.description;
                document.getElementById('modalLocation').textContent = data.location;

                // Display the modal
                modal.style.display = "block";
            })
            .catch(error => console.error('Error:', error));
    };
});
