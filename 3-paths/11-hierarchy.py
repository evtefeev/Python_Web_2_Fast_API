from fastapi import FastAPI, Path, HTTPException


app = FastAPI()


employees_db = {
    "sales": {
        "1": {"name": "Alice", "position": "Sales Manager"},
        "3": {"name": "Eve", "position": "Sales Associate"}
    },
    "engineering": {
        "2": {"name": "Bob", "position": "Software Engineer"},
        "4": {"name": "Charlie", "position": "DevOps Engineer"}
    },
}


@app.get("/departments/{department_id}/employees/{employee_id}")
async def get_employee(
    department_id: str = Path(..., title="ID of the department"),
    employee_id: str = Path(..., title="ID of the employee")
):
    department = employees_db.get(department_id)
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")


    employee = department.get(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found in the given department")


    return employee
