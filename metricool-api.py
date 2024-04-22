from add_img import add_image
from add_publication import create_publication

def main():
    img_path = "img/test.jpg"

    # Llamar a la función para subir la imagen
    image_url = add_image(img_path)
    
    # Parámetros para crear la publicación
    publication_data = {
        "providers": [{"network": "facebook"}, {"network": "instagram"}],
        "publicationDate": {"dateTime": "2024-04-28T14:50:02", "timezone": "America/Lima"},
        "text": "🤗Testing post from Automating Bot",
        "media": [image_url],  # Usamos la URL de la imagen subida
        "mediaAltText": ["Descripción de la imagen"],
        "draft": "false",
        "hasNotReadNotes": "false",
        "autoPublish": "true",
        "shortener": "false",
        "firstCommentText": "",
        "smartLinkData": {"ids": []},
        "facebookData": {"type": "POST"},
        "instagramData": {"type": "POST", "showReelOnFeed": "true", "collaborators": []},
        "descendants": []
    }
    
    # Llamar a la función para crear la publicación
    create_publication(publication_data)

if __name__ == "__main__":
    main()
