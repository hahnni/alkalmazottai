This repo is represents how to create documenteation with LLM model. 
The modeil is gpt-3.5-turbo. 

### Creating Documentation Porcess

After push to the githup repo start jobs to use the model and create documentation from code. 
The generate_docs_script.py python script is interact the OpenAI API and sending code as a promt and receiving documentation an a response. 

After generating docs it commiting in docs folder. 

There is some issue with the API authenticaton, we need to configure the API key for that. 
