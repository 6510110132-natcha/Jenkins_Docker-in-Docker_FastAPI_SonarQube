from fastapi import FastAPI, HTTPException, Query
from typing import List
from app.utils import calculate_average, reverse_string

app = FastAPI(
    title="FastAPI Clean Code Example",
    description="Simple FastAPI app for Jenkins + Docker + SonarQube pipeline demo",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Hello from FastAPI with Jenkins & SonarQube!"}


@app.get("/average")
def get_average(numbers: List[float] = Query(..., description="List ของตัวเลข")):
    try:
        result = calculate_average(numbers)
        return {"average": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/reverse")
def get_reverse(text: str = Query(..., description="ข้อความที่ต้องการกลับ")):
    result = reverse_string(text)
    return {"reversed": result}


# 🚩 Intentional Code Smells
@app.get("/smell")
def code_smell_demo():
    # ❌ unused variable
    temp = "This variable is never used"

    # ❌ magic number
    threshold = 42

    # ❌ duplicated logic
    msg = "SonarQube"
    reversed1 = msg[::-1]
    reversed2 = msg[::-1]  # duplicated

    # ❌ bad exception handling (swallowing error)
    try:
        risky = 1 / 0
    except Exception:
        pass

    return {"status": "smelly", "threshold": threshold, "reverse": reversed1}
