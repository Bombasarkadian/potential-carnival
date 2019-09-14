import random

from api.config import settings
from api.image_map import IMAGE_MAP


class ImagesService:
    IMAGES_COUNT = 10

    def __init__(self, session):
        self.session = session

    def select_image(self, img_id):
        choices = set(self.session.get().get('choices'))
        choices.add(img_id)

        self.session.update({
            'choices': list(choices)
        })
        return

    def generate_images(self):
        viewed = set(self.session.get().get('viewed'))
        images = set(IMAGE_MAP.keys())

        images_left = list(images - viewed)
        random.shuffle(images_left)

        selected_images = images_left[:self.IMAGES_COUNT]

        self.session.update({
            'viewed': list(viewed) + selected_images
        })
        return [self.generate_image(img_id) for img_id in selected_images]

    def generate_image(self, img_id):
        return {
            'id': img_id,
            'url': f'{settings["base_url"]}/static/img/{img_id}',
            'alt': img_id
        }
