import os
import pygame

script_directory = os.path.dirname(os.path.realpath(__file__))
print(script_directory)

asset_path = os.path.join(script_directory,'assets')
print(asset_path)

_assets_images = sorted(list(entry.name for entry in os.scandir(asset_path)
                      if entry.is_file))

images = list(pygame.image.load(os.path.join(asset_path,image)) 
              for image in sorted(list(entry.name 
                                       for entry in os.scandir(asset_path)
                                        if entry.is_file)))

print(images)
