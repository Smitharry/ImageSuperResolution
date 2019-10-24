from setuptools import setup

setup(name='imagesr',
      version='0.1',
      description='Image Super Resolution project',
      url="https://github.com/Smitharry/ImageSuperResolution",
      author='Maria Kuznetsova',
      author_email='kuznetsovamaria1996@gmail.com',
      install_requires=[
            'pillow',
            'tqdm'
      ],
      packages=['imagesr'],
      zip_safe=False)
