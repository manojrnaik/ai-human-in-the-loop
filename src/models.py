from typing import List, Literal, Optional, Dict, Any
from pydantic import BaseModel, Field

class HRStateSchema(BaseModel):
    employee_id: str = Field(..., description="Unique enterprise tracker ID for resource classification")
    bonus_increment_inr: float = Field(..., description="Target allocation financial update value")
    system_safety_flag: bool = Field(default=False, description="Verification gate tracking indicator")
    approval_status: Literal["PENDING", "GRANTED", "REJECTED"] = Field(default="PENDING")
    execution_trail: List[str] = Field(default_factory=list, description="Historical graph state node audit logs")
