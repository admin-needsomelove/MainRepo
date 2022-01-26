 #update reuirement.txt with whatever pckages you need
 source .venv/bin/activate
pip install -r lambda/requirements.txt --target lambda/layer/python/lib/python3.9/site-packages
zip -r python.zip python
