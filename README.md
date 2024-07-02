Greystone Labs Backend Code Challenge

## Loan Amoritization API

This project is a REST API for a Loan Amortization app built using FastAPI. The API allows clients to:
- Create a user
- Create a loan
- Fetch a loan schedule
- Fetch a loan summary for a specific month
- Fetch all loans for a user
- Share a loan with another user



## setup 
1.  Install Dependencies
    ```pip install -r requirements.txt```

2. Run 
    ```uvicorn app.main:app --reload```


3. The API documentation will be available at 
    http://127.0.0.1:8000/docs


###################################################################

### API Endpoints


## User Endpoints

## Create User

- POST /api/v1/users/
-  Request Body:
```
{
  "email": "user@example.com",
  "name": "User Name"
}
```
Response:
```
{
  "id": 1,
  "email": "user@example.com",
  "name": "User Name"
}
```

## Read User
- GET /api/v1/users/{user_id}
- Response:
```
{
  "id": 1,
  "email": "user@example.com",
  "name": "User Name"
}
```


## Loan Endpoints
## Create Loan

- POST /api/v1/loans/
- Request Body:
```
{
  "amount": 10000,
  "annual_interest_rate": 5,
  "loan_term_months": 12,
  "owner_id": 1
}
```
- Response:
```
{
  "id": 1,
  "amount": 10000,
  "annual_interest_rate": 5,
  "loan_term_months": 12,
  "owner_id": 1
}
```

## Read Loan
- GET /api/v1/loans/{loan_id}
- Response:
```
{
  "id": 1,
  "amount": 10000,
  "annual_interest_rate": 5,
  "loan_term_months": 12,
  "owner_id": 1
}
```

## Get Amortization Schedule
- GET /api/v1/loans/{loan_id}/amortization
- Response:
```
[
  {
    "month": 1,
    "remaining_balance": 9183.75,
    "monthly_payment": 856.07,
    "principal_payment": 814.40,
    "interest_payment": 41.67
  },
  ...
  {
    "month": 12,
    "remaining_balance": 0,
    "monthly_payment": 856.07,
    "principal_payment": 852.85,
    "interest_payment": 3.22
  }
]
```



######################################################################

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
    Ensure you installed the testing dependencies: ```pip install pytest httpx pytest-asyncio```
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