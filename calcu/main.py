from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def calculator_form(request: Request):
    # Renders the HTML form on the home page
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(request: Request):
    # Extracts data from the form and performs the calculation
    form_data = await request.form()
    a = float(form_data.get("a"))
    b = float(form_data.get("b"))
    operation = form_data.get("operation")

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return templates.TemplateResponse("index.html", {"request": request, "result": result})
