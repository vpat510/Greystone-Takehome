Greystone Labs Backend Code Challenge

## Loan Amoritization API

## setup 
1. Install Dependencies
    ```pip install -r requirements.txt```

2. Run 
    ```uvicorn app.main:app --reload```


3. Access docs
    http://127.0.0.1:8000/docs








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