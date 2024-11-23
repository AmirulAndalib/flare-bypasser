import importlib
import distutils.core


def is_installed(pkgname):
  try:
    if importlib.import_module(pkgname):
      return True
  except Exception:
    pass
  return False

print("flare-bypasser installer: cv2 is installed: " + str(is_installed('cv2')), flush = True)
print("flare-bypasser installer: numpy is installed: " + str(is_installed('numpy')), flush = True)

install_requires = [
  'asyncio',
  'uuid',
  'urllib3',
  'numpy',
  'certifi==2024.8.30',
  'websockets==14.0',
  'zendriver_flare_bypasser==0.2.0',  # 'zendriver @ git+https://github.com/yoori/zendriver.git@flare-bypasser'
  'argparse',
  'oslex',
  'jinja2',

  # Server dependecies
  'fastapi',
  'uvicorn',

  'xvfbwrapper==0.2.9 ; platform_system != "Windows"',
  'gunicorn ; platform_system != "Windows"',
]

if not is_installed('cv2'):
  # can be installed as opencv-python or opencv-contrib-python
  install_requires += ['opencv-python']

distutils.core.setup(install_requires=install_requires)
