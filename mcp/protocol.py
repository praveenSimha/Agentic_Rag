import uuid
from datetime import datetime
from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class MCPMessage:
    sender: str
    receiver: str
    type: str
    trace_id: str
    payload: Dict[str, Any]
    timestamp: str = datetime.now().isoformat()

def create_mcp_message(
    sender: str,
    receiver: str,
    type_: str,
    payload: Dict[str, Any],
    trace_id: Optional[str] = None,
    timestamp: Optional[str] = None
) -> Dict[str, Any]:
    return {
        "sender": sender,
        "receiver": receiver,
        "type": type_,
        "trace_id": trace_id or str(uuid.uuid4()),
        "timestamp": timestamp or datetime.now().isoformat(),
        "payload": payload
    }
