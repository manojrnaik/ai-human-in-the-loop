import logging
from typing import Dict, Any, Tuple
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from src.models import HRStateSchema

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")
logger = logging.getLogger("HITLOrchestrationEngine")

# Node 1: Automated Aggregation Layer
async def calculate_metrics_node(state: Dict[str, Any]) -> Dict[str, Any]:
    logger.info("Node Execution: Calculating performance evaluation payroll metrics.")
    validated = HRStateSchema(**state)
    
    # Simulate internal agent business arithmetic computation
    validated.bonus_increment_inr = 75000.00
    validated.execution_trail.append("Calculated target bonus metrics successfully.")
    
    # Trigger system flag if allocation breaches standard company spending limits
    if validated.bonus_increment_inr > 50000.00:
        validated.system_safety_flag = True
        validated.execution_trail.append("Alert: Spending threshold breached. Compiling system breakpoint interruption.")
        
    return validated.model_dump()

# Node 2: Restricted Transaction Node (Requires verified permission status parameters)
async def process_transaction_node(state: Dict[str, Any]) -> Dict[str, Any]:
    logger.info("Node Execution: Accessing internal accounting pipeline ledger.")
    validated = HRStateSchema(**state)
    
    if validated.approval_status != "GRANTED":
        logger.error("CRITICAL SAFETY VOID: Attempted restricted node entry without human token signature.")
        validated.execution_trail.append("Execution aborted: Safety compliance error.")
        return validated.model_dump()
        
    validated.execution_trail.append("Success: Financial payload dispatched to central banks.")
    return validated.model_dump()

# Compile the graph structure with explicit interrupt rules
workflow = StateGraph(dict)

# Register workflow operational logic structures
workflow.add_node("calculate_metrics_node", calculate_metrics_node)
workflow.add_node("process_transaction_node", process_transaction_node)

# Set systemic transitions paths
workflow.add_edge(START, "calculate_metrics_node")
workflow.add_edge("calculate_metrics_node", "process_transaction_node")
workflow.add_edge("process_transaction_node", END)

# Instantiate DB simulation persistence checkpoint layer
checkpointer = MemorySaver()

# COMPILE STEP: Tell the engine to drop execution thread BEFORE entry to high-risk areas
app_graph = workflow.compile(
    checkpointer=checkpointer,
    interrupt_before=["process_transaction_node"]
)
