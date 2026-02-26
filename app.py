from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from core.orchestrator import StartupOrchestrator
from utils.database import init_db
from utils.pdf_generator import generate_pdf
import os
import uuid

app = FastAPI()
init_db()

orchestrator = StartupOrchestrator()


class IdeaRequest(BaseModel):
    idea: str


@app.post("/generate-pdf")
def generate_pdf_report(request: IdeaRequest):

    result = orchestrator.run(request.idea)

    filename = f"report_{uuid.uuid4().hex}.pdf"
    file_path = os.path.join("reports", filename)

    os.makedirs("reports", exist_ok=True)

    generate_pdf(result, file_path)

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type='application/pdf'
    )