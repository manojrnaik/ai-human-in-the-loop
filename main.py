import asyncio
from src.agent_graph import app_graph
from src.models import HRStateSchema

async def main():
    # Setup standard systemic configurations token
    thread_id = "tx_channel_0091"
    config = {"configurable": {"thread_id": thread_id}}
    
    # Ingest baseline structural user query elements
    initial_input = {
        "employee_id": "EMP-8842",
        "bonus_increment_inr": 0.0
    }

    print("=== STAGE 1: INITIATING AUTONOMOUS AGENT ACTIONS ===")
    async for event in app_graph.astream(initial_input, config=config):
        print(f"Active Processing Node Signal: {list(event.keys())}")

    # Inspect current database cache matrix state to verify breakpoint alignment
    current_snapshot = await app_graph.aget_state(config)
    print(f"\nGraph Operational Status: Waiting state identified.")
    print(f"Next Node Target Stack: {current_snapshot.next}")
    print(f"Current Memory Log: {current_snapshot.values.get('execution_trail')}")
    print(f"System Safety Gate Flagged: {current_snapshot.values.get('system_safety_flag')}")

    print("\n=== STAGE 2: SIMULATING HUMAN INTERACTIVE REVIEW ===")
    print("Actioning state payload adjustments via dashboard admin panel...")
    
    # Reconstruct state values to inject authorization keys
    current_state_data = current_snapshot.values
    current_state_data["approval_status"] = "GRANTED"
    current_state_data["execution_trail"].append("Human Authorization Confirmed: Admin token hash signed.")

    # INJECTION STEP: Push updated values back down inside the checkpoint container
    await app_graph.aupdate_state(config, current_state_data, as_node="calculate_metrics_node")
    print("Database snapshot state hydrated with signature attributes successfully.")

    print("\n=== STAGE 3: RESUMING WORKFLOW PATH EXECUTIONS FROM BREAKPOINT ===")
    # Passing None as payload triggers the runtime engine to pick up right from where the snapshot left off
    async for event in app_graph.astream(None, config=config):
        print(f"Active Resumed Processing Node Signal: {list(event.keys())}")

    # Fetch absolute closing structural state configuration parameters
    final_snapshot = await app_graph.aget_state(config)
    print(f"\nFinal State Trail Evaluation Log:")
    for log in final_snapshot.values.get("execution_trail", []):
        print(f" - {log}")

if __name__ == "__main__":
    asyncio.run(main())
