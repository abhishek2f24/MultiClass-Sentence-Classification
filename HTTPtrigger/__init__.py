import logging
import azure.functions as func
import numpy as np
import time
from keras.models import load_model
from keras import backend as K
from transformers import AutoTokenizer,TFBertModel

global model, tokenizer
model = load_model('bert.hdf5', custom_objects={'TFBertModel':TFBertModel}, compile=False)
tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
        
        
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        start = time.time()
        query = name

        x_val = tokenizer(
            text=str(query),
            add_special_tokens=True,
            max_length=27,
            truncation=True,
            padding='max_length', 
            return_tensors='tf',
            return_token_type_ids = False,
            return_attention_mask = True,
            verbose = True)
        
        end = time.time()
        print(end - start)
        start1 = time.time()
        K.clear_session()
        end1 = time.time()
        print(end1 - start1)
        start2 = time.time()
        validation = model.predict({'input_ids':x_val['input_ids'],'attention_mask':x_val['attention_mask']})*10
        end2 = time.time()
        print(end2 - start2)
        start3 = time.time()
        
        pred = np.where(validation == np.max(validation))
        
        results = pred[1]
        result = results.item()
        end3 = time.time()
        print(end3 - start3)
        if result==0:
            return func.HttpResponse("Concept of query is Project Planning")
        elif result==1:
            return func.HttpResponse("Concept of the field is Process Flow Stream")
        elif result==2:
            return func.HttpResponse("Concept of the field is Operating Losses")
        elif result==3:
            return func.HttpResponse("Concept of the field is Operational Parameter")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
