var modal = document.getElementById("projectModal");

var span = document.getElementsByClassName("close")[0];

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Handle opening the modal and setting the content
document.querySelectorAll('.view-details').forEach(function(link) {
    link.onclick = function() {
        var projectId = this.getAttribute('data-project-id');

        fetch('/project_details/' + projectId + '/')
            .then(response => response.json())
            .then(data => {
                document.getElementById('modalTitle').textContent = data.title;
                document.getElementById('modalDescription').textContent = data.description;
                document.getElementById('modalLocation').textContent = data.location;

                modal.style.display = "block";
            })
            .catch(error => console.error('Error:', error));
    };
});
