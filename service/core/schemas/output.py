from pydantic import BaseModel

class APIOutput(BaseModel):
    garbage_type: str
    time_elapse: float
    time_elapsed_preprocessed: float