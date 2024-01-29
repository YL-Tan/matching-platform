function fetchRecommendations() {
    fetch('/api/recommendations/')
        .then(response => response.json())
        .then(data => {
            let container = document.getElementById('recommendations-container');
            container.innerHTML = '';  // Clear existing content
            data['recommendations'].forEach(project => {
                let projectElement = document.createElement('div');
                projectElement.innerHTML = `<h4>${project.title}</h4><p>${project.description}</p>`;
                container.appendChild(projectElement);
            });
        })
        .catch(error => console.error('Error:', error));
}

fetchRecommendations();