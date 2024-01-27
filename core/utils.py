from sklearn.feature_extraction.text import TfidfVectorizer
from core.models import Project
from sklearn.metrics.pairwise import cosine_similarity

def extract_features():
    projects = Project.objects.all()
    combined_texts = []

    for project in projects:
        # Basic text preprocessing
        description = project.description.strip().lower() if project.description else ""
        category_name = project.category.name.strip().lower() if project.category.name else ""
        location = project.location.strip().lower() if project.location else ""

        text = f"{description} {category_name} {location}"
        combined_texts.append(text)

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(combined_texts)

    return tfidf_matrix, vectorizer

def calculate_similarity(tfidf_matrix, user_vector):
    return cosine_similarity(tfidf_matrix, user_vector)

def create_user_vector(user_preferences, vectorizer):
    category_names = [category.name for category in user_preferences['preferred_categories'].all()]
    categories_text = ' '.join(category_names)
    country_names = [country.name for country in user_preferences['preferred_countries'].all()]
    countries_text = ' '.join(country_names)
    combined_preferences = f"{categories_text} {countries_text}"

    # Transform the combined_preferences using the same vectorizer used for projects
    user_vector = vectorizer.transform([combined_preferences])

    return user_vector