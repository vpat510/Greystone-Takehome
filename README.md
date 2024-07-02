Greystone Labs Backend Code Challenge

## Loan Amoritization API

## setup 
1. Install Dependencies
    ```pip install -r requirements.txt```

2. Run 
    ```uvicorn app.main:app --reload```


3. Access docs
    http://127.0.0.1:8000/docs


###################################################################
 ## Tests

 1. To Run all tests
    ```pytest```

2. To run specific tests
        ```pytest tests/test_main.py```
        ```pytest tests/test_amortization.py```

3. Might need to set PYTHONPATH. You need to set the PYTHONPATH to the root of your project directory so that Python can find the app module.
run on terminal:       
    ```export PYTHONPATH=.```

4. MISC 
     pytest for running tests
    httpx for making HTTP requests to the FastAPI endpoints.


######################################################################

## FASTAPI notes 
- https://fastapi.tiangolo.com
- quickly build API, fastest web framework
- async server framework under the hood 
- scarlette x pydantic
- install uvicorn (async server implemenation)
- type hints -> declare type lol
- concurrency -> await ... 
- hot reload: uvicorn main:app --reload
- http://127.0.0.1:8000/docs -> automatic docs




## MISC

Issues with code-runner because python needs to be python3 on MacBook
fixed:
https://stackoverflow.com/questions/71804847/vscode-python-running-ommand-error-bin-sh-python-command-not-found
https://stackoverflow.com/questions/76240654/enable-xlint-for-vscode-java-compiling/76251185#76251185
"python": "python -u",  => python3

Issue with pylance
https://stackoverflow.com/questions/71918703/visual-studio-code-pylance-report-missing-imports
add the python path